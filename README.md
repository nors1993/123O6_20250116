# 基于该仓库进行修改https://github.com/johnshazhu/12306
# 12306
# 坐席类别
    # 特等座 P 选座只有A、C、F
    # 商务座 9 选座只有A、C、F
    # 一等座 M 选座为A、C、D、F
    # 二等座 O 选座为A、B、C、D、F（不是0，是大写的字母偶）

    # 高级动卧 A 不能选铺位
    # 高级软卧 6 不能选铺位
    # 一等卧 I 不能选铺位
    # 动卧 F 下铺 上铺
    # 二等卧 J 不能选铺位？

    # 硬座 1 不能选座
    # 软座 2 不能选座
    # 硬卧 3 下铺 中铺 上铺
    # 软卧 4 下铺 上铺
    
# 配置文件 config.properties
```
username=12306账号
password=12306密码
trainCode=订票车次（可多个车次，多个车次以英文逗号隔开，优先匹配前面的）
seatType=席别（上面坐席类别说明中）
date=车次日期，格式为yyyy-MM-dd，例如 2023-09-19）
from=出发站
to=到达站
passengers=乘客（可多个，名字以英文逗号隔开）
castNum=登录用户的身份证的后4位，获取短信验证码用
chooseSeats=选择动车/高铁坐席（高铁坐席一般为A、B、C, D、F，一人的话可以设置1F，1A等，两人的话为1D1F，或1F2F）
seatDetailType=卧铺（100为1个下铺，200为两个下铺，依次类推。101为1个下铺和上铺，211为2个下铺，一个中铺，一个上铺）
purpose_codes=（ADULT: 成人，0x00: 学生）
timesBetweenTwoQuery=两次查询的时间间隔（单位为秒），设置后自动查询余票（候补下单设置时默认会取消自动查询）
candidate=1（1为候补下单）
aftertime=12:00（只看几点以后的车次，仅当未设置订票车次时生效）
```
配置config.properties后，执行qr.py，resource目录下打开qr_image.jpg，手机12306 app扫码登录后，可自动购票。  

或执行login.py，通过账号密码方式自动登录后购票。

暂只支持单程票。

# Windows 部署（20250116追加）
1、安装NodeJS

2、优化原有代码，使得在windows中部署不报错

1）在qr.py文件开头中增加下列代码：（保证文件在windows中能够正确以UTF-8的格式打开）

```python
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
```

2）在config.py文件中将以下代码改写：

```python
with open('config.properties', 'r') as f:

```

改为：

```python
with open('config.properties', 'r', encoding='utf-8') as f:
```

3、按照README中的内容修改配置参数并运行。Enjoy！

**Tips**:&#x20;

1）查询时间最短只能设置为0.4，即timesBetweenTwoQuery=0.4，低于这个值，可能会封IP地址。

2）如果在12306平台 更新了乘客信息 或 切换新账号, 请手动删除cache目录否则可能有未知问题。
