from flask import Flask, request, jsonify

app = Flask(__name__)

pendingin_ruangan = [
    {"id": 1, "nama": "AC Samsung", "merk": "Samsung", "tipe": "Split", "kapasitas": 1, "harga": 5000000},
    {"id": 2, "nama": "AC LG", "merk": "LG", "tipe": "Window", "kapasitas": 1.5, "harga": 6000000},
]

@app.route('/api/v1/pendingin_ruangan', methods=['GET'])
def get_pendingin_ruangan():
    return jsonify(pendingin_ruangan)

@app.route('/api/v1/pendingin_ruangan/<int:id>', methods=['GET'])
def get_pendingin_ruangan_by_id(id):
    pendingin = next((p for p in pendingin_ruangan if p["id"] == id), None)
    if pendingin is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(pendingin)

@app.route('/api/v1/pendingin_ruangan', methods=['POST'])
def create_pendingin_ruangan():
    new_pendingin = request.get_json()
    pendingin_ruangan.append(new_pendingin)
    return jsonify(new_pendingin), 201

if __name__ == '__main__':
    app.run(debug=True)
