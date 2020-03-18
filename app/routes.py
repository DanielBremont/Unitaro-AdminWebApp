from flask import render_template, request, jsonify, json, redirect
from app import app
import base64
from  .Api import facturas, db
from tinydb import Query

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ventas/registrar')
def ventas_registrar():
    return render_template('ventas/registrar.html')

@app.route('/ventas/newProduct')
def ventas_new_product():
    return render_template('ventas/newProduct.html')  

@app.route('/ventas/facturas')
def ventas_consultar():
    return render_template('ventas/facturas.html')

@app.route('/ventas/minifacturaview/<id>')
def minifacturaview(id):
    factura  =  facturas.get(id)
    return render_template('ventas/minifacturaview.html', data = factura)

@app.route('/api/save/<table>', methods=['POST'])
def save(table):
    object_id = facturas.Save(table, request.json)
    return {"result": 405, "table_name":table, "data": request.json, "id": object_id}

@app.route('/api/get/<table>', methods=['GET'])
def get(table):
    return jsonify(db.table(table).all())

@app.route('/api/factura',  methods=['POST'])
def salvar_factura():    
    facturas.SaveFactura(request.json)
    return jsonify(request.json)

@app.route('/api/facturas/list',  methods=['GET'])
def list_facturas():
    lf = [{
            "id" : 1,
            "link": "/ventas/minifacturaview/1"
        },
        {
            "id" : 2,
            "link": "/ventas/minifacturaview/2"
        },
        {
            "id" : 3,
            "link": "/ventas/minifacturaview/3"
        },
        {
            "id" : 4,
            "link": "/ventas/minifacturaview/4"
        }
    ]

    return jsonify({"facturas": lf})


@app.route('/ventas/verfactura')
def ventas_verfactura():    
    # print(request)
    # print(request.json)

    # nombre  = request.json['nombre']
    # descripcion = request.json['descripcion']
    data = base64.b64decode(request.args.get('data'))
    data = json.loads(data)

    return render_template('ventas/verfactura.html', data = data)

@app.route('/reportes/consultar_ventas')
def reportes_consultar_ventas():
    return render_template('reportes/consultar_ventas.html')

@app.route('/reportes/ventas_por_cobrar')
def reportes_cuentas_por_cobrar():
    return render_template('reportes/ventas_por_cobrar.html')

@app.route('/reportes/top_clientes')
def reportes_flujo_clientes():
    return render_template('reportes/top_clientes.html')

@app.route('/catalogo_productos/categorias')
def catalogo_productos_categorias():
    return render_template('catalogo_productos/categorias.html')

@app.route('/catalogo_productos/newCategoria')
def catalogo_productos_newCategoria() :
    return render_template('catalogo_productos/newCategoria.html')
    
@app.route('/catalogo_productos/productos')
def catalogo_productos_productos():
    return render_template('catalogo_productos/productos.html')

@app.route('/catalogo_productos/newProducto')
def catalogo_productos_newProductos() :
    return render_template('catalogo_productos/newProducto.html')

@app.route('/login')
def login():
    return render_template('cuenta/login.html')

@app.route('/register')
def register():
    return render_template('cuenta/register.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('cuenta/forgot-password.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/404')
def error404():
    return render_template('404.html')

## Components
@app.route('/c/rs_ventas_graph')
def c_rs_ventas_graph():
    return render_template('components/rs_ventas_graph.html')

@app.route('/c/rs_facturas_graph')
def c_rs_facturas_graph():
    return render_template('components/rs_facturas_graph.html')

@app.route('/c/rs_ventas_x_cobrar')
def c_rs_ventas_x_cobrar():
    return render_template('components/rs_ventas_x_cobrar.html')

@app.route('/c/rs_clientes_mes')
def c_rs_clientes_mes():
    return render_template('components/rs_clientes_mes.html')

@app.route('/c/taro_alert')
def c_taro_alert():
    return render_template('components/taro_alert.html')

@app.route('/c/metris')
def c_metris():
    return render_template('components/taro_indicadores.html')

@app.route('/activity_log')
def activity_log():
    return render_template('activity_log.html')

@app.route('/logout')
def logout():
    return redirect("/login", code=302)

@app.route('/api/saveCategoria', methods=['POST'])
def saveCategoria():
    # return jsonify({
    #     'nombre': 'mariano'
    # })

    nombre  = request.json['nombre']
    descripcion = request.json['descripcion']

    print(nombre, descripcion)
    print('Save to database using api.')

    return jsonify(request.json)

@app.route('/api/Producto', methods=['POST'])
def saveProducto():     
    categoria  = request.json['categoria']
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']

    print(categoria, precio, nombre, descripcion)
    print('Save to database using api.')

    return jsonify(request.json)