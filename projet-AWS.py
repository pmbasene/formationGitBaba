import cx_Oracle as cx
import mysql.connector as mysql
from mysql.connector import Error

# Penser à creer des classes 


#connection a la db oracle
##########
print("Connexion a la db oracle")
print('entrer le user database oracle:')
#user=input()  #hr/hr@10.0.21.233/xe
db= cx.connect('hr/hr@10.0.21.233/xe')
print("connected")

curOracle= db.cursor()
curOracle.execute('SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME from EMPLOYEES')
dataOracle= curOracle.fetchall()
for recOracle in dataOracle:
    print(recOracle)


#########################3
# db mysql-rds
###########
#print("Connexion db mysql-rds")
#print('entrer le host:')
#host=input()  #myrdspro.cgjslnsnwgqi.eu-west-3.rds.amazonaws.com

#print('entrer le nom (de la database rds:')
#database=input()  #dbprojet

##print('entrer le user database rds:')
#user=input()  #myrdspro

#print('entrer le mdp database rds:')
#password=input()  #Mamadou12&
try:
    dbmysql = mysql.connect(host="myrdspro.cgjslnsnwgqi.eu-west-3.rds.amazonaws.com",database='dbprojet', user='myrdspro',password='Mamadou12&')

    if dbmysql.is_connected():
       db_Info = dbmysql.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)
       print ("Your connected to rds-mysql")
except Error as e :
    print ("Error while connecting to MySQL", e)

curMysql = dbmysql.cursor()
# curMysql.execute("DROP TABLE contact")
curMysql.execute("CREATE TABLE IF NOT EXISTS contact (id INT,prenom VARCHAR(50),nom VARCHAR(50))")
sql = "INSERT INTO contact (id, prenom, nom) VALUES (%s, %s, %s)"
for i in range(100):
    curMysql.execute(sql, dataOracle[i])
dbmysql.commit()