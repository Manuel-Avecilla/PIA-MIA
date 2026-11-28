import clips
from motor import EQUIPOS, crear_entorno, diagnosticos, explicar


def mostrar_diagnosticos_e_informe():
    """Ejecuta el motor con la estrategia por defecto y muestra diagnosticos e informe."""
    env, informe = crear_entorno()
    env.run()
    for equipo, problema, regla in diagnosticos(env):
        print(equipo, problema, regla)
    print(informe)


def _obtener_agenda(env):
    """Devuelve la lista de activaciones pendientes como tuplas (nombre, salience)."""
    agenda = []
    for activacion in env.activations():
        agenda.append((activacion.name, activacion.salience))
    return agenda


def mostrar_ejecucion_por_estrategia():
    """Compara la ejecucion paso a paso entre las estrategias DEPTH y BREADTH."""
    estrategias = (clips.Strategy.DEPTH, clips.Strategy.BREADTH)
    for estrategia in estrategias:
        env, informe = crear_entorno(estrategia=estrategia)
        while True:
            agenda = _obtener_agenda(env)
            if not agenda:
                break
            print(agenda)
            env.run(1)
        print(informe)


def mostrar_explicaciones():
    """Ejecuta el motor e imprime la explicacion detallada para cada equipo."""
    env, informe = crear_entorno()
    env.run()
    for datos_equipo in EQUIPOS:
        id_equipo = datos_equipo["id"]
        print(explicar(env, informe, id_equipo), "\n")


def main():
    """Ejecuta las demostraciones principales del sistema experto de red."""
    mostrar_diagnosticos_e_informe()
    mostrar_ejecucion_por_estrategia()
    mostrar_explicaciones()


if __name__ == "__main__":
    main()
