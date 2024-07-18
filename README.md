# Prueba Tecnica 

Este repositorio incluye la transformacion de un archivo .csv a sqlite, la limpieza de los datos, la relacion de cargos con compañias, la creación de vistas y la implementación de una clase en Python para calcular el número faltante de un conjunto de los primeros 100 números naturales.
Dejo aquí la tabla que se me pide un un punto mas abajo.

![image](https://github.com/user-attachments/assets/ffc9d671-44ce-43a9-95a3-e1642f9b6358)


## Requisitos Previos

1. **Instalar MongoDB**
   - Descarga e instala MongoDB desde la [página oficial de MongoDB](https://www.mongodb.com/try/download/community).
   - Seguir las instrucciones de instalación según el sistema operativo (la prueba fue desarrollada en windows 10)

2. **Instalar Python**
   - Instalar Python  si aun no se ha instalado en el sistema. se puede descargar desde [página oficial de Python](https://www.python.org/downloads/).

## Configuración del Entorno

1. **Clonar el repositorio**
   - Clona el repositorio en la pc local usando:
     ```bash
     git clone https://github.com/Aaronorozr/PruebaT.git

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


4. **Instalar las dependencias**
   - Instala las dependencias listadas en el archivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
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
### Ejecutar la Clase en Python

1. **se puede ejecutar el script `cien.py` para extraer un número de un conjunto de los primeros 100 números naturales. Por ejemplo:
     ```bash
     python conjunto.py 42
     ```

## Uso del Proyecto y respuestas

# Sección 1: Procesamiento y transferencia de datos
Objetivo: Crear un proceso con las herramientas disponibles por el usuario
## 1.1 Carga de información
Decidí transportar los datos a SQLlite para poder tener un mayor control a la hora de pruebas rapidas con la herramienta DB BROUSER SQLlite, ya que posteiormente pasaria la base de datos a una mas robusta (MongoDB).
## 1.2, 1.3 y 1.4 Extracción, Transformación y Disperción.
Hice el procedimiento de extracción de SQLlite directamente a mongo db, limpiando los datos y transformandolos al esquema que se me propuso, tuve bastantes inconvenientes, los nombres de las compañias estaban incorrectos, a pesar de ser solo dos compañias me tuve que asegurar que en la tabla companies de mongodb solo aparecieran las dos, añadiendo logica al script de python, el amount tenia problemas a la hora de convertir los valores debido a numeros muy altos y valores con notacion cientifica, las fechas tenian valores incorrectos para timestamp, al final usé datatime,
me fue mas viable avanzar estos tres puntos a la vez que hacerlos uno por uno.

## 1.5 SQL
   Diseñé una vista para ver el monto total transaccionado por día para las diferentes compañías.

# Sección 2: Creación de una API
Creé una clase con metodos para calcular el numero faltante de un conjunto de los primeros 100 números, decidí usar archivos JSON para mantener la logica del API a no permitir extraer el mismo numero mas de una vez. 

## Contenido del Repositorio

- `conjunto.py`: Clase en Python que representa un conjunto de los primeros 100 números naturales y permite extraer un número.
- `cargar_datos.py`: Script para cargar y transformar datos en MongoDB.
- `crear_vista.py`: Script para crear una vista en MongoDB.
- `requirements.txt`: Lista de dependencias necesarias para el proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, haz un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más información, consulta el archivo `LICENSE`.
