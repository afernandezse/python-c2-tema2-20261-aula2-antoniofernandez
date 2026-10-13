# Tema 2. Plantillas Jinja2 y sitios estáticos con Pelican

## 🗒️ Requisitos

Necesitas Python 3.10 o superior y Git. Desde la raíz del repositorio, crea
un entorno virtual e instala las dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

En Windows, activa el entorno con `.venv\Scripts\activate`.

## 📝 Enunciados y versión para estudiantes

Los ejercicios están organizados por bloques, siguiendo el patrón de
`python-c1-tema2`: un archivo `ej2XN.py` con el enunciado en su docstring
y un archivo `ej2XN_test.py` con sus pruebas. Aunque el nombre del repositorio
termine en **-sol**, esta rama contiene la **versión para estudiantes, sin
soluciones**: funciones con TODO y `NotImplementedError`, plantillas por
completar y archivos de configuración y contenido iniciales.
Lee los enunciados, implementa cada ejercicio y comprueba los tests sin
modificarlos. Los datos JSON y el SVG se conservan como entradas.

Los apartados del tema junto con los ejercicios son los siguientes:

| Apartado | Ejercicios |
| --- | --- |
| a. Sintaxis y motor de plantillas Jinja2 | [ej2a1](2a/ej2a1.py) [ej2a2](2a/ej2a2.py) [ej2a3](2a/ej2a3.py) [ej2a4](2a/ej2a4.py) |
| b. Automatización con Python y Jinja2 | [ej2b1](2b/ej2b1.py) [ej2b2](2b/ej2b2.py) [ej2b3](2b/ej2b3.py) [ej2b4](2b/ej2b4.py) |
| c. Generación y publicación con Pelican | [ej2c1](2c/ej2c1.py) [ej2c2](2c/ej2c2.py) [ej2c3](2c/ej2c3.py) [ej2c4](2c/ej2c4.py) [ej2c5](2c/ej2c5.py) |

Debes configurar el autoescape al implementar los ejercicios de Jinja2.
Usa únicamente plantillas y contenido de confianza; el autoescape no convierte Jinja2
en un entorno seguro para ejecutar plantillas ajenas.

## 💻 Comandos

### Ejecutar las pruebas

```bash
python -m pytest
python -m pytest 2a/ej2a1_test.py
python -m pytest 1b
python -m pytest 1c
```

Hay **70 pruebas**. Inicialmente se esperan fallos intencionados hasta
implementar los ejercicios; la protección de publicación sin autorización
ya está presente y puede pasar su prueba. Las pruebas usan archivos temporales
y simulan la publicación: no necesitan credenciales ni publican en GitHub.
Si una prueba falla, revisa el enunciado y el error antes de volver a intentarlo.

Los comandos de generación, visualización y publicación siguientes son
aplicables **después de implementar** los ejercicios y completar sus plantillas,
contenido y configuración. Los scaffolds actuales no generan un sitio operativo.

### Generar HTML con Jinja2

```bash
python 2b/generar_web.py
python 2b/ej2b3.py
python 2b/ej2b4.py
```

Al completar ej2b2, el generador deberá leer [datos.json](2b/datos.json), cargar
[index.html](2b/templates/index.html) y escribir `2b/output/index.html`.
Entonces podrás abrir ese archivo en el navegador. Mantén las rutas por
defecto relativas al script, no al directorio del terminal.

Sigue este orden en el bloque b: configura el entorno en **ej2b1**, genera
tu primera web desde JSON en **ej2b2**, reutiliza una estructura común con
herencia en **ej2b3** y crea un catálogo con macros en **ej2b4**.
Los dos últimos ejercicios deben reutilizar el mismo generador y los datos del
sitio para escribir `2b/output/bienvenida.html` y `2b/output/catalogo.html`.
Haz que ambas páginas hereden de [base.html](2b/templates/base.html) y que el
catálogo reutilice la macro que implementarás en [macros.html](2b/templates/macros.html).

### Inicializar y generar un sitio Pelican

Para practicar la inicialización, ejecuta `pelican-quickstart` y elige una
carpeta nueva, **distinta de `2c/sitio`**, para no sobrescribir los archivos
de trabajo. [2c/sitio](2c/sitio) contiene únicamente archivos iniciales:
completa `pelicanconf.py`, `content/bienvenida.md` y después `publishconf.py`.

```bash
pelican-quickstart
cd 2c/sitio
pelican content -s pelicanconf.py
python -m http.server --directory output 8000
```

Abre `http://localhost:8000` y detén el servidor con Ctrl+C.

En Pelican, los metadatos del artículo van al principio del Markdown en
líneas `Title:`, `Date:`, `Category:`, etc., seguidas de una línea vacía.
Este encabezado cumple la función de *frontmatter*, pero **no** lleva
delimitadores YAML `---`. Los recursos se referencian con rutas como
`![Imagen]({static}/images/pelican.svg)` y su carpeta debe figurar en
`STATIC_PATHS`.

Tras completar y revisar `publishconf.py`, genera la versión de producción
desde `2c/sitio`:

```bash
pelican content -s publishconf.py
```

### Publicar en GitHub Pages

Revisa primero `SITEURL` en [publishconf.py](2c/sitio/publishconf.py):
debe ser la URL pública de **tu** sitio, incluyendo el nombre del repositorio
si se trata de una página de proyecto. Configura GitHub Pages para publicar
desde la rama `gh-pages`, carpeta raíz, en Settings → Pages.

Desde la raíz del repositorio:

```bash
python 2c/ej2c5.py
```

Al implementar ej2c5, haz que muestre los comandos sin ejecutarlos por defecto.
Conserva la autorización explícita: solo cuando hayas revisado la configuración
y tengas permisos para publicar, ejecuta:

```bash
python 2c/ej2c5.py --publicar
```

Tu implementación deberá generar el sitio con `publishconf.py` y después usar
`ghp-import` para publicar únicamente la salida HTML en `gh-pages`, con `.nojekyll`,
sin forzar el push.
La publicación real requiere Git, un remoto `origin` correcto y autenticación
configurada localmente; nunca incluyas credenciales en los archivos del curso.
Si falla la generación, tu implementación debe impedir la publicación.

### Guardar los ejercicios

```bash
git pull
git add .
git commit -m "Completar ejercicios del tema 2"
git push
```

Las carpetas de salida y el entorno virtual están excluidos de Git.
Consulta el Tema 0 si necesitas ayuda para ejecutar tests o enviar tus cambios.