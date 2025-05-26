from flask import Flask, jsonify, request
from scanner import scan_network
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde el frontend

@app.route('/scan', methods=['GET'])
def scan():
    base_ip = request.args.get('base_ip', '192.168.1')
    hosts = scan_network(base_ip)
    return jsonify(hosts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
