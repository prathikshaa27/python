import mysql.connector

products_database =mysql.connector.connect(
    host="Prathi",
    user="root",
    password="prathi27",
    database="products"
)
if products_database is connected()