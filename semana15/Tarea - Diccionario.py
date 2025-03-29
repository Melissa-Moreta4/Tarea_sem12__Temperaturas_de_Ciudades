#Tarea Sem 15 "Trabajando con Diccionarios"
"""Crea un diccionario llamado informacion_personal que contenga información ficticia
sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
Modifica valores, accede nuevos datos y elimina un elemento en el diccionario."""

print("\n*** DICCIONARIO ***")
informacion_personal={
    "Nombre": "Iván",
    "Edad": 33,
    "Ciudad": "Palora"
}
print("Diccionario de datos:", informacion_personal)

#Modificar Ciudad
informacion_personal["Ciudad"]="Buena Fe"
print("Luego de cambiar 'Ciudad':", informacion_personal)

#Insertar Profesión de la persona
informacion_personal["Profesión"]= "Ing en Arquitectura"
print("Después de insertar 'Profesión':", informacion_personal)

#Eliminar un elemento
del informacion_personal["Edad"]
print("Luego de eliminar 'Edad':", informacion_personal)

#Verificar Teléfono de la persona
if "Teléfono" not in informacion_personal:
    informacion_personal["Teléfono"]= 989898432
print("A continuación, de agregar 'Teléfono':", informacion_personal)