import tinydb

db = tinydb.TinyDB('/home/danieldev/Documents/wc/app/Api/db.json')

def Save(table_name, row):
  table  = db.table(table_name)
  return table.insert(row)

def SaveFactura(factura):
  dbproductos = db.table('productos')
  dbproductos.insert(factura)

def get(id):
  print(f'get factura {id}')
  return {"nombre_empresa" : "Daniel Victoriano", "factura_estado" : "Atrasada", "order_date" : "2019-01-02", "INVOICE_NUMBER" : "125863478945", "factura_vence": "05 Nov", "Total": "$RD 3000"}