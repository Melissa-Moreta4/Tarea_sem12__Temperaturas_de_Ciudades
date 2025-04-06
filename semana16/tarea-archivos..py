# Crear un nuevo archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')

"""Se utiliza los métodos de escritura y lestura"""

# Método write(): para escribir una línea a la vez
my_notes.write("Línea 1: Primera prueba, bienvenido a mi archivo.\n")
my_notes.write("Línea 2: Estamos Trabajando con archivos en Python.\n")

# Método writelines(): para escribir una lista de líneas
lineas = ["Línea 3: Prueba de otro ejemplo de lineas.\n", "Línea 4: Terminando la Prueba del uso de lista de líneas.\n"]
my_notes.writelines(lineas)

my_notes.close()

# Abre el archivo my_notes.txt.
my_notes = open('my_notes.txt', 'r')

"""Lee el contenido del archivo línea por línea utilizando el método adecuado"""

# Método 1. read()
print('Método 1: read()')
print('*******************')
print(my_notes.read())
my_notes.close()

# Método 2. readlines()
my_notes = open('my_notes.txt', 'r')
print('Método 2: readlines()')
print('*******************')
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()