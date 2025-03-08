# Crear una matriz 3D para registro de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
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

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad Jambelí", "Ciudad Nueva Loja", "Ciudad Zamora"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
