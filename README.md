# Pitstop - MiniBlog de Automovilismo

**¡Atención! Esta aplicación se encuentra actualmente en proceso de desarrollo.**

Bienvenido al repositorio de **Pitstop**, un trabajo integrador para la materia PP1_PY. En este proyecto, estamos utilizando Flask para desarrollar un miniblog enfocado en artículos relacionados con el emocionante mundo del deporte automovilismo.

## Acerca de Pitstop

A través de este miniblog, aspiramos a crear un espacio donde los entusiastas de las carreras de autos puedan compartir y explorar artículos detallados sobre eventos, equipos, pilotos y tecnologías en el mundo del automovilismo.

## Tecnologías Utilizadas

Este proyecto está construido principalmente utilizando:

- **Flask**: Un framework web ligero y poderoso para Python que nos permite crear aplicaciones web de manera eficiente.
- **HTML y CSS**: Para diseñar y dar estilo a las páginas web, asegurando una experiencia visual agradable.
- **Bootstrap**: Como framework para dar estilo.
- **Python**: El lenguaje de programación que impulsa la lógica detrás de Pitstop.

## Funcionalidades Planificadas

Estamos trabajando arduamente en desarrollar las siguientes características para Pitstop:

- Registro de usuarios y autenticación segura.
- Publicación, edición y eliminación de artículos.
- Comentarios y participación de la comunidad.
- Categorización de artículos por tipos de carreras, equipos, pilotos, etc.

## Cómo Correr la Aplicación

1. Clona este repositorio: `git clone https://github.com/juanjcenturion/centurion-pit_stop-miniblog.git`
2. Navega al directorio del proyecto.
3. Crea un entorno virtual: `python3 -m venv venv`
4. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En macOS y Linux: `source venv/bin/activate`
5. Instala las dependencias: `pip install -r requirements.txt`
6. Configura las variables de entorno, como la clave secreta de Flask, la configuración de la base de datos, etc. (crear archivo `.env`).
7. Inicia la aplicación: `flask run --reload`

La aplicación estará disponible en `http://localhost:5000`.

## Endpoints

- `/`: Página de inicio con los artículos más recientes.
- `/articulo/<int:id>`: Página de un artículo específico.
- `/crear_articulo`: Página para crear un nuevo artículo (requiere autenticación).
- `/editar_articulo/<int:id>`: Página para editar un artículo existente (requiere autenticación).
- `/registro`: Página de registro de usuario.

¡Gracias por ser parte de Pitstop!

---
Este proyecto es parte del Trabajo Integrador para la materia PP1_PY. Insituto Tecnologico Rio Cuarto, 2023.
