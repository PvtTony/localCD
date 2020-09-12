import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from views import PageRequest

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# TODO change it
app.config['SECRET_KEY'] = 'test_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'simplecd.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEFAULT_PAGE_SIZE'] = 30
db = SQLAlchemy(app)

from service import find_resource_title, select_resource_detail_by_verycd_id


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/query', methods=['GET'])
def query():
    title = request.args.get('title')
    pri_category = request.args.get('pri_category')
    paging = PageRequest()
    paging.page = int(request.args.get('page')) if request.args.get('page') is not None else 1
    paging.page_size = int(request.args.get('page_size')) if request.args.get('page_size') is not None \
        else app.config['DEFAULT_PAGE_SIZE']
    if pri_category is None:
        pg = find_resource_title(title, paging)
    else:
        pg = find_resource_title(title, paging, pri_category=pri_category)
    return render_template('query.html', title=title, resources=pg)


@app.route('/resource/<verycd_id>', methods=['GET'])
def resource(verycd_id):
    resource = select_resource_detail_by_verycd_id(verycd_id)
    return render_template('detail.html', resource=resource)


if __name__ == '__main__':
    app.run()
