def get_user_last_access(user):
    access = sorted(user.accesses, key=lambda x: x.local_time, reverse=True)[0]
    return access

def print_datetime(dt):
    return dt.strftime('%d/%m/%y-%H:%M')