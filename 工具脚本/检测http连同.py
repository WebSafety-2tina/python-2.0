import re
import requests

# 正则表达式模式，用于匹配HTTP和HTTPS链接
link_pattern = r'https?://\S+'


def check_links(text):
    # 找到文本中的所有链接
    links = re.findall(link_pattern, text)

    # 遍历链接并检查可用性
    results = {}
    for link in links:
        try:
            response = requests.get(link)
            if response.status_code == 200:
                results[link] = True
            else:
                results[link] = False
        except requests.exceptions.RequestException:
            results[link] = False

    return results


if __name__ == "__main__":
    text = """
    Here are some example links:
    Build ID: @StarLinkCloud
URL: http://106.12.160.106:18/login.aspx
Username: 101
Password: 00882
Application: Microsoft_[Edge]_Default
===============
URL: http://120.26.214.72:8888/49a636bb/
Username: woda1bby
Password: aa1d7ad59e9d
Application: Microsoft_[Edge]_Default
===============
URL: https://subscribe.receivei.com/
Username: natsuki.gjm.china@gmail.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://www.ssk2.top:18/login.aspx
Username: 101
Password: 00882
Application: Microsoft_[Edge]_Default
===============
URL: http://124.156.208.72:8888/tencentcloud/
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://47.242.229.197:8888/08d078b3
Username: wjdmcxtj
Password: 4f62ad4e
Application: Microsoft_[Edge]_Default
===============
URL: http://47.242.247.237:8888/61b14e59
Username: zzkvdibt
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ganyu.live/
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ganyu.live/install/index.php
Username: ganyu_live
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://web.jnruidatong.com/okoweb/activate
Username: 18156622714
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://subscribe.receivei.com/
Username: 488358
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://anyhk.net/clientarea.php
Username: natsuki.gjm.china@gmail.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://passport.126.com/webzj/v1.0.1/pub/index_dl2_new.html
Username: gjm18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://havanalogin.taobao.com/mini_login.htm
Username: tb4900889024
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://154.205.7.116:8888/bind
Username: 18156622714
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://subscribe.receivei.com/
Username: 919241584@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ganyu.live/wp-admin/user-new.php
Username: и“ќжњ¬
Password: lanben2020
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ssk2.top:18/login.aspx
Username: 101
Password: 00882
Application: Microsoft_[Edge]_Default
===============
URL: http://120.48.11.6/member/login
Username: natsuki@admin.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://ssk2.top:1902/login
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.11px.cn/code/weixin/1459.html
Username: зі»з»џз®Ўзђ†е‘
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://39.108.128.144:8888/4c3d8ac4
Username: irzlwdbq
Password: b622374b
Application: Microsoft_[Edge]_Default
===============
URL: https://user.mihoyo.com/
Username: ying1004913827@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://www.ssk3.top/Admin/login
Username: demo@demo.com
Password: 123456
Application: Microsoft_[Edge]_Default
===============
URL: http://43.152.199.245:8888/tencentcloud/
Username: telkwevr
Password: a1f8b7e8f04f
Application: Microsoft_[Edge]_Default
===============
URL: http://120.26.214.72:8888/admin/
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://120.48.11.6:8888/2a8f04f0/
Username: 4t14y2c1
Password: bc2dbe9a
Application: Microsoft_[Edge]_Default
===============
URL: http://merc.zfc1688.cn/
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ganyu.live/wp-admin/install.php
Username: Natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://freemycloud.pw/auth/login
Username: 18156622714@163.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html
Username: yu1888068021
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.smschinese.com.cn/Login.shtml
Username: natsuki
Password: 806838
Application: Microsoft_[Edge]_Default
===============
URL: http://106.14.201.49:8888/admin/
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://124.156.208.72:8888/tencentcloud/
Username: telkwevr
Password: ba4ce8169436
Application: Microsoft_[Edge]_Default
===============
URL: http://89.40.4.249:8888/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://120.26.214.72:8888/34b1f03f
Username: 1qo5qpmp
Password: 8041cf48
Application: Microsoft_[Edge]_Default
===============
URL: http://47.242.229.197:8888/8b7f2c26
Username: barqyhew
Password: b44ad042
Application: Microsoft_[Edge]_Default
===============
URL: http://120.48.11.6:888/phpmyadmin_977e3093938c42d8/index.php
Username: root
Password: f02770bd0e4c8c35
Application: Microsoft_[Edge]_Default
===============
URL: http://104.224.177.29:33123/9f72bf8c
Username: hmrgssfi
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://acg198.com/zy/azyx/page/2
Username: afmin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://120.48.11.6:8888/96669f99/
Username: eavubjqf
Password: e624bd7e
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk4.top/
Username: Natsuki
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://login.taobao.com/member/login.jhtml
Username: tb4900889024
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://qulingyu2.com/login/
Username: afmin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://www.ssk3.top/member/register/
Username: зі»з»џз®Ўзђ†е‘
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://btacg.vip/29127/
Username: adminbchdhdj
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://89.40.4.249:8888/7ba33e16
Username: k3fydalj
Password: b9339b25
Application: Microsoft_[Edge]_Default
===============
URL: https://signin.aws.amazon.com/signin
Username: 18156622714@163.com
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: https://kh.yto.net.cn/new/login
Username: 15056937128
Password: Song123@
Application: Microsoft_[Edge]_Default
===============
URL: http://e3.jdv.cc/e3/webopm/web/
Username: HBKF02
Password: zxcvbnm1.
Application: Microsoft_[Edge]_Default
===============
URL: http://104.224.177.29:8888/4fee64f8
Username: ujpwueqe
Password: a6f71533
Application: Microsoft_[Edge]_Default
===============
URL: https://subscribe.receivei.com/
Username: 988089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://e3.jdv.cc/e3/webopm/web/
Username: HBKF07
Password: @natsuki00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.158.219.11:8888/tencentcloud/
Username: telkwevr
Password: f85f406dc22e
Application: Microsoft_[Edge]_Default
===============
URL: http://45.113.0.28:8888/a62aa745
Username: ailca4tc
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://154.205.7.116:8888/e0eafa6b
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://vip.photonpay.com/account/login
Username: 18156622714
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.wwttl.com/6746.html
Username: natsuki1321
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://auth.services.adobe.com/zh_CN/index.html
Username: natsuki.gjm.china@gmail.com
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://ssk2.top/reg
Username: зі»з»џз®Ўзђ†е‘
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://89.40.2.96:8888/0fe497e0
Username: v0gxldfh
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://wet-22.xyz/archives/9543
Username: zyl200194
Password: 200194
Application: Microsoft_[Edge]_Default
===============
URL: https://localhost:44316/login.aspx
Username: 101
Password: 00882
Application: Microsoft_[Edge]_Default
===============
URL: http://120.26.214.72:8888/
Username: 18156622714
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://124.156.216.232:8888/8e5bac32
Username: 5qlc0hww
Password: 2b007a81
Application: Microsoft_[Edge]_Default
===============
URL: http://43.133.163.30:8888/tencentcloud/
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://login.live.com/oauth20_authorize.srf
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://cloud.tencent.com/login/subAccount
Username: natsuki
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://www.ssk2.top:81/Admin/login
Username: natsuki@admin.com
Password: 123456
Application: Microsoft_[Edge]_Default
===============
URL: https://mms.yangkeduo.com/login/
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://47.242.7.58:8888/c4194324/
Username: woda1bby
Password: b322fae65e5b
Application: Microsoft_[Edge]_Default
===============
URL: http://8.210.169.141:8888/60a318cd/
Username: woda1bby
Password: 3cb2aaa6e704
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk4.top/
Username: NAtsuki
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://dl.reg.163.com/webzj/v1.0.1/pub/index2_new.html
Username: yu1888068021@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://89.40.13.75:8888/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.yinghua.homes/admin.php
Username: liujianghao
Password: miko2016
Application: Microsoft_[Edge]_Default
===============
URL: http://39.101.194.37:39228/member.php
Username: test
Password: test123
Application: Microsoft_[Edge]_Default
===============
URL: https://www.yinghua.homes/install/index.php
Username: www_yinghua_hom
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://89.40.13.75:8888/phpmyadmin/index.php
Username: www_yinghua_hom
Password: eib2RbPHzySpdhA8
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.1.1/qis_m/QIS_wireless.htm
Username: ASUS_70_2G
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://121.4.75.16:8888/2bf7282d
Username: qsttm2c0
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://89.40.13.75:8888/phpmyadmin/index.php
Username: root
Password: f96ed6fc1a5df369
Application: Microsoft_[Edge]_Default
===============
URL: http://89.40.13.75:8888/6a60c9ad
Username: klzw8adp
Password: 30eb6ad9
Application: Microsoft_[Edge]_Default
===============
URL: https://yinghua.homes/171/.html
Username: najdnand
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://212.24.109.237:8888/feab816f
Username: pu7jbfyf
Password: a265861d
Application: Microsoft_[Edge]_Default
===============
URL: http://212.24.109.237:8888/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://mp.weixin.qq.com/cgi-bin/readtemplate
Username: 026351
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14:8888/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://login.bce.baidu.com/
Username: жµ·еЏЈжЎ”ж±‡иґёж“
Password: @Qaz00882
Application: Microsoft_[Edge]_Default
===============
URL: http://localhost:9798/
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.208.199:8888/07a83f70
Username: gplvtagc
Password: ae78ccb3
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.208.199:8888/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://rjhome.me/46984.html
Username: 358165
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14:8888/6349a923
Username: jfkqzwta
Password: dcdacfd8
Application: Microsoft_[Edge]_Default
===============
URL: https://www.12315.cn/cuser/index
Username: 17394626570
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.208.199:8888/16c52391
Username: ndwj2oct
Password: b1942a16
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.208.199:16807/6b392508
Username: evmuxhdg
Password: cd464360
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/
Username: 912230
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.208.199:26272/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.199.134:8888/b91b91ed
Username: mhcmy6hh
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.208.199:26272/4c5a1f3e
Username: mm8gokgy
Password: 2e7dfdd4
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.199.134:32085/85085ece
Username: vd7q0xeh
Password: a74b17b0
Application: Microsoft_[Edge]_Default
===============
URL: http://121.4.75.16:8888/637ff383
Username: hou4n0f3
Password: 0f4b3a36
Application: Microsoft_[Edge]_Default
===============
URL: https://www.zyk001.com/archives/14633
Username: administrator
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.10.1/cmcc/login.html
Username: username
Password: FTH9YM9M
Application: Microsoft_[Edge]_Default
===============
URL: http://121.4.75.16:8888/
Username: AKIDsKcqwxnQFHAXjhV7YqvqZ3Yt2yhCWcVH
Password: p360h9tU1RQEwUpz0CD3g7UfeU9xa2PZ
Application: Microsoft_[Edge]_Default
===============
URL: https://accounts.google.com/signin/v2/challenge/pwd
Username: natsuki.gjm.china@gmail.com
Password: @gjm008822
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/
Username: 451429
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.epay.com/epayweb/user/register
Username: 992958
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://pay.jccj.cc/user/userinfo.php
Username: UNKNOWN
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14:32084/bind
Username: 18156622714
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ss.lmsq.work/index.html
Username: ad
Password: admin
Application: Microsoft_[Edge]_Default
===============
URL: https://mp.weixin.qq.com/cgi-bin/readtemplate
Username: 124334
Password: @GJM00882
Application: Microsoft_[Edge]_Default
===============
URL: https://mp.weixin.qq.com/cgi-bin/readtemplate
Username: 637239
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://mp.weixin.qq.com/cgi-bin/readtemplate
Username: 084767
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://mp.weixin.qq.com/
Username: reimulm007@foxmail.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://8.219.62.59:7800/fddb6f3a
Username: aqqwozs4
Password: 2d3589e0
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.1.1/
Username: user
Password: c7yacc6p
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.31.18/cgi-bin/luci/
Username: root
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://accounts.google.com/signup/v2/webcreateaccount
Username: miaolovelan1
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14:32084/phpmyadmin/index.php
Username: zfxt_lmsq_work
Password: zfxt
Application: Microsoft_[Edge]_Default
===============
URL: https://zfxt.lmsq.work/User/Login.php
Username: 10001
Password: 123456
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/
Username: 33504660899@gmail.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://zfxt.lmsq.work/install.php
Username: houtai
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14:32084/ead80d9d
Username: 9fcxuqqo
Password: 94c96bac
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14:32084/phpmyadmin/index.php
Username: houtai
Password: houtai
Application: Microsoft_[Edge]_Default
===============
URL: http://43.163.229.168:33828/2f33ae39
Username: gyczbdmo
Password: b640f983
Application: Microsoft_[Edge]_Default
===============
URL: https://sso.ahzwfw.gov.cn/uccp-server/login
Username: 91340104MA8PUA0M5M
Password: @gjm00082
Application: Microsoft_[Edge]_Default
===============
URL: https://www.gsxt.gov.cn/socialuser-use-login.html
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://gx.gsxt.gov.cn/socialuser-use-login.html
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ah.gsxt.gov.cn/socialuser-use-login.html
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://passport.alibaba.com/member/reg/fast/union_reg.htm
Username: reimulm007@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://etax.anhui.chinatax.gov.cn/cas/login
Username: 91340104MA8PUA0M5M
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://account.xiaomi.com/fe/service/login/password
Username: 18156622714
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://cn.account.xiaomi.com/fe/service/login/password
Username: 18156622714
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ganyu.live/install/
Username: www_ganyu_live
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://dashboard.tawk.to/signup
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.zoho.com.cn/desk/signup.html
Username: зЃµжў¦
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://app.crisp.chat/initiate/signup/
Username: зЃµжў¦
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://www.visvn.cn/index.php
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://accounts.clickbank.com/master/create-account
Username: UNKNOWN
Password: mikC!2mF2w7kHBH
Application: Microsoft_[Edge]_Default
===============
URL: https://ui.awin.com/publisher-signup/us/awin/step1
Username: еј е®Ѓ
Password: _.x3Gmx9QQhD5:W
Application: Microsoft_[Edge]_Default
===============
URL: https://xn--gmqz83awjh.com/auth/register
Username: 3350466089
Password: CNFF8bLk:dpv!.7
Application: Microsoft_[Edge]_Default
===============
URL: https://bwh81.net/register.php
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://reg.taobao.com/member/reg/fast/union_reg.htm
Username: tieyuan_hf
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://passport.taobao.com/ac/password_reset.htm
Username: tieyuan_hf
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://login.taobao.com/
Username: tb362595775324
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://havanalogin.taobao.com/mini_login.htm
Username: tb362595775324
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.124.1/router_password_mobile.asp
Username: UNKNOWN
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.81.180:7800/d0456a7d
Username: e7mfkgx6
Password: e26659fb
Application: Microsoft_[Edge]_Default
===============
URL: https://mail.sina.com.cn/register/regmail.php
Username: reimulm
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://smart.mail.163.com/signup/
Username: reimulm
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: http://47.243.57.234:7800/9eaf2891
Username: t5olg243
Password: b343da67
Application: Microsoft_[Edge]_Default
===============
URL: https://github.com/signup
Username: Natsuki890
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://47.243.57.234:888/phpmyadmin_a2e2974959feaba8/index.php
Username: qqq
Password: qqq
Application: Microsoft_[Edge]_Default
===============
URL: https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html
Username: 18156622714@163.com
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14:32084/phpmyadmin/index.php
Username: root
Password: fef720258ba7d1ed
Application: Microsoft_[Edge]_Default
===============
URL: https://onevpshosting.com/cart.php
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://onevpshosting.com/register.php
Username: UNKNOWN
Password: f8.TN_Z5CPdd9CJ
Application: Microsoft_[Edge]_Default
===============
URL: http://43.153.219.163:7800/b35d9bc5
Username: rfm9jgsq
Password: d4be5e19
Application: Microsoft_[Edge]_Default
===============
URL: http://43.153.219.59:31701/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.52shiguang.cc/login/index.html
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://121.4.75.16:8888/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://121.4.75.16:7800/5a78cbee
Username: dmxxqlsx
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.154.186.114:29836/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://8.218.43.131:30585/d6459e46
Username: rq53ni4c
Password: acf8b8d0
Application: Microsoft_[Edge]_Default
===============
URL: http://8.218.43.131:30585/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://129.226.198.106:8888/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://demo.aapanel.com/fdgi87jbn/
Username: aapanel
Password: www.aapanel.com
Application: Microsoft_[Edge]_Default
===============
URL: http://129.226.198.106:24216/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://129.226.198.106:24216/437900ee
Username: 8nw2dwqx
Password: 39f8abf8
Application: Microsoft_[Edge]_Default
===============
URL: https://ysz.reimulm.com/auth/register
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.153.215.12:7800/f03261ee
Username: cgj7t4az
Password: 3ed9f69a
Application: Microsoft_[Edge]_Default
===============
URL: https://ysz.reimulm.com/auth/login
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://yst.reimulm.com/admin00882
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://fzz.reimulm.com/admin008822
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://lm.reimulm.com/auth/login
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://fz.reimulm.com/4afe4965
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://my.vultr.com/deploy/
Username: 3350466889@qq.com
Password: @Gjm008822
Application: Microsoft_[Edge]_Default
===============
URL: https://www.vultr.com/register/
Username: 3350466889@qq.com
Password: @Gjm008822
Application: Microsoft_[Edge]_Default
===============
URL: https://www.vultr.com/register/
Username: 18156622714@qq.com
Password: @Gjm000882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.vultr.com/
Username: 3545293605@qq.com
Password: !NUfi9hDFkeSL8.
Application: Microsoft_[Edge]_Default
===============
URL: https://support.onevps.com/register/BJL5KnDpD8QiUxa1mopc
Username: natsuki
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.93.240:7800/a5e5a24a
Username: 2anuuiup
Password: fce01119
Application: Microsoft_[Edge]_Default
===============
URL: http://149.28.21.204:7800/be49924e
Username: djwz3rhy
Password: a7078a80
Application: Microsoft_[Edge]_Default
===============
URL: https://app.cloudcone.com.cn/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://cloud.digitalocean.com/registrations/email
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://app.cloudcone.com/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/
Username: hjsjss@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://account.hostmem.com/register
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://console.kamatera.com/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.kamatera.com/express/compute/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://my.vultr.com/deploy/
Username: 3545293605@qq.com
Password: @Gjm008822
Application: Microsoft_[Edge]_Default
===============
URL: https://www.zijizhang.com/administrator/
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.122.12:7800/eab4fd23
Username: ufikzmaz
Password: 32195434
Application: Microsoft_[Edge]_Default
===============
URL: https://www.reimulm.com/natsuki256580
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://lm.reimulm.com/auth/login
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/4f967fb8
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://lmm.reimulm.com/
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ysz.reimulm.com/
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://jc.reimulm.com/auth/login
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://xlxianmu.lol/d653de30
Username: 3350466089@qq.com
Password: 308310bfb7ac0cc315d35e8d75db7fa7
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.93.240:7800/5733a789
Username: lfu76cjk
Password: 188b3847
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulmm.com/
Username: 752411
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulmm.com/auth/login
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://router.asus.com/qis/QIS_admin_pass.htm
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://router.asus.com/QIS_wizard.htm
Username: Miao256
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.1.1/QIS_wizard.htm
Username: miao
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.1.1/Main_Login.asp
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.122.12:7800/89acacb1
Username: 8ifesyqf
Password: e51dd46b
Application: Microsoft_[Edge]_Default
===============
URL: http://43.153.215.12:888/phpmyadmin_9715fd080a956ce6/index.php
Username: ysz
Password: ysz
Application: Microsoft_[Edge]_Default
===============
URL: https://demo.proxypanel.cf/login
Username: test@test.com
Password: 123456
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.122.12:888/phpmyadmin_d1f25e29584c6266/index.php
Username: lm
Password: lm
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.234.117:888/phpmyadmin_566e012e58e051e2/index.php
Username: ganyu
Password: ganyu
Application: Microsoft_[Edge]_Default
===============
URL: https://ui.ptlogin2.qq.com/cgi-bin/login
Username: 3545293605@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://xui.ptlogin2.qq.com/cgi-bin/xlogin
Username: 3545293605@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://cnpassport.alibaba.com/mini_login.htm
Username: tieyuan_hf
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ganyujc.top/auth/login
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.reimulmm.com/auth/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://open.weixin.qq.com/
Username: gejinmiao@amashironatsuki.com
Password: Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://m.exmail.qq.com/cgi-bin/loginpage
Username: gejinmiao@amashironatsuki.com
Password: Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://exmail.qq.com/cgi-bin/loginpage
Username: gejinmiao@amashironatsuki.com
Password: Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ganyujc.top/auth/register
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://yunsut.top/natsuki256580
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ganyujc.top/auth/register
Username: 3257832852
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ganyujc.top/auth/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://clients.hostwinds.com/buycloud/274
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.paypal.com/c2/welcome/signup/
Username: и‘›й‡‘и‹—
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://my.vultr.com/
Username: ganyu
Password: @Gjm008822
Application: Microsoft_[Edge]_Default
===============
URL: http://149.28.132.40:11539/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://149.28.132.40:11539/9b0d09d4
Username: epvyz18i
Password: 77122c77
Application: Microsoft_[Edge]_Default
===============
URL: https://support.onevps.com/support/login
Username: 3545293605@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://108.160.143.220:16301/81acb754
Username: 4pfbtwtx
Password: 34dfe255
Application: Microsoft_[Edge]_Default
===============
URL: https://cloud.tencent.com/account/apply-login
Username: 282670
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://cloud.tencent.com/login
Username: ganyu2021@ganyujc.top
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://64.176.36.47:29329/ecdc9b21
Username: xqlwppru
Password: 84d5f2fc
Application: Microsoft_[Edge]_Default
===============
URL: http://141.164.57.90:21664/6a1247c7
Username: h3cgimfp
Password: b9a85131
Application: Microsoft_[Edge]_Default
===============
URL: http://64.176.36.47:29329/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.159.44.207:7800/b564be67
Username: dd8lvz86
Password: 2b3249b8
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.234.117:7800/039f98b5
Username: ddexggke
Password: b75993bc
Application: Microsoft_[Edge]_Default
===============
URL: https://comic345.xyz/auth/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.234.117:7800/ebdfd028
Username: 4mptjsou
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://onevpshosting.com/register.php
Username: 3545293605@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://mail.163.com/register/index.htm
Username: ganyujc2021
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html
Username: ganyujc2021
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.234.117:888/phpmyadmin_704b1adb9131f6ad/index.php
Username: sql
Password: sql
Application: Microsoft_[Edge]_Default
===============
URL: https://guoke.click/auth/login
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://comic345.xyz/auth/login
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.6.33:888/phpmyadmin_4b2518c2ae0744a8/index.php
Username: com
Password: com
Application: Microsoft_[Edge]_Default
===============
URL: https://www.aiyongyun.com/cart
Username: 768463
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://154.204.178.168:36172/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://my.henghost.com/register1.php
Username: 901350
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://my.idcsmart.com/regist.html
Username: 959144
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://139.84.139.89:25201/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://64.176.41.244:38560/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.35.194:34594/46d841f6
Username: lcfz67t3
Password: a40c6d2a
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.35.194:34594/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://65.20.76.113:25637/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://139.84.169.225:16658/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://108.160.143.220:28778/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://my.idcsmart.com/regist.html
Username: 602635
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://my.idcsmart.com/shop/
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lmsq.work/install.html
Username: @gjm00882
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://my.idcsmart.com/shop/shop_detail.html
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.yunlifang.cn/reg.asp
Username: gjm3350466089
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.yunlifang.cn/reg.asp
Username: 335046609
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.huotuiyun.com/register
Username: 523328
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lmsq.work/natsuki00882/
Username: 17394626570
Password: wUBm3E1ycX7x
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lmsq.work/natsuki00882/
Username: 18156622714
Password: tkOsKBXK79lE
Application: Microsoft_[Edge]_Default
===============
URL: https://shandiansd.top/
Username: 792775
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lmsq.work/natsuki00882/
Username: roor
Password: ejjee
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lmsq.work/natsuki00882/
Username: root
Password: hdhdhdd
Application: Microsoft_[Edge]_Default
===============
URL: https://www.41yun.com/register
Username: 424754
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.vpsor.cn/center/register
Username: elqpkdds
Password: @92s__jmo1suwd
Application: Microsoft_[Edge]_Default
===============
URL: https://www.vpsor.cn/center/register
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://lmsq.work/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lmsq.work/register
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://jc.lmsq.work/auth/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lmsq.work/register
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://cloud.03s.cn/
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.41yun.com/login
Username: 7568
Password: q9HpnqASUge5s!A
Application: Microsoft_[Edge]_Default
===============
URL: https://www.41yun.com/login
Username: 5223
Password: VDT7jvcuV.B7pMu
Application: Microsoft_[Edge]_Default
===============
URL: https://www.41yun.com/login
Username: 4472
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.3.46:38679/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://account.oray.com/login/login-win-v3
Username: 678786
Password: TunGyZh20wpsNEhU/bzX6alpZ+NyhlxwxBX5dfhXgE48OGRVAlda5+zXtgaqYtgjrGst0NZKC4tjEXiItJe9HK6TR66/Z4MLBVmDFKLA/RV59SjQpcW+2b4cKT0IYCRMkmhcyftAthYOSuAjZgHGP0xpy1aecejYb918CXrP9q4NSKR4PmmI9hN0zz9Ta2wx1/MM0MVW41lmqtm/U2hwwPBogVgUVsb3gKp1gRpLMH8r/DHHafPLRhuoxONjhp0zBSCEWp/IZ1d/EoE+3lI4zKqcA73yhll09jzR3WV0CPL/yKrUgrQkaZEYZGb+/acEcO7Go9ZAhBlBFCDgyEvJAA==
Application: Microsoft_[Edge]_Default
===============
URL: https://console-v2.oray.com/account/addto
Username: natsuki1233
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://account.oray.com/login/login-win-v3
Username: natsuki1233
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.3.46:38679/4ac990dc
Username: 40ocgaj2
Password: d0eb4e50
Application: Microsoft_[Edge]_Default
===============
URL: https://70u62a1247.yicp.fun/4ac990dc
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://guoke.click/a8c64b52
Username: 3350466089@qq.com
Password: d993a6f644ce55e75b787f0e2c565c57
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.3.46:38679/4ac990dc
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ganyujc.top/auth/login
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://139.84.139.89:25201/2aa4d467
Username: 87nsoj3m
Password: b6627e18
Application: Microsoft_[Edge]_Default
===============
URL: http://139.84.169.225:16658/7f83e0c4
Username: pnrkeyga
Password: dfc3cd65
Application: Microsoft_[Edge]_Default
===============
URL: http://65.20.76.113:25637/b2ac5688
Username: v5oqlja1
Password: 47f1bb98
Application: Microsoft_[Edge]_Default
===============
URL: http://64.176.41.244:38560/c643e5c0
Username: tmyen8kl
Password: d7ee81a9
Application: Microsoft_[Edge]_Default
===============
URL: http://108.160.143.220:28778/bdcb45d4
Username: ozdv3muk
Password: f405c67f
Application: Microsoft_[Edge]_Default
===============
URL: http://43.134.79.238:7800/a1158717
Username: vxrfveww
Password: 1ef8ff9c
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.208.199:7800/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://xiaobai.cab/91f00217
Username: 3350466089@qq.com
Password: 0688ec7abd81e8ce837e25711f2ef1d3
Application: Microsoft_[Edge]_Default
===============
URL: http://43.159.44.207:7800/3fad71ac
Username: w0pvhuxa
Password: d351fd61
Application: Microsoft_[Edge]_Default
===============
URL: http://139.180.134.48:30757/0c74c281
Username: c0j28bzf
Password: fc83b2cd
Application: Microsoft_[Edge]_Default
===============
URL: http://139.180.134.48:30757/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://auth.alipay.com/login/ant_sso_index.htm
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://mdeduct.alipay.com/customer/customerAgreementSign.htm
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://securitycore.alipay.com/validate.htm
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.6.33:7800/96536146
Username: maq4ptdv
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.baidu.com/
Username: 15332788924
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://shandiansd.top/
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://lite.moe/register.php
Username: nn
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://lite.moe/index.php/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://member.dogyun.com/profile/realname
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://account.dogyun.com/register
Username: reimulm007@foxmail.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://account.dogyun.com/register
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.28idc.com/login
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://154.204.178.168:36172/1c799ead
Username: sn9s95mk
Password: 5425ec1b
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.208.199:7800/fb26de89
Username: qytfor4c
Password: 50695cad
Application: Microsoft_[Edge]_Default
===============
URL: https://www.instagram.com/accounts/emailsignup/
Username: UNKNOWN
Password: zSnwqXbxg-w9J:s
Application: Microsoft_[Edge]_Default
===============
URL: https://www.instagram.com/accounts/emailsignup/
Username: zhangsan123
Password: VB9x.e8vAjySQpA
Application: Microsoft_[Edge]_Default
===============
URL: https://lsptu8.com/
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://155.138.202.243:25719/e807855e
Username: kommmng8
Password: 7ae6a201
Application: Microsoft_[Edge]_Default
===============
URL: http://95.179.166.22:24699/2a5400cc
Username: odgkwokv
Password: 0800bd89
Application: Microsoft_[Edge]_Default
===============
URL: http://136.244.69.24:32106/c904b13d
Username: zun5ycci
Password: 1915409f
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.71.187:41360/b31ce737
Username: ocq9ijz4
Password: 6d45dbf2
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.166.86:17819/92afc5a2
Username: w1omdbka
Password: 9daa9f92
Application: Microsoft_[Edge]_Default
===============
URL: http://95.179.208.211:29285/e189e149
Username: utrtolzd
Password: 0371ec39
Application: Microsoft_[Edge]_Default
===============
URL: http://149.28.202.192:40937/4a7a60dd
Username: lg2plyes
Password: beaec6fd
Application: Microsoft_[Edge]_Default
===============
URL: http://149.28.127.123:34482/6a22548a
Username: swltimlt
Password: 17fe9787
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.209.59:31740/9ddf7088
Username: 0jo0lz0l
Password: f2995f48
Application: Microsoft_[Edge]_Default
===============
URL: http://95.179.166.22:24699/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://155.138.202.243:25719/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.71.187:41360/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.166.86:17819/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://136.244.69.24:32106/bind
Username: 17394626570
Password: @gjm00882\
Application: Microsoft_[Edge]_Default
===============
URL: http://95.179.208.211:29285/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://149.28.202.192:40937/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://shandiansd.top/
Username: 930352
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://shandiansd.top/
Username: ganyuCloud@ganyujc.top
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://bandwagonhost.com/clientarea.php
Username: 18156622714@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.23/
Username: natsuki
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.33/
Username: natsuki
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://149.28.127.123:28390/8d84f8a4
Username: lqqa7lgz
Password: e11eb0d9
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.209.59:12377/94662a0b
Username: i8aforuy
Password: 63c48c15
Application: Microsoft_[Edge]_Default
===============
URL: http://149.28.127.123:28390/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.209.59:12377/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://140.82.25.165:41517/12338c05
Username: nzxofjul
Password: 012a42c7
Application: Microsoft_[Edge]_Default
===============
URL: http://140.82.25.165:41517/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://144.202.120.100:21714/3e60d792
Username: aetnfr35
Password: 8d1bcc5c
Application: Microsoft_[Edge]_Default
===============
URL: http://144.202.120.100:21714/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.aiyongyun.com/login
Username: 18156622714
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.1.1/cgi-bin/luci
Username: useradmin
Password: 5hffy
Application: Microsoft_[Edge]_Default
===============
URL: https://billing.hostens.com/cart/
Username: 3350466089@qq.com
Password: NQPNX@eceZ8qTCX
Application: Microsoft_[Edge]_Default
===============
URL: https://www.dmit.io/
Username: еј
Password: 7UPPdV.Nc2!GuNM
Application: Microsoft_[Edge]_Default
===============
URL: https://www.dmit.io/
Username: US
Password: 7UPPdV.Nc2!GuNM
Application: Microsoft_[Edge]_Default
===============
URL: https://www.dmit.io/index.php
Username: UNKNOWN
Password: s!UsvnHuCJD3Tyk
Application: Microsoft_[Edge]_Default
===============
URL: https://www.dmit.io/index.php
Username: UNKNOWN
Password: s!UsvnHuCJD3Tyk
Application: Microsoft_[Edge]_Default
===============
Username: host.78641fd7ee5d4f7
Password: default
Application: Microsoft_[Edge]_Default
===============
URL: https://www.cubecloud.net/cart.php
Username: CubeCloud-2023326499
Password: 4511322jbkbb
Application: Microsoft_[Edge]_Default
===============
URL: https://bandwagonhost.com/clientarea.php
Username: 3545293605@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://bwh81.net/register.php
Username: 3545293605@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.cubecloud.net/cart.php
Username: CubeCloud-2023326909
Password: 4511322jbkbb
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lcayun.com/register
Username: 276631
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.xnxx.com/video-17698id4/no_se_que_poner
Username: gjb4227
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html
Username: 18156622714
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: https://mail.163.com/register/index.htm
Username: 18156622714
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: https://mail.163.com/register/index.htm
Username: gjmsvip
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.35:19734/6aa534af
Username: pqr4kh5z
Password: f5196de2
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.35:5212/login
Username: admin@cloudreve.org
Password: NpeVtJJY
Application: Microsoft_[Edge]_Default
===============
URL: https://www.paypal.com/c2/signin
Username: 3350466089@qq.com
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.paypal.com/c2/welcome/signup/
Username: gjmsvip@126.com
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://mail.163.com/register/index.htm
Username: 19157340971
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://e.mail.163.com/mobilemail/inner2/home.do
Username: 19157340971
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.paypal.com/c2/welcome/signup/
Username: 3545293605@qq.com
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html
Username: m19157340971
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.124.40:31327/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://64.176.36.47:7800/da8bdd63
Username: idgb3e5u
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://64.176.41.244:7800/94d54044
Username: x8cwfgup
Password: 30170a1b
Application: Microsoft_[Edge]_Default
===============
URL: https://dash.cloudflare.com/sign-up
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://shandiansd.top/auth/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.35:81/Admin/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://705jg22642.zicp.fun/Admin/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://tieyunkeji.cn/09a71b91
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://passport.126.com/webzj/v1.0.1/pub/index_dl2_new.html
Username: gjmsvip
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.cosmotown.com/
Username: 3350466089@qq.com
Password: G#sxyLaPrGj33k$
Application: Microsoft_[Edge]_Default
===============
URL: http://124.156.216.232:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.exoclick.com/signup/
Username: 3350466089
Password: Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.amashiro.top/admin/login
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://bwh81.net/clientarea.php
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://fz.reimulm.com/4afe4965
Username: 3350466089@qq.com
Password: 21be09878ec397cbd44fb11511483407
Application: Microsoft_[Edge]_Default
===============
URL: https://user.taggood-5.xyz/
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://accounts.clickbank.com/master/create-account
Username: +86 181 5662 2714
Password: @4X!7BabFvjb4LBh
Application: Microsoft_[Edge]_Default
===============
URL: https://www.okloli.com/wp-login.php
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://etax.anhui.chinatax.gov.cn/cas/resetPwd/toResetPwd
Username: 953804
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.159.44.207:7800/87f1752f
Username: dcgjunjg
Password: bb9d7808
Application: Microsoft_[Edge]_Default
===============
URL: https://console.todesk.com/
Username: 3350466089@qq.com
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ctyun.cn/h5/auth/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://89.40.4.249:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.mtutuu.com/14943.html
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.luoligh.xyz/member.php
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://121.4.75.16/wp-admin/install.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ysz.reimulm.com/ysz1314520
Username: admin@admin.com
Password: 12345678
Application: Microsoft_[Edge]_Default
===============
URL: http://43.153.219.163:7800/587841ad
Username: 8zydviql
Password: fd4f3df2
Application: Microsoft_[Edge]_Default
===============
URL: https://amashiro.top:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://103.118.221.55/admin/login
Username: admin
Password: 123456
Application: Microsoft_[Edge]_Default
===============
URL: https://sm.ms/register
Username: 3350466089
Password: !EaCicimEaB9P8h
Application: Microsoft_[Edge]_Default
===============
URL: https://admin.exoclick.com/login
Username: 3350466089
Password: Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://demo.v2board.com/
Username: 3350466889@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://yunsuti.top/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://id.oppomobile.com/register.html
Username: gejinmiao@amashironatsuki.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.hahagal.com/2354.html
Username: 3350466089
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://121.4.75.16:5700/initialization
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://natsuki.ssk1.xyz:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://yypro.net/auth/register
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://47.242.247.237:54321/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://id.vivo.com.cn/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://wasv.top:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.kexuesw.xyz/0b050d5c
Username: 3350466089@qq.com
Password: 5218494fd4e88272bda3d30fa3d04d0c
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk3.top/Admin/login
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://live.yuanacg.com/member.php
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://shandianpro.com/
Username: 3350466089@qq.com
Password: gjm008822
Application: Microsoft_[Edge]_Default
===============
URL: http://ssk3.top/Admin/login
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://104.224.177.29:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.amashiro.top:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://lm.lmsq.work/xNKdnASFlM.php/index/login
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ganyu.live:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://yinghua.homes/wp-admin/install.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk4.top/wp-login.php
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://121.4.75.16/wp-admin/install.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://subscribe.receivei.com/
Username: 3350466089@qq.com
Password: gjm008822
Application: Microsoft_[Edge]_Default
===============
URL: https://bwh89.net/cart.php
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk4.top/index.php
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.208.199:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.zijizhang.com/audit/
Username: еђ€и‚Ґй¤®е…ѓзЅ‘з»њз§‘жЉЂжњ‰й™ђе…¬еЏё
Password: b7f4987b
Application: Microsoft_[Edge]_Default
===============
URL: https://juzicloud.org/auth/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk1.xyz/25a4b932
Username: 3350466089@qq.com
Password: ff6cfb1622d490bca068ee5d713700ab
Application: Microsoft_[Edge]_Default
===============
URL: https://passport2.chaoxing.com/login
Username: 15070493148
Password: 20190302121li
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/
Username: bdznnnsz
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://dev.233leyuan.com/
Username: gejinmiao@amashironatsuki.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://182.160.2.194:801/e2c6a69c/
Username: admin
Password: 1imCd3M9I54wlCC'
Application: Microsoft_[Edge]_Default
===============
URL: https://wangxiaomei.live:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://note.996flh.com/member.php
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://89.40.2.96:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/
Username: 181566227143@163.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://129.226.198.106:7800/7574c16d
Username: trzjidwe
Password: b5d44149
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ssk4.top:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://bandwagonhost.com/clientarea.php
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://id.vivo.com.cn/
Username: gejinmiao@amashironatsuki.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://qulingyu3.com/login/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://sso.godaddy.com/v1/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://yunsuti.top/
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://wangxiaomei.live/wp-admin/install.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.ctfile.com/p/register
Username: 3350466089@qq.com
Password: !ZGwaxKV_4drffK
Application: Microsoft_[Edge]_Default
===============
URL: https://juzicloud.org/auth/register
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://wasv.top/Admin/login
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://23.105.199.134:54654/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://yunsuti.top/admin00882
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.kexuesw.xyz/0b050d5c
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html
Username: 13755759168
Password: qq5224118
Application: Microsoft_[Edge]_Default
===============
URL: https://muniucloud.one/auth/register
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://accounts.google.com/signin/v2/challenge/pwd
Username: 3350466089@qq.com
Password: @gjm008822
Application: Microsoft_[Edge]_Default
===============
URL: https://accounts.clickbank.com/login.htm
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://dl.reg.163.com/webzj/v1.0.1/pub/index2_new.html
Username: 13755759168@163.com
Password: qq5224118
Application: Microsoft_[Edge]_Default
===============
URL: https://www.yinghua.homes/portal.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk1.xyz/wp-admin/install.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://admin.dpweixin.com/sign-in.html
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.vikacg.com/sa/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://129.226.216.74:7800/804c5f59
Username: irf5qtym
Password: d3f7cdfc
Application: Microsoft_[Edge]_Default
===============
URL: http://43.153.219.59:31701/4f0b1743
Username: 0zuuuggt
Password: a2687e86
Application: Microsoft_[Edge]_Default
===============
URL: http://wasv.top/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://note.996flh.com/member.php
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://onevpshosting.com/cart.php
Username: 3350466889@qq.com
Password: MvFE33tRYR_aatA
Application: Microsoft_[Edge]_Default
===============
URL: https://ysz.reimulm.com/auth/register
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.133.163.30/admin/
Username: admin
Password: admin
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk1.xyz:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.epicgames.com/id/login/epic
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://ssk2.top/admin/login
Username: admin
Password: 123456
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.50.1/Main_Login.asp
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://custweb.alipay.com/register/org/account/pwd/complete/entrance
Username: 9428
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://106.14.201.49/Admin/login
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.153.174.122:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://106.14.201.49/wp-login.php
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.xlz.plus/Register.html
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://39.108.128.144/wp-login.php
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://onevpshosting.com/cart.php
Username: й‡‘и‹—
Password: 6n6eBuqV5G_QMq8
Application: Microsoft_[Edge]_Default
===============
URL: https://cmy2.network/register
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://43.153.204.35:7800/3d2732a3
Username: 5idz3qgc
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ganyu.live/wp-admin/install.php
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://localhost:44337/login.aspx
Username: admin
Password: natsuki
Application: Microsoft_[Edge]_Default
===============
URL: https://qulingyu2.com/login/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://amashiro.top/install/index.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://freessl.cn/register
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://120.48.11.6:801/8f7bfec3/
Username: admin
Password: R1tZ3KFo6qa3tS\4
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk3.top/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.bidvertiser.com/advertiser-reg/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://129.226.198.106:8888/tencentcloud
Username: elqpkdds
Password: 53007d309562
Application: Microsoft_[Edge]_Default
===============
URL: https://suying222.com/auth/login
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://yunsut.top/c6c42e7f
Username: admin@admin.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://onevpshosting.com/cart.php
Username: gejinmiao@amashironatsuki.com
Password: _mUm7i2qTmwt.Nzgjm0088
Application: Microsoft_[Edge]_Default
===============
URL: http://43.154.186.114:29836/91d3d772
Username: 2d96xiqe
Password: 621b9f7a
Application: Microsoft_[Edge]_Default
===============
URL: https://dev.dcloud.net.cn/
Username: 3350466089@qq.com
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: https://www.csjplatform.com/
Username: gejinmiao@amashironatsuki.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/
Username: hjsjss
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://reimulm.com/
Username: 3545293605@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://19138033771.xnwl123.com/user/login.php
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ssk4.top:54321/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://app.currenxie.com/login
Username: 3350466089@qq.com
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://www.wangxiaomei.live/wp-admin/install.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://www.ssk3.top/admin/login
Username: admin
Password: 123456
Application: Microsoft_[Edge]_Default
===============
URL: https://admin.exoclick.com/login
Username: 3350466089@qq.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lisiku1.com/member.php
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ims.pinduoduo.com/
Username: UNKNOWN
Password: v6:F2_FvVyJUt!9
Application: Microsoft_[Edge]_Default
===============
URL: https://ims.pinduoduo.com/
Username: 18156622714
Password: v6:F2_FvVyJUt!9
Application: Microsoft_[Edge]_Default
===============
URL: http://43.159.44.207:7800/dd032383
Username: bhohp88x
Password: f8ee617a
Application: Microsoft_[Edge]_Default
===============
URL: http://43.156.6.33:7800/9de6cc55
Username: gi77cwfp
Password: eac4c3d3
Application: Microsoft_[Edge]_Default
===============
URL: https://accounts.google.com/v3/signin/challenge/pwd
Username: fenganggei@gmail.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.tmhhost.com/login
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://216.238.66.146:30692/c2ca8688
Username: 1v5ykw8g
Password: 77ef9d93
Application: Microsoft_[Edge]_Default
===============
URL: http://216.238.66.146:30692/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.35:5212/admin/user/edit/1
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://demo.kodcloud.com/
Username: demo
Password: demo
Application: Microsoft_[Edge]_Default
===============
URL: https://login.microsoftonline.com/81b34f1a-d0ad-4dfd-9a4d-5d44e3222037/oauth2/authorize
Username: jinmiao@leoblue.onmicrosoft.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://caihong8.top/6205c9ea/
Username: 3350466089@qq.com
Password: 7b9e9c8dd37389b2b8751a2ef66d2007
Application: Microsoft_[Edge]_Default
===============
URL: https://my.vultr.com/
Username: ganyu2021@ganyujc.top
Password: @Gjm008822
Application: Microsoft_[Edge]_Default
===============
URL: http://139.180.145.218:18415/f538102e
Username: hb8bagob
Password: ff18bdc6
Application: Microsoft_[Edge]_Default
===============
URL: http://139.180.145.218:18415/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.35/admin/login.php
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.36:11255/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.36:11255/42fe97d5
Username: ylxou8nk
Password: 9b43b003
Application: Microsoft_[Edge]_Default
===============
URL: https://sms-activate.org/getNumber
Username: m19157340971@163.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://sms-activate.org/
Username: reimulm007@foxmail.com
Password: RYTS6dNQa7c!Y9e
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.99:38857/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.99:38857/b6e57176
Username: tyu1cxo9
Password: e13a607c
Application: Microsoft_[Edge]_Default
===============
URL: http://65.20.81.60:38025/c5eb3d0b
Username: 7zvbjlcm
Password: 52f7428e
Application: Microsoft_[Edge]_Default
===============
URL: http://45.76.183.154:23862/4443845b
Username: iuqd5q0d
Password: ced11529
Application: Microsoft_[Edge]_Default
===============
URL: http://139.84.171.169:28909/71670460
Username: jbxqcpwj
Password: c8a2c424
Application: Microsoft_[Edge]_Default
===============
URL: http://139.84.171.169:28909/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://45.76.183.154:23862/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://65.20.81.60:38025/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://141.164.57.229:41086/2e5488df
Username: gzq33ypf
Password: 0cdf481a
Application: Microsoft_[Edge]_Default
===============
URL: https://account.protonvpn.com/signup
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.99/install/index.php
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.99/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14:32084/ead80d9d
Username: @gjm00882
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.98:22632/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.35:8000/natsuki
Username: natsuki
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://xiaolang.click/fd1dea97
Username: 3350466089@qq.com
Password: 6639270d1f6db80dda9a86bf70779bad
Application: Microsoft_[Edge]_Default
===============
URL: https://login.microsoftonline.com/common/oauth2/v2.0/authorize
Username: jingshu@leoblue.onmicrosoft.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.98:22632/2d09f956
Username: 9mcf9bmc
Password: fcf37451
Application: Microsoft_[Edge]_Default
===============
URL: http://payy.lmsq.work/admin/login.php
Username: admin
Password: 123456
Application: Microsoft_[Edge]_Default
===============
URL: http://117.78.6.14:5000/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://memberprod.alipay.com/account/reg/regComplete.htm
Username: gejinmiao@amashironatsuki.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://auth.alipay.com/login/homeB.htm
Username: gejinmiao@amashironatsuki.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://8.210.232.175:5000/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://jc.lmsq.work/login
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.lmsq.work/natsuki00882/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://yd.lmsq.work/LM/Login.php
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://lmsq.work/wp-admin/install.php
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://zfxt.lmsq.work/Admin/Login.php
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://v.lmsq.work/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://etax.anhui.chinatax.gov.cn/cas/login
Username: 341723200308087236
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://139.180.191.144:36516/abe5c74d
Username: vma81naa
Password: f32d968e
Application: Microsoft_[Edge]_Default
===============
URL: http://139.180.191.144:36516/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.244.223:25411/f7a12005
Username: 0b5wqfbs
Password: 01cb0f5a
Application: Microsoft_[Edge]_Default
===============
URL: http://45.77.244.223:25411/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.18:5000/
Username: и“ќжњ¬
Password: liao2023
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.19:42103/8e008168
Username: v4wonrjo
Password: 2e351c45
Application: Microsoft_[Edge]_Default
===============
URL: https://www.1342050.com/
Username: 18156622714@163.com
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.1342050.com/
Username: natsuki
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://www.gtloli.gay/member.php
Username: natsuki--0098
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://8.218.57.50:7800/e11f69c2
Username: dm7bth5a
Password: e5cf00d8
Application: Microsoft_[Edge]_Default
===============
URL: http://139.180.158.130:7800/0a224bfe
Username: yofde51a
Password: b941e757
Application: Microsoft_[Edge]_Default
===============
URL: https://wz.kuroneko.monster/
Username: 3350366089@qq.com
Password: a2a3bca00662dbac87b0d71569500cbf
Application: Microsoft_[Edge]_Default
===============
URL: http://139.180.158.130:888/phpmyadmin_833ef60964f86a28/index.php
Username: mon
Password: mon
Application: Microsoft_[Edge]_Default
===============
URL: https://kuroneko.monster/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://login.microsoftonline.com/common/oauth2/v2.0/authorize
Username: natsuki@ikuroneko.onmicrosoft.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.18:5000/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://tieyuankj.com:5000/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://openid.13a.com/register
Username: natsuki12adsds
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://sms-activate.org/
Username: 3350466089@qq.com
Password: @Gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://121.4.75.16:8888/tencentcloud
Username: elqpkdds
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ui.ptlogin2.qq.com/cgi-bin/login
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://mp.weixin.qq.com/advanced/advanced
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://xui.ptlogin2.qq.com/cgi-bin/xlogin
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://pay.lmsq.work/admin/login.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ss.lmsq.work/
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://payy.lmsq.work/admin/login.php
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.1/Main_Login.asp
Username: admin
Password: gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://login.live.com/ppsecure/post.srf
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://lsptu9.com/
Username: 3350466089
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: https://ziyuan.baidu.com/login/index
Username: 18156622714
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: https://login.bce.baidu.com/
Username: 18156622714
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: https://openapi.baidu.com/oauth/2.0/authorize
Username: 18156622714
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: https://pan.baidu.com/s/1z1z685XyuxutKKxzbxwBYw
Username: 18156622714
Password: 123456789@q
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.32:10349/7742c612
Username: mbjps4us
Password: e70d6f41
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.32:10349/bind
Username: 17394626570
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.50:5000/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.2/
Username: root
Password: password
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.1.1/cgi-bin/luci
Username: telecomadmin
Password: nE7jA%5m
Application: Microsoft_[Edge]_Default
===============
URL: https://myaccount.openvpn.com/signup/as
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.50:2052/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://qh.lmsq.work:2052/
Username: admin
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.50:2052/
Username: и“ќжњ¬
Password: 2023liao
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.39:7800/f3838722
Username: wifwq6jx
Password: 6636992e
Application: Microsoft_[Edge]_Default
===============
URL: http://192.168.2.39/98c31420
Username: 3350466089@qq.com
Password: b23784d8ae2d102040f0917cd392c6bc
Application: Microsoft_[Edge]_Default
===============
URL: http://ruanjiangjm.lol:8880/
Username: 3350466089@qq.com
Password: @gjm00882
Application: Microsoft_[Edge]_Default
===============
URL: http://www.ruanjiangjm.lol:2052/
Username: admin
Password: admin
Application: Microsoft_[Edge]_Default
===============

    """

    link_results = check_links(text)

    for link, is_valid in link_results.items():
        print(f"{link}: {'Pingable' if is_valid else 'Not Pingable'}")
