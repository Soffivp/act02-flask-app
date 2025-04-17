from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %H:%M:%S")

    # Descargar el contenido
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response = requests.get(url)

    if response.status_code == 200:
        contenido = response.text.splitlines()
        encabezados = contenido[0].split(",")  # Usamos "," como separador
        datos = contenido[1:]

        ids = ("3", "4", "5", "7")
        datos_filtrados = [
            fila.split(",") for fila in datos
            if fila.split(",")[0].startswith(ids)
        ]

        # Crear tabla HTML
        tabla_html = "<table border='1'>\n"
        tabla_html += "  <tr>" + "".join(f"<th>{col}</th>" for col in encabezados) + "</tr>\n"

        for fila in datos_filtrados:
            tabla_html += "  <tr>" + "".join(f"<td>{celda}</td>" for celda in fila) + "</tr>\n"

        tabla_html += "</table>"

        # Combinar el saludo y la tabla
        return f'¡Hola, mundo! <b>{fecha_formateada}</b><br><br>{tabla_html}'
    else:
        return f"Error al obtener los datos: {response.status_code}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
