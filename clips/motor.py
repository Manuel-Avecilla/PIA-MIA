from pathlib import Path
import clips

RUTA_CLP = Path(__file__).parent / "red.clp"
CAMPOS = ("navega", "ping_externo", "ping_gateway", "ip", "led")

EQUIPOS = [
    {"id": "pc01", "navega": "no", "ping_externo": "ok"},
    {
        "id": "pc02",
        "navega": "no",
        "ping_externo": "falla",
        "ping_gateway": "ok",
        "ip": "si",
        "led": "encendido",
    },
    {
        "id": "pc03",
        "navega": "no",
        "ping_externo": "falla",
        "ping_gateway": "ok",
        "ip": "si",
        "led": "encendido",
    },
    {
        "id": "pc04",
        "navega": "no",
        "ping_externo": "falla",
        "ping_gateway": "falla",
        "ip": "no",
        "led": "apagado",
    },
    {
        "id": "pc05",
        "navega": "no",
        "ping_externo": "falla",
        "ping_gateway": "falla",
        "ip": "no",
        "led": "encendido",
    },
    {
        "id": "pc06",
        "navega": "si",
        "ping_externo": "ok",
        "ping_gateway": "ok",
        "ip": "si",
        "led": "encendido",
    },
]

DESCRIPCION = {
    "R1-dns": "navega=no y ping_externo=ok",
    "R3-salida-router": "navega=no, ping_externo=falla y ping_gateway=ok",
    "R5-dhcp-o-cable": "ping_gateway=falla e ip=no",
    "R6-cable": "diagnóstico 'dhcp-o-cable' y led=apagado",
    "R8-dhcp": "diagnóstico 'dhcp-o-cable' y led=encendido",
}


def insertar_equipos(env, equipos):
    """Inserta cada diccionario de equipo como un hecho en el entorno CLIPS."""
    plantilla_equipo = env.find_template("equipo")
    for datos_equipo in equipos:
        hecho_equipo = {}
        for campo, valor in datos_equipo.items():
            hecho_equipo[campo] = clips.Symbol(valor)
        plantilla_equipo.assert_fact(**hecho_equipo)


def crear_entorno(equipos=EQUIPOS, estrategia=clips.Strategy.DEPTH):
    """Crea y devuelve la tupla (env, informe) con las reglas cargadas y los equipos insertados.

    Registra la funcion auxiliar antes de cargar red.clp y configura la estrategia
    de resolucion de conflictos antes de insertar los hechos iniciales.
    """
    informe = []

    def registrar(equipo, texto):
        """Guarda en el informe la recomendacion emitida desde las reglas CLIPS."""
        informe.append((str(equipo), texto))

    env = clips.Environment()
    env.define_function(registrar)
    env.load(str(RUTA_CLP))
    env.strategy = estrategia
    env.reset()
    insertar_equipos(env, equipos)
    return env, informe


def diagnosticos(env):
    """Devuelve una lista de tuplas (equipo, problema, regla) en orden de creacion."""
    lista_diagnosticos = []
    for hecho in env.facts():
        if hecho.template.name == "diagnostico":
            equipo = str(hecho["equipo"])
            problema = str(hecho["problema"])
            regla = str(hecho["regla"])
            lista_diagnosticos.append((equipo, problema, regla))
    return lista_diagnosticos


def _formatear_datos_equipo(env, id_equipo):
    """Busca el hecho del equipo indicado y devuelve sus campos formateados como texto."""
    for hecho in env.facts():
        if hecho.template.name == "equipo" and str(hecho["id"]) == id_equipo:
            partes_datos = []
            for campo in CAMPOS:
                valor = hecho[campo]
                partes_datos.append(f"{campo}={valor}")
            return ", ".join(partes_datos)
    return None


def _obtener_pasos_diagnostico(env, id_equipo):
    """Recopila los diagnosticos de un equipo ordenados por su indice de creacion."""
    pasos = []
    for hecho in env.facts():
        if hecho.template.name == "diagnostico" and str(hecho["equipo"]) == id_equipo:
            indice = hecho.index
            problema = str(hecho["problema"])
            regla = str(hecho["regla"])
            pasos.append((indice, problema, regla))
    pasos.sort()
    return pasos


def _obtener_ultima_accion(informe, id_equipo):
    """Devuelve la ultima accion recomendada registrada para el equipo o None si no hay."""
    ultima_accion = None
    for equipo, texto in informe:
        if equipo == id_equipo:
            ultima_accion = texto
    return ultima_accion


def explicar(env, informe, id_equipo):
    """Construye y devuelve una explicacion legible de los diagnosticos y acciones de un equipo."""
    datos_formateados = _formatear_datos_equipo(env, id_equipo)
    pasos = _obtener_pasos_diagnostico(env, id_equipo)

    lineas = [f"{id_equipo} — datos: {datos_formateados}"]
    if not pasos:
        lineas.append("  Sin diagnóstico: ninguna regla encaja")
        return "\n".join(lineas)

    for numero_paso, (_, problema, regla) in enumerate(pasos, start=1):
        descripcion_regla = DESCRIPCION[regla]
        lineas.append(f"  {numero_paso}. {problema}  ({regla}: {descripcion_regla})")

    ultima_accion = _obtener_ultima_accion(informe, id_equipo)
    if ultima_accion is not None:
        lineas.append(f"  Acción recomendada: {ultima_accion}")
    else:
        lineas.append("  Sin acción individual (ver aviso al coordinador)")

    return "\n".join(lineas)
