import locale, datetime
from .settings import *
locale.setlocale(locale.LC_ALL, "zh_cn")

def today() -> str:
    return datetime.date.today().strftime(ds).replace("0", "")
