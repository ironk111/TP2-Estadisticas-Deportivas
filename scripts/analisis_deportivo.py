
import matplotlib.pyplot as plt

partidos = []

try:
    with open("datos/partidos.csv", "r", encoding="utf-8") as archivo:
        encabezado = archivo.readline()
        for linea in archivo:
            datos = linea.strip().split(",")

            partido = {
                "fecha": datos[0],
                "local": datos[1],
                "visitante": datos[2],
                "goles_local": int(datos[3]),
                "goles_visitante": int(datos[4])
            }

            partidos.append(partido)
except FileNotFoundError:
    print("No se encontró el archivo.")
except Exception as e:
    print("Ocurrió un error:")
    print(e)
else:
    total_goles = 0

    for partido in partidos:
        total_goles += partido["goles_local"]
        total_goles += partido["goles_visitante"]

    promedio = total_goles / len(partidos)

    print("Cantidad de partidos:", len(partidos))
    print("Promedio de goles:", round(promedio, 2))


victorias = {}

for partido in partidos:

    if partido["goles_local"] > partido["goles_visitante"]:

        ganador = partido["local"]

    elif partido["goles_visitante"] > partido["goles_local"]:

        ganador = partido["visitante"]

    else:
        continue

    if ganador in victorias:
        victorias[ganador] += 1
    else:
        victorias[ganador] = 1

equipos = list(victorias.keys())
cantidad = list(victorias.values())

plt.bar(equipos, cantidad)

plt.title("Partidos ganados por equipo")
plt.xlabel("Equipos")
plt.ylabel("Victorias")

plt.savefig("resultados/grafico_victorias.png")

print("Gráfico generado correctamente.")
