from flask import Flask, request, jsonify
from flask_cors import CORS


from model.areas import (
    get_areas,
    get_area,
    create_area,
    get_area_by_name,
    update_area,
    delete_area,
)

from model.marcas import (
    get_marcas,
    get_marca,
    get_marca_by_name,
    update_marca,
    create_marca,
    delete_marca,
)

from model.empresa import (
    get_empresas,
    get_empresa,
    create_empresa,
    get_empresa_by_name,
    update_empresa,
    delete_empresa,
)

from model.tecnicos import (
    get_tecnicos,
    get_tecnico,
    create_tecnico,
    get_tecnico_by_name,
    update_tecnico,
    delete_tecnico,
)

from model.proveedores import (
    get_proveedores,
    get_proveedor,
    create_proveedor,
    get_proveedor_by_name,
    update_proveedor,
    delete_proveedor,
)

from model.historial import (
    get_historiales,
    get_historial,
    create_historial,
    update_historial,
    delete_historial,
)

from model.responsable import (
    get_responsables,
    get_responsable,
    create_responsable,
    get_responsable_by_name,
    update_responsable,
    delete_responsable,
)

from model.equipos import (
    get_equipos,
    get_equipo,
    create_equipo,
    get_equipo_by_name,
    update_equipo,
    delete_equipo,
)

app = Flask(__name__)
CORS(app)


@app.route('/areas', methods=['GET'])
def list_areas():
    retorno = get_areas()
    return jsonify(retorno)

@app.route('/areas/<int:area_id>', methods=['GET'])
def get_area_by_id(area_id):
    return jsonify(get_area(area_id))

@app.route('/areas/by_name/<area_name>', methods=['GET'])
def Get_area_by_name(area_name):
    return jsonify(get_area_by_name(area_name))

@app.route('/areas', methods=['POST'])
def Create_area():
    data = request.get_json()
    name = data['nombre']
    return jsonify(create_area(name))

@app.route('/areas/<int:area_id>', methods=['PUT'])
def Update_area(area_id):
    data = request.get_json()
    name = data['nombre']
    return jsonify(update_area(name, area_id))

@app.route('/areas/<int:area_id>', methods=['DELETE'])
def Delete_area(area_id):
    return jsonify(delete_area(area_id))

#

@app.route('/marcas', methods=['GET'])
def list_marcas():
    retorno = get_marcas()
    return jsonify(retorno)

@app.route('/marcas/<int:area_id>', methods=['GET'])
def get_marca_by_id(marca_id):
    return jsonify(get_marca(marca_id))

@app.route('/marcas/by_name/<marca_name>', methods=['GET'])
def Get_marca_by_name(marca_name):
    return jsonify(get_marca_by_name(marca_name))

@app.route('/marcas', methods=['POST'])
def create_marca():
    data = request.get_json()
    name = data['nombre']
    pais = data['pais']
    return jsonify(create_marca(name, pais))

@app.route('/marcas/<int:marca_id>', methods=['PUT'])
def Update_marca(marca_id):
    data = request.get_json()
    name = data['nombre']
    pais = data['pais']
    return jsonify(update_marca(name, pais, marca_id))   

@app.route('/marcas/<int:marca_id>', methods=['DELETE'])
def Delete_marca(marca_id):
    return jsonify(delete_marca(marca_id))

#2

@app.route('/tecnicos', methods=['GET'])
def list_tecnicos():
    retorno = get_tecnicos()
    return jsonify(retorno)

@app.route('/tecnicos/<int:tecnico_id>', methods=['GET'])
def get_tecnico_by_id(tecnico_id):
    return jsonify(get_tecnico(tecnico_id))

@app.route('/tecnicos/by_name/<tecnico_name>', methods=['GET'])
def Get_tecnico_by_name(tecnico_name):
    return jsonify(get_tecnico_by_name(tecnico_name))

@app.route('/tecnicos', methods=['POST'])
def Create_tecnico():
    data = request.get_json()
    name = data['nombre']
    company = data['empresa']
    return jsonify(create_tecnico(name, company))

@app.route('/tecnicos/<int:tecnico_id>', methods=['PUT'])
def Update_tecnico(tecnico_id):
    data = request.get_json()
    name = data['nombre']
    company = data['empresa']
    return jsonify(update_tecnico(name, company, tecnico_id))   

@app.route('/tecnicos/<int:tecnico_id>', methods=['DELETE'])
def Delete_tecnico(tecnico_id):
    return jsonify(delete_tecnico(tecnico_id))


#3


@app.route('/proveedores', methods=['GET'])
def list_proveedores():
    retorno = get_proveedores()
    return jsonify(retorno)

@app.route('/proveedores/<int:proveedor_id>', methods=['GET'])
def get_proveedor_by_id(proveedor_id):
    return jsonify(get_proveedor(proveedor_id))

@app.route('/proveedores/by_name/<proveedor_name>', methods=['GET'])
def Get_proveedor_by_name(proveedor_name):
    return jsonify(get_proveedor_by_name(proveedor_name))

@app.route('/proveedores', methods=['POST'])
def Create_proveedor():
    data = request.get_json()
    name = data['nombre']
    pais = data['paisl']
    return jsonify(create_proveedor(name, pais))

@app.route('/proveedores/<int:proveedor_id>', methods=['PUT'])
def Update_proveedor(proveedor_id):
    data = request.get_json()
    name = data['nombre']
    pais = data['paisl']
    return jsonify(update_proveedor(name, pais, proveedor_id))   

