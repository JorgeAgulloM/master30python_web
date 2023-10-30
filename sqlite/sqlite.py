### sqlite ###

import sqlite3 as sql

db = 'sqlite\pruebas_sqlite.db'

# Conexión
conexion = sql.connect(database=db)

cursor = conexion.cursor()

# Crear Tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        titulo VARCHAR(255), 
        description TEXT, 
        precio DOUBLE(255)
    )
""")

# Guardar cambios
conexion.commit()

# Insertar registro
cursor.execute("INSERT INTO products VALUES (NULL, 'Primer producto', 'Descripción', '500.00')")
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
for product in products:
    print(product)

# primer objeto
cursor.execute("SELECT * FROM products")
product = cursor.fetchone()
print(product)

# Eliminar registros
delete = False
if delete:
    #conexion.execute("DELETE FROM products") # BORRA TODA LA TABLA
    conexion.execute("DELETE FROM products WHERE id = 5") # BORRA TODA LA TABLA
    conexion.commit()

# Insertar muchso registros
productos = [
    ("MacBook Pro", "Laptop potente con pantalla Retina de 13 pulgadas.", 1499.99),
    ("iPhone 13", "Teléfono inteligente con cámara avanzada y rendimiento rápido.", 999.99),
    ("Samsung Galaxy S22", "Teléfono Android de alta gama con pantalla AMOLED.", 1099.99),
    ("Sony 65-inch 4K TV", "Televisor con calidad de imagen impresionante.", 799.99),
    ("PlayStation 5", "Consola de juegos de última generación.", 499.99),
    ("Dyson V11 Vacuum", "Aspiradora sin cables con una potente succión.", 599.99),
    ("Instant Pot Duo", "Olla a presión eléctrica multifunción.", 89.99),
    ("Bose QuietComfort 45", "Auriculares con cancelación de ruido premium.", 349.99),
    ("Amazon Echo Dot", "Altavoz inteligente con asistente virtual Alexa.", 39.99),
    ("Nespresso Vertuo Plus", "Máquina de café con tecnología de cápsulas.", 149.99)
]

cursor.executemany("INSERT INTO products VALUES (NULL,?,?,?)", productos)
conexion.commit()
products = cursor.fetchall()

for product in products:
    print(product)
    print("")

# Update
cursor.execute("UPDATE products SET precio = 1000000.00 WHERE id = 12")
conexion.commit()
cursor.execute("SELECT * FROM products WHERE id = 12")
product = cursor.fetchall()
print(product)

# Desconexión
conexion.close()
