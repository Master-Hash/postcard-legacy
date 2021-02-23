# postcard
动态电子名片

## 请求参数
`/<API>?[options]`

### 路径
```shell
$ flask routes
Endpoint  Methods  Rule
--------  -------  -----------------------
contact   GET      /contact
egg       GET      /teapot
greeting  GET      /greeting
index     GET      /
postcard  GET      /postcard
static    GET      /static/<path:filename>
```

- `/`
- `/teapot`：彩蛋
- `/static`：静态文件
- API：
  - `/postcard`：主要维护，推荐使用
  - `/greeting`：只显示左边问候和可选图片
  - `/contact`：只显示右边联系方式和个签

就现在的优化而言，不推荐使用前两个，毕竟只是简单地挖掉了部分，没有修改路径和 viewbox。

### 参数
- `img={in|ex|others}` 选择图片模式：内置/外置/无图片
- `src=<filename>|<url>` `in` 模式下选择文件名称（[仓库路径](/static)），`ex` 模式下为文件 url（base64 你觉得行也行）
- `github=<username>`
- `qq=<username>`
- `mail=<address>`
- `bilibili=<username>`
- `line=<str>`
- `line2=<str>` @Xecades 建议摆成两行。两行之间没有依赖关系。

所有参数均为可选，多余的参数会被忽略。

## 依赖及相关技术说明
因为我没有使用各种虚拟环境的习惯，只好将依赖手动列出来。

pip 中模块名如下：
- flask
- [geoip2](https://github.com/maxmind/GeoIP2-python)

UA 由 Flask 自动处理。

数据库来自 [GeoLite](https://dev.maxmind.com/geoip/geoip2/geolite2/)。
<!-- ~~实测连我家都找不准~~ -->
<!-- 国家统计局，爬虫噩梦，传说中的表格布局就在这里出现了吗？ -->

## Get Involved 参与进来！
能做的事情很多呢。详见 [issue](https://github.com/Master-Hash/postcard/issues)。

~~再说，找 XSS 之类的事情也乐在其中啊。~~

## 贡献
- [@Xecades](https://github.com/Xecades) 作图

## 致谢
- 前辈 [@hanlin-studio](https://github.com/hanlin-studio) 的[原型](https://github.com/hanlin-studio/IP)
- [P3TERX/GeoLite.mmdb](https://github.com/P3TERX/GeoLite.mmdb)
- [FastGit](https://fastgit.org/)
