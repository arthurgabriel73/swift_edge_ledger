from datetime import datetime

from pytz import timezone, utc

brazil_tz = timezone('America/Sao_Paulo')


def get_utc_now() -> datetime:
    return datetime.now(utc)