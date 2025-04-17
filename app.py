from flask import Flask
from datetime import datetime
import requests
app = Flask(__name__)

@app.route('/')
def home():
    # Obtener la fecha y hora actual
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %H:%M:%S")

    # URL del archivo txt
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'
    
    # Obtener el contenido del archivo
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si hay error
        contenido = respuesta.text.replace('\n', '<br>')  # Para que se vea bien en HTML
    except Exception as e:
        contenido = f'<i>Error al obtener el archivo: {e}</i>'

    # Devolver el contenido como parte del HTML
    return f'''
    <h1>¡Hola, mundo!</h1>
    <p><b>Fecha actual:</b> {fecha_formateada}</p>
    <h2>Contenido del archivo:</h2>
    <div style="white-space: pre-wrap; font-family: monospace;">{contenido}</div>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
