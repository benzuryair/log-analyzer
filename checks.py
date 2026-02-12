from config import *


def get_external_ips(date_list):
    return [i for i in date_list if not i[1].startswith(tuple(INTERNAL_IP))]


def get_sensitive_port(date_list):
    return [i for i in date_list if int(i[3]) in SENSITIVE_PORT]


def get_large_packet(date_list):
    return [i for i in date_list if int(i[5]) > LARGE_PACKET]


def tag_traffic(date_list):
    return ["LARGE" if int(i[5]) > LARGE_PACKET else "NORMAL" for i in date_list]
