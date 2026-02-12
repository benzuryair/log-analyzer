from config import *


def get_source_ip(date):
    new = [j[1] for j in date]
    return {i: new.count(i) for i in new}


def get_protocol(date):
    return {int(i[3]): i[4] for i in date}


def get_suspicions(date):
    suspicions_dikt = {}
    for i in date:
        suspicions_list = []
        if not i[1].startswith(tuple(INTERNAL_IP)):
            suspicions_list.append("external_ips")

        if int(i[3]) in SENSITIVE_PORT:
            suspicions_list.append("sensitive_port")

        if int(i[5]) > LARGE_PACKET:
            suspicions_list.append("large_packet")

        if NIGHT_START <= int(i[0][11:13]) < NIGHT_END:
            suspicions_list.append("night_activity")

        if i[1] in suspicions_dikt:
            for j in suspicions_dikt[i[1]]:
                if j not in suspicions_list:
                    suspicions_list.append(j)
        suspicions_dikt[i[1]] = suspicions_list

    return suspicions_dikt


def filter_suspicions(suspicions_dikt):
    return {i: j for i, j in suspicions_dikt.items if len(j) >= 2}
