import pandas as pd
from sqlalchemy import create_engine, text, String, Float, DateTime


archivo_csv = 'data_prueba_tecnica.csv'
datos = pd.read_csv(archivo_csv)


motor = create_engine('sqlite:///basedatos.db')


consulta_crear_tabla = """
CREATE TABLE IF NOT EXISTS datos_limpiados (
    id VARCHAR(24) NOT NULL PRIMARY KEY,
    company_name VARCHAR(130) NULL,
    company_id VARCHAR(24) NOT NULL,
    amount DECIMAL(16,2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL
);
"""

with motor.connect() as conexion:
    conexion.execute(text(consulta_crear_tabla))


datos_transformados = datos.rename(columns={
    "id": "id",
    "name": "company_name",
    "company_id": "company_id",
    "amount": "amount",
    "status": "status",
    "created_at": "created_at",
    "paid_at": "updated_at"
})


datos_transformados['amount'] = datos_transformados['amount'].astype(float)


datos_transformados['created_at'] = pd.to_datetime(datos_transformados['created_at'], errors='coerce', format='%Y-%m-%d')
datos_transformados['updated_at'] = pd.to_datetime(datos_transformados['updated_at'], errors='coerce', format='%Y-%m-%d')

datos_transformados.to_sql('datos_limpiados', con=motor, if_exists='replace', index=False, dtype={
    'id': String(24),
    'company_name': String(130),
    'company_id': String(24),
    'amount': Float,
    'status': String(30),
    'created_at': DateTime,
    'updated_at': DateTime
})

print("Datos transformados y cargados en SQLite exitosamente.")
