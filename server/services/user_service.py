from models import get_session, User

def get_registered_users():
    session = get_session()
    return session.query(User).filter(User.email.isnot(None))

def get_user_by_uuid(uuid):
    session = get_session()
    return session.query(User).get(uuid)