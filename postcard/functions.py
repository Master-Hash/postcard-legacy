import locale, datetime, geoip2.database, os
# from .settings import *

if os.name == "nt":
    locale.setlocale(locale.LC_ALL, "zh_cn")
else:
    locale.setlocale(locale.LC_ALL, "zh_CN.UTF-8")

def today() -> str:
    a = datetime.date.today()
    return f"{a.year} 年 {a.month} 月 {a.day} 日 {a.strftime('%A')}"

def getCity(ip: str) -> str:
    if ip == "127.0.0.1":
        # There's no place like 127.0.0.1，that's a famous photo
        return "本地"
    with geoip2.database.Reader("GeoLite2-City.mmdb") as reader:
	    response = reader.city(ip)
    return response.city.names['zh-CN']
