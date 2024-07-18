# Prueba Tecnica 

Este proyecto incluye la creación de vistas en una base de datos MongoDB y la implementación de una clase en Python para calcular el número faltante de un conjunto de los primeros 100 números naturales.

## Requisitos Previos

1. **Instalar MongoDB**
   - Descarga e instala MongoDB desde la [página oficial de MongoDB](https://www.mongodb.com/try/download/community).
   - Sigue las instrucciones de instalación según tu sistema operativo.

2. **Instalar Python**
   - Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde la [página oficial de Python](https://www.python.org/downloads/).

## Configuración del Entorno

1. **Clonar el repositorio**
   - Clona este repositorio en tu máquina local usando:
     ```bash
     git clone <URL_DEL_REPOSITORIO>
     cd <NOMBRE_DEL_REPOSITORIO>
     ```

2. **Crear un entorno virtual**
   - Crea un nuevo entorno virtual en el directorio del proyecto:
     ```bash
     python -m venv venv
     ```

3. **Activar el entorno virtual**
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar las dependencias**
   - Instala las dependencias listadas en el archivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

## Uso del Proyecto

### Exportar la Base de Datos MongoDB

Para exportar la base de datos MongoDB, usa MongoDB Compass o sigue los comandos proporcionados anteriormente.

### Ejecutar la Clase en Python

1. **Ejecutar el script para extraer un número**
   - Puedes ejecutar el script `conjunto.py` para extraer un número de un conjunto de los primeros 100 números naturales. Por ejemplo:
     ```bash
     python conjunto.py 42
     ```

### Cargar los Datos en MongoDB

1. **Ejecutar el script de carga de datos**
   - Ejecuta el script que carga y transforma los datos en MongoDB:
     ```bash
     python cargar_datos.py
     ```

2. **Crear la vista en MongoDB**
   - Ejecuta el script para crear la vista en MongoDB:
     ```bash
     python crear_vista.py
     ```

## Contenido del Repositorio

- `conjunto.py`: Clase en Python que representa un conjunto de los primeros 100 números naturales y permite extraer un número.
- `cargar_datos.py`: Script para cargar y transformar datos en MongoDB.
- `crear_vista.py`: Script para crear una vista en MongoDB.
- `requirements.txt`: Lista de dependencias necesarias para el proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, haz un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más información, consulta el archivo `LICENSE`.
