import clips
import pytest
from motor import crear_entorno, diagnosticos, explicar

AVISO = ("aula", "Avisar al coordinador TIC")


@pytest.fixture
def ejecutado():
    """Crea un entorno con los equipos por defecto, lo ejecuta y devuelve (env, informe)."""
    env, informe = crear_entorno()
    env.run()
    return env, informe


def test_diagnosticos_finales(ejecutado):
    """Comprueba que se generan exactamente los diagnosticos esperados para los equipos con fallo."""
    env, _ = ejecutado
    obtenidos = set()
    for equipo, problema, _ in diagnosticos(env):
        obtenidos.add((equipo, problema))

    esperados = {
        ("pc01", "dns"),
        ("pc02", "salida-router"),
        ("pc03", "salida-router"),
        ("pc04", "dhcp-o-cable"),
        ("pc04", "cable"),
        ("pc05", "dhcp-o-cable"),
        ("pc05", "dhcp"),
    }
    assert obtenidos == esperados


def test_pc06_no_tiene_diagnostico(ejecutado):
    """Comprueba que el equipo sin problemas (pc06) no recibe ningun diagnostico."""
    env, _ = ejecutado
    equipos_diagnosticados = []
    for equipo, _, _ in diagnosticos(env):
        equipos_diagnosticados.append(equipo)

    assert "pc06" not in equipos_diagnosticados


def test_recomendaciones(ejecutado):
    """Comprueba que el informe contiene las recomendaciones individuales y el aviso al coordinador."""
    _, informe = ejecutado
    esperadas = {
        ("pc01", "Revisar la configuración DNS"),
        ("pc04", "Revisar el cable de red"),
        ("pc05", "Renovar la IP"),
        AVISO,
    }
    assert set(informe) == esperadas


def test_el_aviso_se_registra_una_sola_vez(ejecutado):
    """Comprueba que el aviso al coordinador TIC no se duplica aunque haya varios equipos afectados."""
    _, informe = ejecutado
    assert informe.count(AVISO) == 1


def test_la_estrategia_cambia_el_orden_pero_no_las_conclusiones():
    """Comprueba que DEPTH y BREADTH producen el mismo conjunto de conclusiones en distinto orden.

    En BREADTH la regla de aviso al coordinador con salience 10 se adelanta al primer lugar.
    """
    entorno_depth, informe_depth = crear_entorno(estrategia=clips.Strategy.DEPTH)
    entorno_depth.run()

    entorno_breadth, informe_breadth = crear_entorno(estrategia=clips.Strategy.BREADTH)
    entorno_breadth.run()

    assert set(informe_depth) == set(informe_breadth)
    assert informe_depth != informe_breadth
    assert informe_depth[0] == ("pc05", "Renovar la IP")
    assert informe_breadth[0] == AVISO


def test_explicacion_encadenada(ejecutado):
    """Comprueba que la explicacion de pc04 refleja el orden encadenado de las reglas aplicadas."""
    env, informe = ejecutado
    texto = explicar(env, informe, "pc04")
    assert "R5-dhcp-o-cable" in texto
    assert "R6-cable" in texto
    assert texto.index("R5-dhcp-o-cable") < texto.index("R6-cable")
