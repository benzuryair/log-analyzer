from config import *


def get_external_ips(date_list):
    return [i for i in date_list if not i[1].startswith(tuple(INTERNAL_IP))]
