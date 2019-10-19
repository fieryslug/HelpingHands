import datetime


def to_date(date):
    return datetime.date(*list(map(int, date.split('-'))))


def enumerate_date(d1, d2, inclusive=True):
    if type(d1) == str:
        d1 = to_date(d1)
    if type(d2) == str:
        d2 = to_date(d2)

    delta = d2 - d1
    if inclusive:
        delta += datetime.timedelta(1)

    n = int(delta.days)
    d_list = []
    for i in range(n):
        d_list.append(d1 + datetime.timedelta(i))
    return d_list

