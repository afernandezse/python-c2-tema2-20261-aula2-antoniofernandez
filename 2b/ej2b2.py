"""
Enunciado:
Completa generar_web.py para leer datos.json (UTF-8), cargar index.html
mediante crear_entorno y generar un archivo HTML estático.
Crea la carpeta de salida si no existe y devuelve la ruta del HTML.
El JSON contiene titulo y cursos (lista de objetos con nombre y descripcion).
Completa index.html: muestra titulo en <title> y <h1>, y recorre cursos
en un <ul> con <li><strong>nombre</strong>: descripcion</li>.
Si no hay cursos, muestra <li>No hay cursos disponibles</li>.
Escapa los datos y lee el JSON antes de escribir para no sobrescribir la
salida si el JSON es inválido; propaga los errores de lectura y decodificación.
El generador debe aceptar el nombre de plantilla para reutilizarlo en 2b3/2b4.
Usa rutas relativas al script para los valores por defecto, no al terminal.
Ejecuta generar_web.py y abre 2b/output/index.html en el navegador.
"""

from generar_web import generar_web


if __name__ == "__main__":
    print(generar_web())
