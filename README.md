# postcard
动态电子名片

## 效果图
<img src="/final.svg" alt="开发环境效果图">
<img src="https://postcard.wh0th.ink/api?img=in&src=1.png" alt="生产环境效果图">

## 请求参数
`/<API>?[options]`

### 路径
```shell
$ flask routes
Endpoint  Methods  Rule
--------  -------  -----------------------
api       GET      /postcard
egg       GET      /teapot
index     GET      /
static    GET      /static/<path:filename>
```

- `/`：主页，重定向至 Github
- `/teapot`：彩蛋
- `/static`：静态文件
- `/api`

### 参数
名片整体可分为四个部分，相关参数也按此顺序介绍。

#### 问候
没有配置。（个人认为这才是动态电子名片的灵魂所在，记得家母第一次碰见的时候吓了一跳）

#### 图片
- `img={in|ex|others}` 选择图片模式：内置/外置/无图片
- `src=<filename>|<url>` `in` 模式下选择文件名称（[仓库路径](/API/res/bg/)），`ex` 模式下为文件 url（直接传入 Base64 还是算了吧）
- `offset_x=<num>`，`offset_y=<num>` 调整图片位置
- `scale=<num>` 控制图片缩放

#### 联系方式
与 Xecades 的 API 完全相同。见
- [API | Xecades](https://api.xecades.xyz/) 提供在线编辑 url 图形界面
- [Github - Xecades/API](https://github.com/Xecades/API)

#### 个签
- `line=<str>`
- `line2=<str>`

上述所有参数均为可选，多余的参数会被忽略。

## 依赖及相关技术说明
因为我没有使用各种虚拟环境的习惯，只好将依赖手动列出来。

pip 中模块名如下：
- flask
- [geoip2](https://github.com/maxmind/GeoIP2-python)
- aiofiles

UA 由 Flask 自动处理。

数据库来自 [GeoLite](https://dev.maxmind.com/geoip/geoip2/geolite2/)。
<!-- ~~实测连我家都找不准~~ -->
<!-- Xecades 在河东 -->
<!-- 还有一堆只能定位国家和大洲的数据 -->
<!-- 国家统计局，爬虫噩梦，传说中的表格布局就在这里出现了吗？ -->

## Get Involved 参与进来！
能做的事情很多呢。详见 [issue](https://github.com/Master-Hash/postcard/issues)。

~~再说，找 XSS 之类的事情也乐在其中啊。~~

## 贡献
- [@Xecades](https://github.com/Xecades) 作图，提供图标和图片

<!-- 后来因为他单干出了一个 Serverless 的API，我有点气，就把他的仓库作为子模块加进来了 -->

## 致谢
- 前辈 [@hanlin-studio](https://github.com/hanlin-studio) 的[原型](https://github.com/hanlin-studio/IP)
- [P3TERX/GeoLite.mmdb](https://github.com/P3TERX/GeoLite.mmdb)
- [FastGit](https://fastgit.org/)
