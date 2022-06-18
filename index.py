from flask import Flask, jsonify, request
import random

application = Flask(__name__)
# Configuracion
application.secret_key = '123456'


@application.route("/", methods=['GET'])
def hello_world():
  return jsonify({'mensaje': 'te comunicas con el API python.'})

@application.route("/cmp", methods=['POST'])
def validar_cmp():
  if request.method == "POST":
    success = False
    mensaje = 'No se encontro usuario registrado con el cmp: {0}'
    
    cmp = request.json['cmp']
    
    # simulamos validacion de cmp
    num = random.random()
    if num >= 0.5:
      success = True
      mensaje = "Se encontro usuario registrado con el cmp: {0}"
    
    return jsonify({'success': success, 'mensaje': mensaje.format(cmp)})




def endpoint_no_encontrado(error):
  return jsonify({'error': 'error', 'mensaje': 'el endpoint no existe.'})

application.register_error_handler(404, endpoint_no_encontrado)
if __name__ == '__main__':
  application.run(debug=True)