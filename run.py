from flask import Flask
from flask import jsonify, request
from productoDao import sql_select_productos, sql_select_producto, sql_insert_producto, sql_edit_producto, sql_delete_producto


app = Flask(__name__)

@app.route('/api/v1/productos/', methods=['GET'])
def get_productos():
    response = sql_select_productos()
    return jsonify(response)

@app.route('/api/v1/producto/<id>',  methods=['GET'])
def get_producto(id):
    response = sql_select_producto(id)
    return jsonify(response)

@app.route('/api/v1/producto/', methods=['POST'])
def create_producto():
   request_data = request.get_json()
   print(request_data)
   id = request_data['id']
   nombre = request_data['nombre']
   precio = request_data['precio']
   existencia = request_data['existencia']
   sql_insert_producto(id, nombre, precio, existencia)
   return jsonify({'message':'Producto Creado.'})

@app.route('/api/v1/producto/', methods=['PUT'])
def update_producto():
    request_data = request.get_json()
    print(request_data)
    id = request_data['id']
    nombre = request_data['nombre']
    sql_edit_producto(id, nombre)
    return jsonify({'message':'Producto Actualizado.'})

@app.route('/api/v1/producto/', methods=['DELETE'])
def delete_producto():
    request_data = request.get_json()
    print(request_data)
    id = request_data['id']   
    sql_delete_producto(id)
    return jsonify({'message':'Producto Eliminado.'})

if __name__ == '__main__':
    app.run(debug=True, port=9000, host='0.0.0.0')