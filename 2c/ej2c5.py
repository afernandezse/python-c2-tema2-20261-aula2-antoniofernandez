"""Enunciado: Automatiza la generación y el despliegue con ghp-import.

Construye primero el sitio usando publishconf.py y después importa output
con «ghp-import -n -p -b gh-pages output», sin forzar el push. Usa subprocess
con check=True: si falla Pelican, no debe ejecutarse el despliegue.
Por defecto muestra los comandos; SOLO la opción explícita --publicar
autoriza ejecutarlos. El push requiere un remoto configurado y permisos.
Las pruebas deben simular subprocess y nunca publicar ni acceder a la red.
Resuelve las rutas desde sitio, usa output por defecto y admite una salida
personalizada. Ejecuta ambos comandos con cwd=sitio y conserva la protección
confirmar=False, que debe rechazar la publicación sin ejecutar nada.
"""

from pathlib import Path
import subprocess


SITIO = Path(__file__).resolve().parent / "sitio"


def comandos_publicacion(sitio=SITIO, salida=None):
    """Devuelve los comandos de generación e importación con rutas absolutas."""
    # TODO: Construye ambos comandos con rutas absolutas, sin ejecutarlos.
    raise NotImplementedError("TODO: implementar comandos_publicacion")


def publicar(sitio=SITIO, salida=None, *, confirmar=False):
    """Publica únicamente con autorización; propaga cualquier fallo de comando."""
    if not confirmar:
        raise ValueError("Para publicar se necesita autorización explícita")
    # TODO: Genera y despliega en orden solo tras la autorización explícita.
    raise NotImplementedError("TODO: implementar publicar")


if __name__ == "__main__":
    import argparse
    import shlex

    parser = argparse.ArgumentParser(description="Generar y publicar el sitio Pelican")
    parser.add_argument("--publicar", action="store_true", help="Autorizar el push a gh-pages")
    argumentos = parser.parse_args()
    if argumentos.publicar:
        publicar(confirmar=True)
    else:
        for comando in comandos_publicacion():
            print(shlex.join(comando))
