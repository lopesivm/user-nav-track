from datetime import datetime

from rq import Queue

import models
from workers import redis_conn

def enqueue_post_track(uuid, page_title, page_url, local_time_ms):
    q = Queue(connection=redis_conn)
    local_time = datetime.fromtimestamp(int(local_time_ms)/1000.0)
    q.enqueue(post_track, uuid, page_title, page_url, local_time, datetime.now())
    return True

def post_track(uuid, page_title, full_page_url, local_time, server_time):
    session = models.get_session()
    user = session.query(models.User).get(uuid)
    if not user:
        user = models.User(uuid=uuid)
    pre_url = full_page_url.split('://')[-1].split('?')

    # Here the query param is being filtered out due to the scope of the project, but it could potentially be saved
    # under the access to the page
    page_url, query_param = pre_url if len(pre_url) > 1 else (pre_url[0], None)
    page = session.query(models.Page).filter(models.Page.url==page_url).first()
    if not page:
        page = models.Page(title=page_title, url=page_url)

    access = models.Access(uuid=uuid,
                           local_time=local_time,
                           server_time=server_time)

    user.accesses.append(access)
    page.accesses.append(access)
    session.add(user)
    session.commit()
    return True

def register_email(uuid, email):
    session = models.get_session()
    user = session.query(models.User).get(uuid)
    if not user:
        user = models.User(uuid=uuid,
                           email=email)
    else:
        user.email = email
    session.add(user)
    session.commit()
    return True