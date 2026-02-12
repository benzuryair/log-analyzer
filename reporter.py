def get_source_ip(date):
    new = [j[1] for j in date]
    return {i: new.count(i) for i in new}


def get_protocol(date):
    return {int(i[3]): i[4] for i in date}
