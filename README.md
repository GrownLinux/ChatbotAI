# Chatbot con Procesamiento de PDF y URL

## Descripción
Este proyecto es un chatbot interactivo desarrollado en Python utilizando Flask. El chatbot es capaz de procesar archivos PDF y URLs, extraer información de ellos, y responder preguntas basadas en su contenido. Además, utiliza la API de OpenAI para generar respuestas inteligentes.

## Características
- Autenticación de usuarios (registro e inicio de sesión)
- Procesamiento y extracción de texto de archivos PDF
- Scraping y análisis de contenido de URLs
- Integración con la API de OpenAI para respuestas inteligentes
- Interfaz web interactiva

## Requisitos
- Python 3.7+
- Flask
- OpenAI API
- SQLite
- Otras dependencias listadas en `requirements.txt`

## Instalación
1. Clona el repositorio:
	git clone https://github.com/tu-usuario/nombre-del-repo.git
	cd nombre-del-repo

2. Crea un entorno virtual y actívalo:
python -m venv venv
source venv/bin/activate  # En Windows usa venv\Scripts\activate


3. Instala las dependencias:
pip install -r requirements.txt


4. Configura las variables de entorno:
- Copia `config.py.example` a `config.py`
- Crea un archivo `.env` en la raíz del proyecto
- Añade tus claves API y secretas al archivo `.env`:
  ```
  OPENAI_API_KEY=tu_clave_api_de_openai
  SECRET_KEY=tu_clave_secreta_de_flask
  ```

## Uso
1. Inicia la aplicación:
python main.py


2. Abre un navegador y ve a `http://localhost:8080`

3. Regístrate o inicia sesión para acceder al chatbot

4. Usa los botones para subir un PDF o procesar una URL, o simplemente escribe tus preguntas en el chat

## Estructura del Proyecto
- `main.py`: Punto de entrada de la aplicación Flask
- `chatbot/`: Contiene la lógica principal del chatbot
- `data_processing/`: Módulos para procesar PDFs y URLs
- `database/`: Manejo de la base de datos
- `templates/`: Archivos HTML para la interfaz web
- `static/`: Archivos CSS y JavaScript
- `config.py`: Configuración de la aplicación
- `requirements.txt`: Lista de dependencias

## Contribuir
Las contribuciones son bienvenidas. Por favor, sigue estos pasos para contribuir:

1. Haz un Fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Proceso de Desarrollo
1. Diseño de la arquitectura del chatbot
2. Implementación de la autenticación de usuarios
3. Desarrollo de la funcionalidad de procesamiento de PDF y URL
4. Integración con la API de OpenAI
5. Creación de la interfaz web interactiva
6. Pruebas y depuración
7. Documentación

## Utilidad
Este chatbot puede ser útil en varios escenarios:
- Análisis rápido de documentos PDF
- Extracción de información clave de páginas web
- Asistente virtual para responder preguntas sobre documentos específicos
- Herramienta educativa para procesar y entender contenido de diversas fuentes

## Futuras Mejoras
- Implementar procesamiento de lenguaje natural más avanzado
- Añadir soporte para más tipos de archivos
- Mejorar la interfaz de usuario
- Implementar un sistema de caché para mejorar el rendimiento

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)

