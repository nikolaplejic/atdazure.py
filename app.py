import azurecfg
import azuredb
import azurecache
import azuretable

import uuid
from flask import Flask, render_template, redirect, request, url_for
from sqlalchemy.sql import select

# Flask bootstrap --------------------------------------------------------------

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Table Storage ----------------------------------------------------------------

@app.route('/table')
def table_handler():
    entities = azuretable.table_service.query_entities('atd', "PartitionKey eq '2014'")
    return render_template('table_list.html', entities=entities)

@app.route('/table/new', methods=['POST', 'GET'])
def table_new_handler():
    if request.method == 'POST':
        data = request.form['data']
        entity = {
            'RowKey': str(uuid.uuid1()),
            'PartitionKey': '2014',
            'data': data
        }

        if azuretable.table_service.insert_entity('atd', entity):
            return redirect(url_for('table_handler'))

    return render_template('table_new.html')

@app.route('/table/row/<rowid>')
def table_row_handler(rowid):
    entity = azuretable.table_service.get_entity('atd', '2014', str(rowid))
    return render_template('table_row.html', entity=entity)

# SQL Database -----------------------------------------------------------------

@app.route('/sql')
def sql_handler():
    query = select([azuredb.products])
    result = azuredb.dbconn.execute(query)
    return render_template('sql_list.html', result=result)

@app.route('/sql/new', methods=['POST', 'GET'])
def sql_new_handler():
    if request.method == 'POST':
        i = azuredb.products.insert().values(ProductName=request.form['product_name'],
                                             ProductDescription=request.form['product_description'],
                                             Price=request.form['price'])
        if azuredb.dbconn.execute(i):
            return redirect(url_for('sql_handler'))

    return render_template('sql_new.html')

@app.route('/sql/row/<rowid>')
def sql_row_handler(rowid):
    s = select([azuredb.products]).where(azuredb.products.c.ProductID == rowid)
    result = azuredb.dbconn.execute(s)
    row = result.fetchone()
    return render_template('sql_row.html', row=row)

# Cache ------------------------------------------------------------------------

@app.route('/cache')
def cache_handler():
    res = azurecache.r.get('a_key')
    return render_template('cache_home.html', e=res)

@app.route('/cache/set')
def cache_set():
    azurecache.r.set('a_key', 'My hovercraft is full of eels.')
    return redirect(url_for('cache_handler'))

@app.route('/cache/del')
def cache_del():
    azurecache.r.delete('a_key')
    return redirect(url_for('cache_handler'))

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
