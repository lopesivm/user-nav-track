from sqlalchemy import func

from models import get_session, Access, Page

def get_global_access_distribution():
    session = get_session()
    access =  session.query(func.count(Access.page_id), Page.title).join(Page).group_by(Page)
    return access

def get_user_access_distribution(uuid):
    session = get_session()
    access = session.query(func.count(Access.page_id), Page.title).join(Page).filter(Access.uuid==uuid).group_by(Page)
    return access