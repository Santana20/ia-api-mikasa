from flask import Flask, jsonify
from config import config

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return jsonify({'mensaje': 'te comunicas con el API python.'})

def endpoint_no_encontrado(error):
  return jsonify({'error': 'error', 'mensaje': 'el endpoint no existe.'})

if __name__ == '__main__':
  app.config.from_object(config['dev'])
  app.register_error_handler(404, endpoint_no_encontrado)
  app.run()