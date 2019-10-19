from api import cache_interface as ci
import numpy as np


def heat_index(loc, n):
    data = ci.read(loc)

    data = data[-n-1:-1]
    hif_n = 0
    for daily in data:
        hif = 0
        for hourly in daily['hourly']:
            a = hourly['HeatIndexF']
            if int(a) > hif:
                hif = int(a)
        hif_n += hif
    return hif_n / n