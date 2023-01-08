from time import sleep as sleep_
from math import floor


def sleep(secs):
    if secs == 0:
        return
    maxrange = 100 * secs
    if isinstance(maxrange, float):
        sleeplittle = floor(maxrange)
        sleep_((maxrange - sleeplittle) / 100)
        maxrange = int(sleeplittle)
    if maxrange > 0:
        for _ in range(maxrange):
            sleep_(0.008)
