from flask import Flask, jsonify

app = Flask(__name__)
# Configuracion
app.secret_key = '123456'


@app.route("/", methods=['GET'])
def hello_world():
    return jsonify({'mensaje': 'te comunicas con el API python.'})

def endpoint_no_encontrado(error):
  return jsonify({'error': 'error', 'mensaje': 'el endpoint no existe.'})

if __name__ == '__main__':
  app.register_error_handler(404, endpoint_no_encontrado)
  app.run()