@app.route('/proveedores/<int:proveedor_id>', methods=['DELETE'])
def Delete_proveedor(proveedor_id):
    return jsonify(delete_proveedor(proveedor_id))

#4

@app.route('/responsable', methods=['GET'])
def list_responsables():
    retorno = get_responsables()
    return jsonify(retorno)

@app.route('/responsable/<int:responsable_id>', methods=['GET'])
def get_responsable_by_id(responsable_id):
    return jsonify(get_responsable(responsable_id))

@app.route('/responsable/by_name/<responsable_name>', methods=['GET'])
def Get_responsable_by_name(responsable_name):
    return jsonify(get_responsable_by_name(responsable_name))

@app.route('/responsable', methods=['POST'])
def Create_responsable():
    data = request.get_json()
    name = data['nombre']
    descripcion = data['descripcion']
    return jsonify(create_responsable(name, descripcion))

@app.route('/responsable/<int:responsable_id>', methods=['PUT'])
def Update_responsable(responsable_id):
    data = request.get_json()
    name = data['nombre']
    descripcion = data['descripcion']
    return jsonify(update_responsable(name, descripcion, responsable_id))   

@app.route('/responsable/<int:responsable_id>', methods=['DELETE'])
def Delete_responsable(responsable_id):
    return jsonify(delete_responsable(responsable_id))

#5

@app.route('/historial', methods=['GET'])
def list_historialess():
    retorno = get_historiales()
    return jsonify(retorno)

@app.route('/historial/<int:historial_id>', methods=['GET'])
def get_historial_by_id(historial_id):
    return jsonify(get_historial(historial_id))

@app.route('/historial', methods=['POST'])
def Create_historial():
    data = request.get_json()
    fecha = data['fecha']
    descripcion = data['descripcion']
    revision = data['revision'] 
    mantenimiento = data['mantenimiento'] 
    control = data['control']
    tecnico = data['tecnico'] 
    return jsonify(create_historial(fecha, descripcion,revision,mantenimiento,control,tecnico))

@app.route('/historial/<int:historial_id>', methods=['PUT'])
def Update_historial(historial_id):
    data = request.get_json()
    fecha = data['fecha']
    descripcion = data['descripcion']
    revision = data['revision'] 
    mantenimiento = data['mantenimiento'] 
    control = data['control']
    tecnico = data['tecnico'] 
    return jsonify(update_historial(fecha, descripcion,revision,mantenimiento,control,tecnico,historial_id))

@app.route('/historial/<int:historial_id>', methods=['DELETE'])
def Delete_historial(historial_id):
    return jsonify(delete_historial(historial_id))

#



@app.route('/empresa', methods=['GET'])
def list_empresas():
    retorno = get_empresas()
    return jsonify(retorno)

@app.route('/empresa/<int:empresa_id>', methods=['GET'])
def get_empresa_by_id(empresa_id):
    return jsonify(get_empresa(empresa_id))

@app.route('/empresa/by_name/<empresa_name>', methods=['GET'])
def Get_empresa_by_name(empresa_name):
    return jsonify(get_empresa_by_name(empresa_name))

@app.route('/empresa', methods=['POST'])
def Create_empresa():
    data = request.get_json()
    name = data['nombre']
    return jsonify(create_empresa(name))

@app.route('/empresa/<int:empresa_id>', methods=['PUT'])
def Update_empresa(empresa_id):
    data = request.get_json()
    name = data['nombre']
    return jsonify(update_empresa(name, empresa_id))

@app.route('/empresa/<int:empresa_id>', methods=['DELETE'])
def Delete_empresa(empresa_id):
    return jsonify(delete_empresa(empresa_id))

@app.route('/equipos', methods=['GET'])
def list_equipos():
    retorno = get_equipos()
    return jsonify(retorno)

@app.route('/equipos/<int:equipo_id>', methods=['GET'])
def get_equipo_by_id(equipo_id):
    return jsonify(get_equipo(equipo_id))

@app.route('/equipos/by_name/<equipo_name>', methods=['GET'])
def Get_equipo_by_name(equipo_name):
    return jsonify(get_equipo_by_name(equipo_name))

@app.route('/equipos', methods=['POST'])
def Create_equipo():
    data = request.get_json()
    name = data['nombre']
    descripcion = data['descripcion']
    facturacion = data['facturacion'] 
    invima = data['invima'] 
    riesgo = data['riesgo']
    historial = data['historial'] 
    proveedores = data['proveedores'] 
    marcas = data['marcas'] 
    areas = data['areas'] 
    responsables = data['responsables']
    return jsonify(create_equipo(name, descripcion, facturacion, invima, riesgo, historial, proveedores, marcas, areas, responsables))

@app.route('/equipos/<int:equipo_id>', methods=['PUT'])
def Update_equipo(equipo_id):
    data = request.get_json()
    name = data['nombre']
    descripcion = data['descripcion']
    facturacion = data['facturacion'] 
    invima = data['invima'] 
    riesgo = data['riesgo']
    historial = data['historial'] 
    proveedores = data['proveedores'] 
    marcas = data['marcas'] 
    areas = data['areas'] 
    responsables = data['responsables']
    return jsonify(update_equipo(name, descripcion, facturacion, invima, riesgo, historial, proveedores, marcas, areas, responsables, equipo_id))

@app.route('/equipos/<int:equipo_id>', methods=['DELETE'])
def Delete_equipo(equipo_id):
    return jsonify(delete_equipo(equipo_id))