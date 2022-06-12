from flask import Flask, jsonify

application = Flask(__name__)
# Configuracion
application.secret_key = '123456'


@application.route("/", methods=['GET'])
def hello_world():
    return jsonify({'mensaje': 'te comunicas con el API python.'})

def endpoint_no_encontrado(error):
  return jsonify({'error': 'error', 'mensaje': 'el endpoint no existe.'})

application.register_error_handler(404, endpoint_no_encontrado)
if __name__ == '__main__':
  application.run()