import pyodbc 
try:
    cnx = pyodbc.connect("""DRIVER={ODBC Driver 17 for SQL Server};SERVER=sql04.ok.ubc.ca;
                        DATABASE=workson;UID=rlawrenc;PWD=todo""")
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM emp WHERE salary < ?", [50000]) 
    for row in cursor:
        print(row[0],row[1], row.salary)        
except pyodbc.Error as err:  
    print(err)
finally:
    cnx.close()
