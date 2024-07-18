from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
db = cliente['basedatosMDB']

pipeline = [
    {
        '$group': {
            '_id': {
                'fecha': { '$dateToString': { 'format': '%Y-%m-%d', 'date': { '$toDate': '$created_at' } } },
                'company_id': '$company_id'
            },
            'total_amount': { '$sum': '$amount' }
        }
    },
    {
        '$lookup': {
            'from': 'companies',
            'localField': '_id.company_id',
            'foreignField': 'company_id',
            'as': 'company_info'
        }
    },
    {
        '$unwind': '$company_info'
    },
    {
        '$project': {
            'fecha': '$_id.fecha',
            'company_id': '$_id.company_id',
            'company_name': '$company_info.company_name',
            'total_amount': 1
        }
    },
    {
        '$sort': {
            'fecha': 1,
            'company_id': 1
        }
    }
]

resultados = db.charges.aggregate(pipeline)

for resultado in resultados:
    print(resultado)
