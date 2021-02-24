import locale, datetime, geoip2.database, os, logging, requests, aiofiles
from base64 import b64encode
from mimetypes import guess_type

icons = [os.path.splitext(i)[0] for i in os.listdir("./API/res/icon")]
required_param = {
    "scale": 0.5,
    "offset_x": 250,
    "offset_y": 32,
    "line": "",
    "line2": "",
}

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
    if response.city.names:
        return response.city.names['zh-CN']
    elif response.country.names:
        return response.country.names['zh-CN']
    elif response.continent.names:
        return response.continent.names['zh-CN']
    else:
        logging.warning(f"找不到 ip 位置：{ip}")
        return "神秘位置" # 这里用什么好呢

# https://blog.csdn.net/sinat_37967865/article/details/94554568
def hrefToBase64(href: str) -> str:
    try:
        img_data = requests.get(href)
    except:
        return ""
    base64_data = b64encode(img_data.content)
    return f'data:{img_data.headers["Content-Type"]};base64,{str(base64_data, "utf-8")}'

def fileToBase64(filename: str) -> str:
    internal_imgs = os.listdir("./API/res/bg")
    _type = guess_type(filename)
    if _type[0] and _type[0].split("/")[0] == "image" and filename in internal_imgs:
        with open(f"./API/res/bg/{filename}", mode="rb") as f:
            img_data = f.read()
        base64_data = b64encode(img_data)
        return f'data:{_type[0]};base64,{str(base64_data, "utf-8")}'
    else:
        return ""

async def iconToBase64(filename: str) -> str:
    if filename in icons:
        async with aiofiles.open(f"./API/res/icon/{filename}.svg", mode="rb") as f:
            img_data = await f.read()
        base64_data = b64encode(img_data)
        return f'data:image/svg+xml;base64,{str(base64_data, "utf-8")}'
    else:
        return ""
# icons = {"github": "Master-Hash", "email": "A137294381b@163.com"}
# res = [{"text": "Master-Hash", "b64_data": "pass"}, {"text": "A137294381b@163.com", "b64_data": "pass"}]
async def getSocial(icons: dict[str, str]) -> list[dict[str, str]]:
    _res = []
    for i in icons:
        _data = await iconToBase64(i)
        _item = {"b64_data": _data, "text": icons[i], "alt": i}
        _res.append(_item)
    return _res
