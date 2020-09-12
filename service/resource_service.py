from models import Resource, ResourceTitleView, ResourceDetailView
from views import Page, PageRequest


def find_resource_title(title: str, paging: PageRequest, pri_category='') -> Page:
    pg = Page()
    pg.current_page = paging.page
    pg.page_size = paging.page_size
    limit = paging.limit
    offset = paging.offset
    if title is None or title == '':
        return pg
    if pri_category != '':
        pg.total = Resource.query \
            .filter((Resource.title.like('%{}%'.format(title))) & (Resource.pri_category == pri_category)).count()
    else:
        pg.total = Resource.query \
            .filter(Resource.title.like('%{}%'.format(title))).count()
    if pg.total != 0:
        if pri_category != '':
            resources = Resource.query \
                .with_entities(Resource.rid, Resource.verycd_id, Resource.title,
                               Resource.pri_category, Resource.sec_category,
                               Resource.publisher, Resource.publish_time, Resource.update_time) \
                .filter((Resource.title.like('%{}%'.format(title))) & (Resource.pri_category == pri_category)) \
                .order_by(Resource.update_time.desc()) \
                .limit(limit).offset(offset).all()
        else:
            resources = Resource.query \
                .with_entities(Resource.rid, Resource.verycd_id, Resource.title,
                               Resource.pri_category, Resource.sec_category,
                               Resource.publisher, Resource.publish_time, Resource.update_time) \
                .filter(Resource.title.like('%{}%'.format(title))).order_by(Resource.update_time.desc()) \
                .limit(limit).offset(offset).all()
        pg.data = list(map(ResourceTitleView.from_resource_data_model, resources))
    return pg


def select_resource_detail_by_verycd_id(verycd_id: int):
    if verycd_id is None or verycd_id == 0:
        return None
    resource = Resource.query.filter(Resource.verycd_id == verycd_id).one()
    return ResourceDetailView.from_resource_data_model(resource)
