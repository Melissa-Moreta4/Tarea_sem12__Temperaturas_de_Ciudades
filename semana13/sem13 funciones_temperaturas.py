#Tarea funciones

#def suma (a,b):
    #return a + b
#resultado
#resultado = suma (9,13)
#print("la suma es ", resultado)

############################ TAREA SEMANA 13 sobre FUNCIONES #############################
"""Desarrollar una funcion que calcule la temperatura promedio de una ciudad durante
un periodo de tiempo. Se utilizará la matriz anterior del código para que la
función pueda recibir estos datos como parámetros y a su vez, calcular la temperatura
promedio de cada ciudad"""

#Código anterior de "Registro de Temperaturas" Consta las temperaturas de las ciudades
#en un tiempo de 4semanas.
temperaturas = [
    [   # Ciudad "Jambelí"
        [   # Semana 1
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 41},
            {"day": "Domingo", "temp": 45}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 39},
            {"day": "Miércoles", "temp": 43},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 49},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 40}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 41}
        ]
    ],
    [   # Ciudad "Nueva Loja"
        [   # Semana 1
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 35},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 45},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 42},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 47},
            {"day": "Domingo", "temp": 41}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 51},
            {"day": "Martes", "temp": 48},
            {"day": "Miércoles", "temp": 45},
            {"day": "Jueves", "temp": 50},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 36}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 39},
            {"day": "Domingo", "temp": 41}
        ]
    ],
    [   # Ciudad "Zamora"
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 49},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 43},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 51},
            {"day": "Martes", "temp": 43},
            {"day": "Miércoles", "temp": 45},
            {"day": "Jueves", "temp": 42},
            {"day": "Viernes", "temp": 39},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 48},
            {"day": "Martes", "temp": 50},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 33}
        ]
    ]
]

#calcular la temperatura promedio de cada ciudad
def promedio_temperaturas_ciudades(ciudades_temperaturas):
    las_temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        las_temperaturas_promedio[ciudad] = promedio

    return las_temperaturas_promedio

"""Se ejecuta una suma de las temperaturas de cada Ciudad y se divide para el
número (4) de temperaturas que consta cada una"""

# Listado de las ciudades con sus temperaturas
ciudades_temperaturas = {
    "Jambeli" : [36.57, 37.86, 32.71, 36.29],
    "Nueva Loja" : [35.86, 40.57, 44.29, 34.57],
    "Zamora" : [28.86, 39.43, 41.29, 36.57]
}

# llamar a la función y posterior calcular sus temperaturas promedio
calcular_temperaturas_promedio = promedio_temperaturas_ciudades(ciudades_temperaturas)

# Resultados en general
print("El promedio de temperaturas de cada una de las Ciudades:")
for ciudad, promedio in calcular_temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")