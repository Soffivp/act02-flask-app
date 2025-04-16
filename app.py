from flask import Flask
from datetime import datetime
import requests



app = Flask(__name__)

@app.route('/')
def home():
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")
    return f'¡Hola, a todos. Bienvenidos! <b>{fecha_formateada}</b>
    resp = requests.get('https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt')

resp.encoding
'ISO-8859-1'
resp.text
'<!doctype html><html itemscope="" itemtype="h...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)