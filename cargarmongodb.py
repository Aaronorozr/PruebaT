import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
import re

motor = create_engine('sqlite:///basedatos.db')

datos_limpiados = pd.read_sql('SELECT * FROM datos_limpiados', motor)

datos_limpiados['created_at'] = pd.to_datetime(datos_limpiados['created_at'], errors='coerce')
datos_limpiados['updated_at'] = pd.to_datetime(datos_limpiados['updated_at'], errors='coerce')

datos_limpiados['company_name'] = datos_limpiados['company_name'].astype(str)


def limpiar_nombre_empresa(nombre):
    if re.match(r'^[\W_]+$', nombre):
        return None
    if '0xFFFF' in nombre:
        return None
    return nombre

datos_limpiados['company_name'] = datos_limpiados['company_name'].apply(limpiar_nombre_empresa)

def corregir_nombres(df):
    company_dict = df.dropna(subset=['company_id']).drop_duplicates('company_name').set_index('company_name')['company_id'].to_dict()
    company_dict['MiPasajefy'] = 'cbf1c8b09cd5b549416d49d220a40cbd317f952e'
    df['company_id'] = df.apply(lambda x: company_dict.get(x['company_name'], x['company_id']), axis=1)
    reverse_company_dict = df.dropna(subset=['company_name']).drop_duplicates('company_id').set_index('company_id')['company_name'].to_dict()
    df['company_name'] = df.apply(lambda x: reverse_company_dict.get(x['company_id'], x['company_name']), axis=1)
    return df
datos_limpiados = corregir_nombres(datos_limpiados)

def corregir_montos(amount):
    try:
        amount = float(amount)
        if amount >= 1e9 or amount < 0:  
            amount = 0.0
    except (ValueError, TypeError):
        amount = 0.0 
    return amount

datos_limpiados['amount'] = datos_limpiados['amount'].apply(corregir_montos)

cliente = MongoClient('localhost', 27017)
db = cliente['basedatosMDB'] 

companies = db['companies']
charges = db['charges']

companies.delete_many({})
charges.delete_many({})

companies_data = datos_limpiados[['company_id', 'company_name']].drop_duplicates().dropna(subset=['company_id', 'company_name']).copy()
datos_limpiados['created_at'] = datos_limpiados['created_at'].apply(lambda x: x.isoformat() if pd.notnull(x) else None)
datos_limpiados['updated_at'] = datos_limpiados['updated_at'].apply(lambda x: x.isoformat() if pd.notnull(x) else None)

companies.insert_many(companies_data.to_dict('records'))
charges.insert_many(datos_limpiados.to_dict('records'))

print("Datos cargados exitosamente en MongoDB.")
