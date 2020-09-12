import json
from datetime import datetime

from app import db


class Resource(db.Model):
    __tablename__ = 'resource'
    rid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    verycd_id = db.Column(db.Integer, default=0, nullable=False)
    title = db.Column(db.Text, default='', nullable=False)
    status = db.Column(db.Text, default='', nullable=False)
    brief = db.Column(db.Text, default='', nullable=False)
    publisher = db.Column(db.Text, default='', nullable=False)
    publish_time = db.Column(db.Integer, default=0, nullable=False)
    update_time = db.Column(db.Integer, default=0, nullable=False)
    pri_category = db.Column(db.Text, default='', nullable=False)
    sec_category = db.Column(db.Text, default='', nullable=False)
    ed2k_links = db.Column(db.Text, default='', nullable=False)
    description = db.Column(db.Text, default='', nullable=False)
    related = db.Column(db.Text, default='', nullable=False)
    vcpv = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return '<Resource %r>' % self.verycd_id


class ResourceTitleView(object):
    def __init__(self):
        self.rid = 0
        self.verycd_id = 0
        self.title = ""
        self.publisher = ""
        self.publish_time = ""
        self.update_time = ""
        self.pri_category = ""
        self.sec_category = ""

    @staticmethod
    def from_resource_data_model(resource: Resource):
        view = ResourceDetailView()
        view.rid = resource.rid
        view.verycd_id = resource.verycd_id
        view.title = resource.title
        view.publisher = resource.publisher
        view.publish_time = datetime.fromtimestamp(resource.publish_time).strftime("%Y/%m/%d %H:%M:%S")
        view.update_time = datetime.fromtimestamp(resource.update_time).strftime("%Y/%m/%d %H:%M:%S")
        view.pri_category = resource.pri_category
        view.sec_category = resource.sec_category
        return view


class ResourceDetailView(object):
    def __init__(self):
        self.rid = 0
        self.verycd_id = 0
        self.title = ""
        self.status = ""
        self.brief = ""
        self.publisher = ""
        self.publish_time = ""
        self.update_time = ""
        self.pri_category = ""
        self.sec_category = ""
        self.ed2k_links = []
        self.description = ""
        self.related = []
        self.vcpv = 0

    @staticmethod
    def from_resource_data_model(resource: Resource):
        view = ResourceDetailView()
        view.rid = resource.rid
        view.verycd_id = resource.verycd_id
        view.title = resource.title
        view.status = resource.status
        view.brief = resource.brief
        view.publisher = resource.publisher
        view.publish_time = datetime.fromtimestamp(resource.publish_time).strftime("%Y/%m/%d %H:%M:%S")
        view.update_time = datetime.fromtimestamp(resource.update_time).strftime("%Y/%m/%d %H:%M:%S")
        view.pri_category = resource.pri_category
        view.sec_category = resource.sec_category
        view.ed2k_links = json.loads(resource.ed2k_links)
        view.description = resource.description
        view.related = json.loads(resource.related)
        view.vcpv = resource.vcpv
        return view
