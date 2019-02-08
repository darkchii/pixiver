pixiver
=======

[![logo2](https://img.shields.io/badge/pypi-0.0.7-blue.svg)](https://pypi.org/project/pixiver/)
[![logo2](https://img.shields.io/badge/build-passing-green.svg)](https://travis-ci.org/darkchii/pixiver)

这是一个面向 `pixiv` 开发者的 python 包。

安装
----

`pip install -U pixiver`

入门指南
-------

目前 `pixiver` 支持以下功能：

注意: 删除线表示 pixiv 没有提供这类服务或 api。

 + 可浏览 pixiv 每日、每周、每月、新人、原创、受男性欢迎、受女性欢迎、每日 + R-18、每周 + R-18、~~每月 + R-18~~、~~新人 + R-18~~、~~原创 + R-18~~、受男性欢迎 + R-18、受女性欢迎 + R-18排行榜作品。（不需要登录）

 + 可根据作品 id 查看作品相关信息。（不需要登录）

 + 可浏览作品下的所有评论。（不需要登录）

 + 可浏览作品标签、排名、点赞数、收藏数等信息。（不需要登录）

 + 可下载不同尺寸的作品。（不需要登录）

 + 可根据用户 id 获取相关信息。（不需要登录）

 + 其他。

下面开始学习如何使用吧！（个人建议使用 python console）

1. 每日排行：

首先导入包并创建对象

```python
from pixiver.imageiv import Daily

r = Daily(20190125)
# or Daily('2019-01-25')
# or Daily('2019/01/25')
# or Daily('2019.01.25')
```

或者初始化对象后，再 run

```
r = Daily()
res = r.run(20190125)
```

对于正确合法的日期，加载成功后将会显示：

```
Pixiver Initializing...
Initialized!
```

接下来这里我们有两种方式可以浏览排行版：

* 使用 `batch()` 一次加载排行榜前 50 个图像进行处理。但对于网络不好的使用者来说，这可能会很头痛。不过我还提供了另一种加载方式（见方法2）。

```
r.batch()
```

获取当前批次第一个作品

```
>>> rf = r.first()
```

查看图像尺寸

```
>>> rf['illust_attrs'].imsize()
(1228, 1736)
```

查看作品原图链接

```
>>> rf['illust_attrs'].original_url()
'https://i.pximg.net/img-original/....jpg'
```

查看作品迷你图链接

```
>>> rf['illust_attrs'].mini_url()
'https://i.pximg.net/c/48x48/img-master/....jpg'
```

作品标题

```
>>> rf['illust_attrs'].illust_title()
'森倉円初個展「Girl Friend」メインビジュアル'
```

作者昵称

```
>>> rf['illust_attrs'].user_name()
'森倉円*初個展2/15-3/6'
```

作品 id

```
>>> rf['illust_attrs'].illust_id()
'72810724'
```

作品创建日期（未作处理）

```
>>> rf['illust_attrs'].create_date()
'2019-01-23T15:00:05+00:00'
```

作品上传日期（未作处理）

```
>>> rf['illust_attrs'].upload_date()
'2019-01-23T15:00:05+00:00'
```


作品链接（这类图应该是除原图外，质量最好的）

```
>>> rf['illust_attrs'].regular_url()
'https://i.pximg.net/img-master/....jpg'
```

查看作品浏览数

```
>>> rf['illust_attrs'].view_count()
103514
```

查看点赞数

```
>>> rf['illust_attrs'].like_count()
...
```

查看收藏数

```
>>> rf['illust_attrs'].mark_count()
...
```

查看评论数

```
>>> rf['illust_attrs'].comment_count()
...
```

查看作品排名

```
>>> rf['rank']
1
```

查看排名日期

```
>>> rf['rank_date']
'20190125'
```

查看评论

```
>>> vcrf = rf['illust_attrs'].view_comments()
>>> vcrf.first()['comment']
...
>>> vcrf.first()['userName']
...
>>> vcrf.next()['comment']
...
```

查看作品标签信息

```
>>> tags = rf['illust_attrs'].view_tags()
>>> tf = tags.first()
>>> tf
<image.ImageTag object 0x00..>
>>> tf.view_tag()
# tag
...
```

一种更快的获取所有标签的方法

```
>>> for tag in rf['illust_attrs'].all()['tags']['tags']:
...     print(tag['tag'])
...
# output some tags
...
```

查看图像

```
>>> rf['illust_attrs'].view_regul_image()
```

喜欢就保存一个（默认保存原图，否则保存前一个查看图片命令下的图像类型）

```
>>> rf['illust_attrs'].save() # 尺寸为 regular 类型
Saved!
```

一种直接保存原图的方式

```
>>> rf['illust_attrs'].save_original()
Saved!
```

获取下一个作品

```
>> rn = r.next()
```

用法与前一个一样

```
>>> rn['illust_attrs'].imsize()
(1500, 1062)
```

* 一次加载一条：`one()` 一次加载排行榜前 50 个中的 1 个，并加入到队列中，这样依然能使用 `batch()` 一样的功能。

```
"""
from pixiver.imageiv import Daily
r = Daily(20190125)
Pixiver Initializing...
Initialized!
"""

>>> ro = r.one()
```

用法也一样

查看浏览量

```
>>> ro['illust_attrs'].view_count()
108805
```

作者昵称

```
>>> ro['illust_attrs'].user_name()
'森倉円*初個展2/15-3/6'
```

查看标签

```
>>> t = ro['illust_attrs'].view_tags()
>>> tf = t.first()
>>> tf.tag_info()
{'tag': 'オリジナル', 'abstract': '独自に創作したもの。', 'thumbnail': 'https://i.pximg.net/....jpg'}
>>> tf.view_tag()
'オリジナル'
>>> for tag in ro['illust_attrs'].all()['tags']['tags']:
...     print(tag['tag'])
...
オリジナル
女の子
桜
なにこれ可愛い
桜の花
美少女
ロングヘアー
```

查看点赞数

```
>>> ro['illust_attrs'].like_count()
14166
```

查看收藏数

```
>>> ro['illust_attrs'].mark_count()
17145
```

查看评论数

```
>>> ro['illust_attrs'].comment_count()
64
```

查看评论

```
>>> vcro = ro['illust_attrs'].view_comments()
>>> vcro.first()['comment']
...
>>> vcro.curr()['comment']
...
>>> vcro.next()['comment']
...
>>> vcro.last()['comment']
...
```

其他排行用法相同，类名分别为：

```
imageiv.Daily
imageiv.Weekly
imageiv.Mouthly
imageiv.Rookie
imageiv.Original
imageiv.Male
imageiv.Female
imageiv.DailyR
imageiv.WeeklyR
imageiv.MaleR
imageiv.FemaleR
```

2. User 类可根据 `pixiv` 用户 id 查看相关信息

```python
from pixiver.useriv import User
r = User(6415776)
```

与排行榜一样，加载后会输出：

```
Pixiver Initializing...
Initialized!
```

查看用户昵称

```
>>> r.username
'ファルケン@'
```

查看关注总量

```
>>> r.following_total
548
```

是否是会员

```
>>> r.premium
True
```

社交链接，返回数据类型： json

```
>>> r.social
{'twitter': {'url': 'https://twitter.com/YutoZin'}}
```

查看其关注用户信息，返回数据类型： json 

```
>>> r.following_all.first()
{'userId': '490219', 'userName': 'Hiten', 'profileImageUrl': ...}
```

查看作品 id

```
>>> r.illusts.first()
'72318445'
>>> r.illusts.next()
'72147871'
...
```

3. 根据作品 ID 浏览相关信息

```
>>> from pixiver import imageiv
>>> pi = imageiv.PixivImage(72773786)
```

查看评论

```
>>> coms = pi.view_comments()
>>> coms.first()['comment']
'face can be better'
```

评论者的昵称

```
>>> coms.first()['userName']
'...'
```

下一条评论

```
>>> coms.next()['comment']
...
```

最后一条评论

```
>>> coms.last()['comment']
...
```

原图链接

```
>>> pi.original_url()
'https://i.pximg.net/img....jpg'
```

喜欢作品的人数

```
>>> pi.like_count()
12183
```

作者昵称

```
>>> pi.user_name()
'河CY'
```

作品收藏数

```
>>> pi.mark_count()
14370
```

作品评论数

```
>>> pi.comment_count()
64
```

4. 其他：

可以下载标签图

```
>>> from pixiver.imageiv import PixivImage
>>> r = PixivImage(imageid)
>>> r.view_tags().first().save_tag_image()
...
```

作品的几种尺寸

```
>>> from pixiver.imageiv import PixivImage
>>> r = PixivImage(imageid)

# 查看 mini 图
>>> r.view_mini_image()
...

# 查看 thumb 图
>>> r.view_thumb_image()
...

# 查看 small 图
>>> r.view_small_image()
...

# 查看 regular 图
>>> r.view_regul_image()
...

# 查看原图
>>> r.view_orig_image()
...
```

评论中，空字符 '' 为大表情图，(...) 这类是小表情

暂时不支持以下功能：

 * 使用个人账户来完成作品收藏、点赞、关注喜欢的作者、发表评论等功能
 * 查看表情
 * 会员相关功能
 * 命令行版

最后
---

欢迎大家对用法提出更好的意见！

欢迎对指南做更好的补充说明！

欢迎一起做贡献！

谢谢支持！
