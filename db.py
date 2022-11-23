from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.assignment
db.Data.insert_one({'ID':407, 'Email':'f@f.com', 'Name':'George', 'Department':'Automobile', 'Submission':1, 'Grade':'B'})
data = db.Data.find({})

for i in data:
    print(i)