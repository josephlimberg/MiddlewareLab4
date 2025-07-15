import mysql.connector

try:
    conn = mysql.connector.connect(
        #host="xxx.xxx.xxx.xxx",  # IP de la compu B
        host="000.000.000.000",
        user="admin",
        password="admin",
        database="saludosdb"
    )
    print(" Conexión exitosa a la base de datos")
    conn.close()
except Exception as e:
    print(" Error de conexión:", e)
