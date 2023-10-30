import mysql.connector as sql

# Connexión
database = sql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python" #Solo añadir si la BBDD ya está creada       
)

# Crear cursor
cursor = database.cursor(buffered=True) #Para ejecutar muchas consultas, no te fies mucho de esto.

# Crear BBDD
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# Consultar si la BBDD se ha creado
#cursor.execute("SHOW DATABASES")

# Observar la BBDD que tenermos registradas en el cursor
#for db in cursor:
#    print(db)
    
# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )               
""")

# Observar tablas
#cursor.execute("SHOW TABLES")

# Imprimir
#for table in cursor:
#    print(table)

# nuevo vehiculo
#cursor.execute("INSERT INTO vehiculos VALUES(NULL, 'ford', 'focus', '18000')")
#database.commit()

# Insertar varios registros a la vez
coches = [
    ('seat', 'ibiza', 16000),
    ('renault', 'clio', 14000),
    ('citroen', 'saxo', 13000),
    ('mercedes', 'clase c', 35000)
]

# Insertar
#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

# update DB
database.commit()

# Select de datos
cursor.execute("SELECT * FROM vehiculos WHERE precio > '14000'")
# Obtenere datos de cursor
result = cursor.fetchall()

print('---MIS COCHES > DE 14000')
for coche in result:
    print(coche)
print('')
    
# Select de datos
cursor.execute("SELECT modelo FROM vehiculos WHERE precio > '14000' AND marca = 'mercedes'")
# Obtenere datos de cursor
result = cursor.fetchall()

print('---MIS COCHES modelo > DE 14000 AND mercedes')
for coche in result:
    print(coche)
print('')

# Eliminar
cursor.execute("DELETE FROM vehiculos WHERE marca = 'renault'")
database.commit()

# Revisar registros eliminados
print(cursor.rowcount, "Borrados!!")
print('')

# Obtener
cursor.execute("SELECT * FROM vehiculos")
print(cursor.fetchall())
print('')

# Actualziar
cursor.execute("UPDATE vehiculos SET modelo='leon' WHERE marca='seat' AND modelo='ibiza'")
database.commit()

print(cursor.rowcount, 'Actualizados!!')
print('')

