from sqlalchemy import create_engine
from sqlalchemy import MetaData,Table,Column, Integer, String

DB_URL = "mysql+mysqldb://root:1234@localhost:3306/employee"

engine = create_engine(DB_URL)
# conn = engine.connect()



try:
    cursor = engine.connect()
    query = 'select * from emp'
    result = cursor.execute(query)
    print(result)



except:
    print("Not successfully")