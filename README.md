# Prueba Tecnica 

Este repositorio incluye la transformacion de un archivo .csv a sqlite, la limpieza de los datos, la relacion de cargos con compañias, la creación de vistas y la implementación de una clase en Python para calcular el número faltante de un conjunto de los primeros 100 números naturales.

## Requisitos Previos

1. **Instalar MongoDB**
   - Descarga e instala MongoDB desde la [página oficial de MongoDB](https://www.mongodb.com/try/download/community).
   - Seguir las instrucciones de instalación según el sistema operativo (la prueba fue desarrollada en windows 10)

2. **Instalar Python**
   - Instalar Python  si aun no se ha instalado en el sistema. se puede descargar desde [página oficial de Python](https://www.python.org/downloads/).

## Configuración del Entorno

1. **Clonar el repositorio**
   - Clona este repositorio en tu máquina local usando:
     ```bash
     git clone [<URL_DEL_REPOSITORIO>](https://github.com/Aaronorozr/PruebaT.git)

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


### Ejecutar la Clase en Python

1. **se puede ejecutar el script `cien.py` para extraer un número de un conjunto de los primeros 100 números naturales. Por ejemplo:
     ```bash
     python conjunto.py 42
     ```
### transformar el archivo data_prueba_tecnica.csv a SQLlite
1. - Ejecuta el script que transforma a SQLlite:
     ```bash
     python importador.py
     ```

### Cargar los Datos en MongoDB

1. **Ejecutar el script que hace toda la limpieza de los datos**
   - Este Script lo creé a medida, basado en la consola de errores de visual studio y mongodb compass a demás se creo la tabla companies donde solo se muestran las dos compañias existentes:
     ```bash
     python cargarmongodb.py
     ```

2. **Crear la vista en MongoDB**
   - una vez limpiado y cargado a  MongoDB:
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
