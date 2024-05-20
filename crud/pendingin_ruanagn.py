from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for pendingin ruangan
pendingin_ruangan = [
    {"id": 1, "name": "AC1", "location": "Room 101", "status": "active"},
    {"id": 2, "name": "AC2", "location": "Room 102", "status": "inactive"},
]

# Helper function to find a pendingin ruangan by ID
def find_pendingin_ruangan_by_id(id):
    return next((item for item in pendingin_ruangan if item["id"] == id), None)

@app.route('/apiv1/pendingin-ruang', methods=['GET'])
def get_pendingin_ruangan():
    return jsonify(pendingin_ruangan)

@app.route('/apiv1/pendingin-ruang', methods=['POST'])
def add_pendingin_ruangan():
    new_data = request.json
    new_data['id'] = len(pendingin_ruangan) + 1
    pendingin_ruangan.append(new_data)
    return jsonify(new_data), 201

@app.route('/apiv1/pendingin-ruang/<int:id>', methods=['GET'])
def get_pendingin_ruangan_detail(id):
    data = find_pendingin_ruangan_by_id(id)
    if data:
        return jsonify(data)
    return jsonify({'message': 'Data not found'}), 404

@app.route('/apiv1/pendingin-ruang/<int:id>', methods=['DELETE'])
def delete_pendingin_ruangan(id):
    data = find_pendingin_ruangan_by_id(id)
    if data:
        pendingin_ruangan.remove(data)
        return jsonify({'message': 'Data deleted successfully'})
    return jsonify({'message': 'Data not found'}), 404

@app.route('/apiv1/pendingin-ruang/<int:id>', methods=['PUT'])
def update_pendingin_ruangan(id):
    data = find_pendingin_ruangan_by_id(id)
    if data:
        update_data = request.json
        data.update(update_data)
        return jsonify(data)
    return jsonify({'message': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
