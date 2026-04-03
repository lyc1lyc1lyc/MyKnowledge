


  

# 前言

哈喽~

欢迎大家来到**OpenClaw**实战手册丨淘金计划，希望本手册能够帮助你在变富/变强的道路上成长的更快一点。

  

在开启你的学习之旅前，请允许我先向你介绍手册的基本情况。

  

**1）出品详情**

  

**内容出品人：大瑜、****智****哥****、****新侠、所罗门龙虾算力服务商**

**内容整理人：淘金之路团队**

**手册出品方：淘金之路团队**

  

**2）学习建议**

1、如果需要**快速定位**到精确内容，可以使用快捷键 Crtrl + F/Command +F 的形式，搜索关键字/词，查找你想要的内容。

  

2、拿到**《实战手册》**后，先浏览左侧的大纲，做到每个板块都心中有数，哪些内容自己原来就懂，哪些是知识盲区？

  

3、本次学习过程中有出现疑问的小伙伴，首先看《**实战手册》**，若还是无法解决直接在交流大群里提问即可，记得带上标签，例如：#提问，我们会有热心的小伙伴和嘉宾为你解答所有问题。

  

**记住：每个带队嘉宾都是在对应领域有不错的成绩和充足的经验，遇到问题解决不了，不要自己瞎琢磨，直接提问。**

  

了解该项目的大概情况后，我们就可以开始跟着手册进行实操啦。

  

以下内容由淘金之路联合圈友制作而成，仅供淘金圈友学习使用。

同时也欢迎圈友们在实践过程中持续反馈，和我们共同完善，可以联系山玟 (Taojinmumu)提供意见与建议~

#### **最后，让我们提高执行力，点亮我们的淘金之路！**

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MjA1NTYxMWQ5YmFhYTllYzFlZTZiZWEwYTMyYjM0NzJfZm9xQUxRTm1vbExuSHRWV2l2ZkRMWFk2cDFDUm5Vc2NfVG9rZW46RUNvV2JJVXVxb3BvVWt4ZXp3OWNwRWlzbktjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

# 一、OpenClaw是什么？

1. ## 介绍一下前世今生
    

2. ### openclaw为何流行
    

AI助手这个词已经很流行了。

经历了Coze 工作流、mcp、manus、flowith以及后面的skill、到现在的openclaw，本质上是一个更智能的AI agent工具。

  

那么这个AI Agent到底有多牛？

可以操作你电脑文件、查看邮件、执行脚本、控制你浏览器，妥妥的24小时数字员工。

  

github目前已经有170k。

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjJhZjM0MjYxZjJmYjU5YWM2M2EzYjYxY2IwZDJjYmVfbVUwY2c3ODA3dGZiTzhhbWo0TmVmbWFEUjFJZ3V5aDVfVG9rZW46Q0t4SGJCc05lbzM5OTh4cWJlbGMwc2lBbm1kXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. ### 改名风波
    

  

刚开始叫Clawdbot。然后名字和claude很相似，被迫改名Moltbot。

  

Moltbot 名字刚挂出来，又发现不够清晰 / 容易和别的东西混。

  

最终改名为openClaw。

  

3. ### 和prompt、以及skill等工具的区别
    

  

这个对比图，讲的很清楚啦。openClaw就是你的手机、skill是里面的一个应用、而prompt就是你发的一次指令。

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=Mzk2YzNmZWJkMGZiMzU2OWVlZjMzODcxNzA4ZmIxYmRfQ3VjcmU1Wmlqd3hPZjNFcDJldnpKWXdCQW9HTEpMaE5fVG9rZW46WGt2U2I2RGpzb0l2QlJ4TGx2QmNtMUpWbnViXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YjRhNTFlMDkyZDE5OTlhNGVjMTU4ZDliOWMzYWUzMzRfVUFjMkFaOHFFTU0xZFo3TjdPRjhqME5KdlVJRWtmd2RfVG9rZW46RHp1VWJrUktJb2tzaWN4MzBvWmNMbGpQbkFlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. ## 如何安装与配置飞书
    

openclaw的安装各种问题，所以咱们只推荐mac 和腾讯云的安装。（win不建议）

本次教学内容以原版openclaw为主，win可以通过minimax智能体辅助安装原版（可帮助电脑小白配置好依赖环境同oneclaw），mac可直接安装（见安装方法） 另外可选用oneclaw（独立运行但同配置文件）或autoclaw（独立运行）

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NGI3MTcwNTdkNGUxZTJlZGZkODkwOTVlZmI2MzRhOTNfMDk0ZFM5ZzZCOTZBS1NsczYyVnJMbFV3RTlxVjAwd1dfVG9rZW46SFJFSWJIcXVDb2NtWml4OVNUb2M5UkRzbnhmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

1. ### 前置条件
    

1、你需要有一台windows、mac、linux设备（或者云服务器）

2、你需要有付费大模型的API key，可以是GPT、CLAUDE、或者kimi API

3、飞书账号：

先拿到飞书的**APPID和APPSecret**【！！！！】

我们大部分人都要用飞书和龙虾进行对话，那么提前申请一个飞书的APPID对后面的安装至关重要。具体的步骤如下：

进入飞书后台，开始创建应用。地址：https://open.feishu.cn/app

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTBkNjJkZGFjODM0NjQ3M2I2YzU5ZTQzMWQ3YmIyMmVfaWFPRXo2V250Slc2WGtvWUw3andha2xBWUhEeHBVVDlfVG9rZW46Vkx2bmI2dk4xb05zd1p4VEE5bmN6MmRpbllyXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

创建成功后，点击“凭证与基础管理”。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTUxZDJjMDRkNWI1OWQxYjE3OWE5ZTNlNzdhYjc1MThfS0FmZHV4UG5VazFSRmtkZndoQzdGOEsxOURGVHJSY2hfVG9rZW46TkNyTWIyY3VXb3BXdkl4SWRMTWNuZkNqbnFmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

获取到：APP_ID 和 APP_Secret。保存起来，我们后面使用。

**顺便把****“机器人”****添加**（否则在配置中总是报错）

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NjE3NjI1ZDk2OWQ4YjFjMjdhMzNkZWNmNTExZGQ1ZWVfY3B3b0JxQUNVbk1KOWxGWW9JZGJjdzl5MUw3dHBqemtfVG9rZW46QUFIY2JOdGZab2g5NFh4WVlYOGNleXNUbnJoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NWIxOWI2YmFlMGUxYzVjZjViMGU2N2QwNWQ3NjVjNTVfZzhVMnFmVTlxdmF1Z2FwbDdhNDE2VUNJWkpWNVBOTGZfVG9rZW46SEhWV2JXZmtGb0ZhUjR4bHR3ZmNxOUU5blhmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. ### 智能体安装
    

3. #### minmax智能体
    

现在很多大厂都出了智能体帮忙安装openclaw，大家在安装的过程中，可以随时问智能体协助安装，尤其是windows小白用户，智能体能非常好的解决windows各种环境依赖和兼容问题。

再结合咱们后续安装方法，可以解决大部分问题，这里推荐先安装一个minmax的智能体，后续有问题都可以直接问。

https://agent.minimax.io/download （海外版地址）

https://agent.minimaxi.com/download （国内版地址） 进入官网点击右上角下载按钮

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NDYxMzk5MGE5ZWZmZTlmOGRhNTAyZjc0Y2I3N2MzM2NfbFVwTURzZWpMYjRVdFdSUFlWcXAzWThFVW1vUXFGN0pfVG9rZW46T1FXMWJFWmNnbzBvZnd4ZTQ4WGN4V2Qwbm5iXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

选择合适的版本下载并安装

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YzdiZjVjODQ2OGQyNGYxMThiOWFlNjU5NzcxMTAxZmRfajBCT2dHYm9hSVcwVnF3WktHU0UyRW9vNlBQaE1vSDFfVG9rZW46V0p1SmJnRVphb2d0eUZ4V3hlOWNpVWxMbnhlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

在打开的界面输入“帮我安装openclaw”

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=M2U3MTU2M2IzOTU1M2E2NDIwZjU5ZDQyOGIzZmQzN2JfQ3hsZ2J0a0UyZkFlRUhaNkk5VVg5S2RWR0pIUW5pOG5fVG9rZW46U0ZZOGJuWDd1b2VsTGp4NXA0N2NJbUkwbmpnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

中间过程有一次区域选择，直接输入“China”

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MTBmNDM5NDdmZmQ3OGJjZjMxZThjMDQxNzYzMDZmMjRfQWpQR3IxOVRyN2xOZTE2eUJ6eFF5ZGxZMzRVSVlBYjVfVG9rZW46VGdSQ2I4RkVjb2FrUEZ4ajRUamM4cXowbmxoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

**到下面这一步说明已经安装好了**

**（如果安装过程中出现提示你安装openclaw-cn版本一定选‘no’，不要安装）**

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=Zjg5OWE0NTExY2IyMWZiZTUzY2ZlOWY0YWJjNDg2NTdfVGFzdDJDUjJqN3FrVDBKcDFIQ2lSNXEzQnUwYUN6ZVlfVG9rZW46STFGSWIwU0RLb3h4VnZ4ZmdTM2NhNDQ3bldiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

**在cmd中输入“openclaw -v”可以看到openclaw的版本为‘2026.3.2’**

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDUxOWFkZGVkOTYwZDJmZDA1MjE3Y2JmYjg1ZWFlMzBfUmJVcVc4U2U5SEtXdnFZMHFnR2gwbW9NM2JUSFk4amxfVG9rZW46UlNmdWJ2Tkhsb1plSTN4NEJhWWNneDZ0blJlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

在安装完后的配置中： 如果大家继续使用minimax账号可以使用上面对话框中的配置指令。否则，**直接跳转到2.3.2章节使用onboard安装。**

  

2. #### **Oneclaw安装**
    

登陆https://oneclaw.cn/ 根据电脑系统下载合适的版本

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2I0MThiNGVhMWY0MjAzZjM4MTFlOTMyNjliMGQ0NzZfQmg5OExWN1REWFF6cTFTQ0x6clhRNEdCT2tDMDdOSDJfVG9rZW46VGQ1SmJjMHVBb1NieXZ4ajlSM2NoOHd3bkdkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

下载后点击安装

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NzJlNTRiODMwMTA2MGY2Y2E4NjQ4YTg0YmZlNDljYThfblJMM0cxY3c3WGt3VVdXdzhwQlJTS25QNnBEbkZnb0hfVG9rZW46TGQ2d2JRWG1ob1NBTXZ4Q01CamM4RTNFbkJkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=M2YyZDY0ZTE1ODY0NDRkYWZhOGZiZGUwNjE0YmNlZDdfTjhSZ0d4RnZScTRWVHFPRXRreXRNY0phOGx0VTlPT0lfVG9rZW46V0IxZmJ2Vjgwb1dKRmp4Y241VWNuejZTblNFXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

进入配置服务商界面，**kimi**用户一定注意**区分选择订阅账号或付费账号**，**其他模型或第三方选自定义**

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MjRjOGU4YjI2MGJjZWE3NjIzNWJiMTZmODFlNzVhODVfaEc2QXowMTB2Y2pyZDc2SVdWa1NMeVBuNDdPZkkxaTNfVG9rZW46V1pUNWJsd3J1b3l1Tnp4bzJVdWNpcWhFbjdmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

在预设中没有找到模型没关系，把**服务商接口地址、key、模型名称填对就可以（不要填v1会自动补充/v1**）

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NjRhMTQ1NTUyZjUwMGM1OWJkZWYwNzRjYzQyYjYwYWFfcDlQUWFMZW03cm9TeERsMVNyYXNiRlNlNEVJbnVKNGdfVG9rZW46T1J5d2JVM214b1R0NGF4dkdGUmMweVVCbmJnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

填完后点击验证就配置完成啦！

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YWRiMWY4MDEwYmYzOWY1MjgxNjY5NGZlYmYzYjY1MGNfaHZndDBtUHVxb2FOWlJTTmE5NXNsbXVjMlVJSWJZd0pfVG9rZW46QlY1dmJCV0IwbzVYVUx4Z25IdmN3Tlh0bnVmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

正式进入oneclaw界面，可以在**输入框进行聊天**，**模型、飞书在‘设置’选项**

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YjJlN2QxZGE3ZGNiMWU3MWZiNmE1ODRjMzMwNjk0NzJfaXg2ZTl1aWxGSXcxQ2tJc25SRXNac2k5VHdNUWExMndfVG9rZW46VksyZGI0RnBCb3JmYjd4ZzFBNmNRQkNkbm1hXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

配置飞书ID和密钥，**打开和关闭这个开关会重启gateway，这样就可以去配置飞书界面了。**

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NzlkMzNlMWVmMjljMjJjZjI2NDY3MmM5NDRkZDU1MDVfbDQ2QUJaZVgzZ0ZXSnFkNTJUdE1wVDN6WUJDVWFDd1ZfVG9rZW46UnZBT2JIc1U2b2k2WFB4MHFuRWNwWFpGbk9nXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

3. #### AutoClaw安装方法
    

登陆https://autoglm.zhipuai.cn/autoclaw/进行下载安装

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MTkxNTM2YzQ5ZjBlYmE3NTNkNjBhMDVlMDEwMTBlYmNfYWJ6NlBQOTVtS1FaQjFhWU1XSkdPSFd6WjZHbXRYdnZfVG9rZW46VlR2V2JLMjhEb3Z0c2x4WDBabGNKY0xHbmJoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=N2VhZTk1NzU0OTRhYTc5MmFhZjkyY2Q1Yzg5OTk1NjNfRnh1OHkxNDNKZEU1OXFzT0RYNWFIYXF4N09udnJTWFJfVG9rZW46SnVjRWJiSkVIb0VjUll4S2dPSGNkVUlZbkRkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

用手机号注册登录

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YWZmMzA0N2M0NGFkN2JmNzMxOTdjZmY5MTYxYzE5NzZfaUF2aVoxcUdGazBzVTNHT1A5NU5URXJ3UGZCVnBzV0tfVG9rZW46WDQyZmJHaWZSbzRlSHZ4OHRiWGNFbDFPblBjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

配置第三方模型与飞书的方法，点击进入设置界面

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YjU0NjgzMTY4M2MzYTg5NjFlOWVkMzUzNTM5MmNiNzVfN3RTM1AzaTdTdUd0NlUyUm5KWTA1c3lxQnZEemZpR1FfVG9rZW46Vndpd2JzY3ZVb0Z6ZnR4dUFheGM0RGttblZiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

在'模型与API'中，选择'添加自定义模型'

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTQyYWYwZjZlYWI5M2I5ODgwMzA0NGYzMWNmOGNjN2FfajJIMWJ2Y0NUdm1ySzUyYlZOaWY4a004Tk5tcVhIN09fVG9rZW46QmdDM2Jtc3BXb1I3dzh4b2FEeWNwUmFubkhlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

依次添加API_key、URL 、模型名称等，连通测试一下然后点击添加

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MjJhZDllMDExMDdjNTMxOTU3NmNlMmQ2MTk5N2FhYzRfY0xuVVpDZ0E3OWRvWkhwd29vbEdzN3kxRnNwNDhoVUNfVG9rZW46VEw5S2JwaEFjb0p0M214eEppNmM2bTh3bkFjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

可以选择默认模型，一可以在聊天框中切换

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NmQxM2FiMGU4Mjg3MmU2MzFhNGFmNmVkYmFjZTA5NzJfbFVialpNSkwyRDkwR3ZYQUk0TVFHcFQ5dDd2dktpdUdfVG9rZW46UTliU2JLRUVmb2FHbzd4b0hGOGNKdm9ubnpjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MjhkOWFkN2NkMDc2N2E4ZWFkMDZlNTUyNDQ3NzI1NTZfZTNBbGJKVGZzMlIwTjd6WkFWdXNDOFhGTVp0QUJvdEZfVG9rZW46UUExWmI2M3h2b0tEMU94V2NOTGN4NGNsbkFkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

配置飞书：Mac用户在聊天界面选择'一键接入飞书',中间有一次扫描登陆飞书，其他全部为自动模式

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NzEwNGM2ODIwMmQ1MTA5NTNmMzAyNWQ2MWVkOGZjMGFfbXFOWTlDODdERXNXUHNONXZHRkFGMWR3ZXVBWmhYemFfVG9rZW46VlhrUGJBTGFHb1MxNmF4eGVJZ2M3SHNvbnpmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

配置飞书：windows用户在设置界面中选择'IM频道'，点击'添加频道'或'+飞书'按钮都可(选其一)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=M2MxNDE0MzU1M2QzZTQ2NWUzMzcyNTdkZmI3NmQ5NDJfaUlQOWc5eDk2cEI1dmxzaDloWEtoTXh1TDVDZ29zMFVfVG9rZW46QTZwVmJ5V2tMb2xhZ294ZWJPd2NLcXdRbkdoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

在'APP ID'和'APP Secret'分别输上我们开始准备好的值后点击保存

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MDY5ZjFmZjZmNTQxZDBjODNhNDE3MTM5N2VhZDA3NTdfa1ZZdnpMVGdOb2hmSmhLOTBGc0dUSnVuMEh5a3J4aWlfVG9rZW46QkQ4b2JQN25Lb2FYRTZ4Y2VqaWNDRVRQbk9kXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

同上

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NjIzNjZkOTFkMmE1MzJlOGQ4NWU0MGE4YWQ3ZGJhMzRfa0lOYVpZaDM2VFhTTXdTaVBVY3huTHBzMnpyazJ1VkhfVG9rZW46TXo1bGJ4cE5Eb2o2Qkp4RU9taGNJWTR5bmFkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MDk1MDM4N2M5ZmY1OWU2NzJlMmI1OTM4NTEzZjIwOGJfblFmd1lrWlBEeEQ0WU43ZEZpTzFBODQ1QmIzOG5CUGFfVG9rZW46WDJNUGJaM3Nyb3RKQlV4QmkwTWN3YWdGbm9nXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

3. ### mac电脑本地安装
    

4. #### **命令安装。**
    

  

安装方式很简单,执行下面命令就行了。

  

但是前提必须是安装了git、nodejs（22版本以上）macOS版本12以上。

  

mac是默认自带的git，先看一下有没有nodejs，在终端执行：

```Plain
node -v
```

  

如果是‘command not found: node’或者低于“v22.22.0”版本，nodejs要自己安装：

```Plain
nvm install 22 
nvm use 22 
nvm alias default 22
```

  

装完验证版本，显示“v22.22.0”就可以了

```Plain
node -v
```

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NTYyZWU1YTZhMGE0NjFhMjZjMWM4MjkyN2Q3MDU4ZDZfdHRoQ1hSUFVaaEFuTEMyVTVkWmZxNllUdmhKdlpCbXZfVG9rZW46VEtuYWJzNFgxb1dHVzZ4VHIxNWNXeXo0bkt5XzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

接下来进入正式的安装教程：（使用国内镜像）

```Markdown
npm install -g openclaw@2026.3.2 --registry=https://registry.npmmirror.com
```

  

这个时候就开始安装了，安装完以后使用“openclaw -v”验证版本为“2026.3.2”

```Plain
openclaw -v
```

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MGFiMGZiMWU0MDI2OWRlODk1OTYxOTdmNjU2MGYzMmZfazJJbjhRTzJQWW1MaDdIV2tiSjEyWDRLckdJQU14QjRfVG9rZW46REdnMWJrZktZb2t6TDd4MURmVmNMM2h1bmllXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

新电脑如果没有Xcode会遇到这个问题，执行

```Python
xcode-select --install
```

会弹出一个窗口，下载、安装成功过之后，

接下来继续安装

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTQ1MDQwNTgyMDk4YmYwYTkyZGMwYzQxZDA5MGE3ZTBfdXRjNmtxT3ZaRFNDZXo0bkMyWVRud1hjVUNEdnZKa1JfVG9rZW46QU93dmJXUlB1b215Nk14OXp5aGNYQmtRbldoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. #### Openclaw 配置应用
    

继续openclaw的配置，在terminal或者powershell中执行：

```Python
openclaw onboard --install-daemon
```

会进入与我们下方一致的安装界面

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ODk3MzU2YWIyZDc4NTc3ZDk4NmU3M2E5OGFkMjhiMTJfNHRCWTBOWkFNT1pyZnh4QkRlSHVicXZUV3pCdmNXRlZfVG9rZW46T05XN2J4dmc3b0Y4SlV4RG5TcGNtbTNxbjNnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

这里必须要选择**“yes”**。下面的选择第一个。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTA3MDUwOTZjYWE0YmMzN2JlZTY4ZDdiMGViMDczMzdfOWtFc1E2c3lQVVBMNlF1WUVqQkhvdHJjSEIweFZySG5fVG9rZW46RzlQOWJuSFdQb3A3V2d4YzRLdmNuS1Nybk9lXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

这个时候会提示你选择模型。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTAyYWNiZTkxMzU1N2M2ZWU2MzlmODIyNjFmMTc2NDVfSGZuTlgzcVFEYm04SVNnR0xhamJEZzZaUEtQelZJdDZfVG9rZW46Ulc0TGJkb3NXbzJxSWF4QUFkUmNXb2E5bnhiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

这里可以根据大家的情况进行选择：

1、推荐openAI和Anthropic（自行解决vpn问题）

2、kimi ，API。到https://platform.moonshot.cn/，注册帐号，获取API，新用户

  

我这里选择openai，通过GPT OAuth来验证。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTVkMmY4NmE4NTdhNmI0MjJjYjU1ZjJlZGViMDZhYWFfT0dyN2Y5NmpBUXpVZFBYeUc5UVNjZ29TUVpQU2ZaenNfVG9rZW46SFRkb2JCWnc5b2thMWp4ZFZDY2NrTEU1blNjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

授权成功之后，提示选择模型。

下一步选择：channel。我们选择安装飞书插件

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=N2UyNmE5YWMzMDA2NmIxZDE5MGEyMGEzZjY2MWE1MmJfZXkzMnJrQXIxZGxxR1Z3QTJCaENVejFnS3BlYjN5MmlfVG9rZW46RnViNWJQSU9rb1ZhNUp4S2ZqUWM0d0ZIbno3XzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

安装完插件以后继续

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YjQwNDNlYmMzM2M0YzJhYjhlMjE5ZDNjMWY5M2E4M2FfWHRvTDdVVExlZk9vT1J1b2FRWTd3aHFuRm43TkJudG1fVG9rZW46V2FYV2JXNGY1b1VMS094elljaWNaNkVVbnRkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

输入飞书的App Secret

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGJjYzAxNjQxYjZkZDJhMDQxMDMxMjkzZjMxMjk5YjFfRktmbmJvOGZzem1nRUl6T3k3UnRuZXAyYnNaRlFnRmhfVG9rZW46T25MSmJJS0Jlb3pkbHJ4d29DeWNKdDd0bjNXXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

输入飞书App ID

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTUzODg0MjY2YWZhOGJmY2E2ZmU5ODQwYjQ1ZDlmZTVfZmIyVlV6anVZTGNBRldack03M0dYYkwzSXR1WVY2aFpfVG9rZW46TUVVUGI4MTRMbzViN3F4M05QdGNqYTV4bm9oXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

接下来选择WebSocket 和Feishu-China

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MmNiMDJiZjg2MzY1OWMyZmMzMmIwYTBiZWVjYzI4NjZfU0gxNUtocnhQT1JuMEVKSkRHaVBYdXVCbmJ2SVBnYjJfVG9rZW46T0RKb2Jja2Jkb200blB4REx2ZWM0ZEpOblNiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjM0ZjUzY2QwMzA1NWU1OWY5MjgwNTMwMmNiNWQyZjVfSlEwMjFxOVZQVWpLVXhicU5lalM2RG9NQUxGZWR4bm9fVG9rZW46WGdieWJxU2JxbzZ2UGl4Q3lBb2NYRGNNbkJjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

这一步是验证步骤，选择Allowlist

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjNjMDdjOGNkMWJhMWUxMDIwYTBjMWRlMmRkMGNjNjZfOXVyazZDN3BvNGRnT1hHSlhQdkVVcktQcjlNRkdWT2dfVG9rZW46U3ZhV2JiSzQ1b3dtOE54aTVybmM0b3hRblZiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

接下来是群聊设置可以输入群号或者回车先忽略（暂时没有群的话）

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YzRhODFkZmNjYmY1Y2FlYzk5OWIxZWNkYzE4MzE2MzNfNnR2Rm1TOFU1RHJnVURzaVF6b3ppZHZIOHlYUHhlaWlfVG9rZW46Qmd3cWJSdHg0b3NtdU54MEdRS2NTaFM5bkNmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

增加搜索链接（新版本才有，旧版本没有可以忽略，测试版本 2026.3.13） 都是需要key的，没有可以直接跳过

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDQ1NTIyMTZkMGExMGRhNDE3ODY5MTZkMjhhODQ3MzRfOTZZS2FJbTlXQkwyMnRqUzVqMEkyOGFMbmFSMlgwYTlfVG9rZW46VEZPUWJsclczb2ZHQXp4OUd6eGMyRXMxbnhiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

接下来提示安装技能：Yes

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDAxN2RmM2I3ZTU1ZTMyMDczOTJiYWQ5MWVkNDNmMGFfVVhwdGdrd05teUE4N0w4MGp3QWM3YnRDQWN5Vk9yWDhfVG9rZW46TDREYmJ0ZHBJb29maFV4anppamNSbTNYbmplXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

具体的技能类目可以先跳过

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NTQ4ZmZjZmZhZWE1ZTY4MzExMzE2MzNiMGM4ZTVmMTJfV0F1NFlGdk0zaldldVdNUFdzVHd3bVhQdjhTMldla1VfVG9rZW46VzRGd2I1aVpMb2lNbXJ4RmZTeGN4R081bkJkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

接下来都是no

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=Zjc2MzU4OWJkOWM2MzhlYzUzMmYzZTgzODcyYjkzNDZfeFRVeWJLYXB0ck14UllpclhGZHVkaDVKTkdVSDdkQ1FfVG9rZW46SjkwZWJLS044b3lnT1V4WFpFb2N0OEdabnJkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

先空格选中，然后回车跳过

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NjNmMTJhNDM2ZjQyNDExZDVkNDU3NGQ4MzIxMzNiZjRfN0xlcnZ5MW1ZOFZ5c0FQMWUxRndkUTgxeEpwdGszTHhfVG9rZW46WGNUZWI3RWpvbzJIQ1l4cTNHUmNneHB5bmtoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

接下来就可以聊天了：选第一个是在终端窗口聊，选第二个是网页窗口（新手推荐）

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YWYxY2JlMWExNjQ2YjBjOGI2YWQ5YjQzN2RjNzViYjhfUHlxQUcydmcyWGpzb0hPbWpvM3dLVGc0bEQxWHJiRDRfVG9rZW46T09nMmJ0Tld4bzNCWXZ4N1FnZWNKZG5NbnpmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MWY3ZTE1MWExNGQ1NDczZWJiODQ0ZGIwM2I4NWE5YjZfeHhLV2F0c0xKbHVtb0pSbkpFcUV0aktpd1B4QjZndmdfVG9rZW46T2p3VWJwcE9Qb05Xa1h4SFg3WWNJSjR3blFkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

---

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MWRlMzU1YjNlMDg1OGEzNTQwOTM3OGM2YjBmNWM5ZWZfdGdmMFduRHBsUFRYRFBlRWVSdEVkVnVDeUNBMmRpQVRfVG9rZW46QjBraGI1OU83b1JDQXB4Z3owS2Nrb1A4bmpkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

4. ### 腾讯云服务器安装
    

5. #### 云服务器安装
    

腾讯云服务器，现在也可以进行部署了。

https://cloud.tencent.com/act/pro/lighthouse-moltbot?from=29437&Is=home

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YzllOTBkYTFjM2RkMDlmMDdmOGRlOGUwMmFiNGFjOWZfQkJxU2syS2k3WGRZSFJBSXhnazRzT01JNXIxczRQUW9fVG9rZW46WmVmR2JEVTY4b0lIMHB4aHQwbmNlUjI0bmxkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

如果你还不确定你是否要使用，可以先选择20.7元一个月的服务器。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YjNiZWZlMDY5ZWNjNGFlZGQxNzljN2Y2MDY2NTMzMGZfY1pwa1JGblhnUDBJdHZzVVNqMlNRSTMzNXpjbjNOMnRfVG9rZW46QkxmbmJMRjI4b3JnaUp4clhwUGNvbU9oblZoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

点击“立即购买”，购买成功进入控制台，点击对应的“ID”即可。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWM4ZmMxZjJkNDk5YmE2Y2ZkZTU4N2YwMTY5OTg1MzNfWXB5MHhBYW1zaTZ0dlpYM0lFTFEyRzF2TDlEOHZVTHpfVG9rZW46WHI1emI1WWYzb1E2a2l4TkVrbmNFbkxtbjBmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. #### 如何配置模型
    

  

因为云服务器，配置交流工具相对比较简单。

接下来进入页面是这样的配置，点击**'登陆'是登陆终端**，点击三个点选择**'管理实例'是进入配置**

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NmM0NmIxNzgxYzQ2MWY1MzFjNTZlMGM2NGZlOGZhNzhfYTRPSkgwU0NzR0V6T1JBZ2xXQXNEenljU3l1Vkg2ZGpfVG9rZW46UG54emJkTldYbzQ3dWZ4VnJlVmNUVDBKbm1iXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

点击**'实例管理'**后选择**'应用管理'**就看到我们配置界面了

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YmU3N2JiZmY1Mjg1YmY1OWJkZDgwOTUxMzY5ODBhNDBfUjBJRWtONGFBa3VRTE51MlRIVVJPVEFDUWZERTQ3RzdfVG9rZW46VzBFeWJoWXpqbzVVVDZ4dlpHR2NEYTdXbmZoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

模型配置跟前面一样，关联飞书就更简单了，channel配置选择飞书，输入APPID和key。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjIwNjcxN2QxODAxZmUxMjk0Y2QxNWJlYmExYjY4NTdfS1lWcnRMVkRzN0tHajZXRmVGY1dvQjBEdzE1NjJxSjlfVG9rZW46WG5CRmJZQlE1b2VOd1l4WXFOVWNpbGRnbkdlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

**在终端使用'openclaw tui'可以测试配置模型是否调通了**

```Plain
openclaw tui
```

**如果配置的飞书长链接一直没有生效，在终端执行重启**

```Plain
openclaw gateway restart 
```

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MDYzMjliYjgyNGYyM2MxMTBiMGQxZTQwMjhjNzQ1ZDVfd2Uydm5sVXY5RXM3MUJ1OE85OG9oTjM4Q3dLMmg5Y1lfVG9rZW46UzVoUmJaVDhob3pjWjZ4YU50NWMxaDVKbjdlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

**详细的安装教程见这里：**

https://cloud.tencent.com/developer/article/2624003?from_column=20421&from=20421

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWQ5YWY4OTlhZGIyOTA0Y2U5ZjNmNzMzOGMzZTYyNjNfNkV2TTRDcUl5c1BlTzNyY1BFSjJVYUlHVDdGU09HVGRfVG9rZW46S3BodGJmZEJZb09tc1F4TFpheWNYZjZabjliXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

5. ### 别急，还剩最后一步----飞书配置
    

  

飞书对权限管控的比较严，在完成openclaw的安装之后，我们需要去飞书管理平台做下面的配置，才能在飞书中和openclaw沟通。

  

地址：https://open.feishu.cn/app，

  

配置权限管理。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YWYyZmRmNTEzY2Q4ZjA3NGQ0ZjU1YTczNjlmYjM4NmNfcXZYdEJ1WWFiWjVFeGpFSkFDZXpFSjVReldMMUVFeEtfVG9rZW46QmV5RmJVMG4wb2JGUE54em5lamM0eG1SbkZkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

这里进行下面权限功能的添加。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTFjYTVkZWUxYzNkMThhMjRmZWFkMTAzN2Y2NmNkOWNfQzBFaHNnT0kyOU14N0hsdFVDekZDR25YNjViWnRYeFhfVG9rZW46T3VoMWIwNFA5b1p6TnJ4WVBQeGNIRHR2bkdlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

当然如果觉得手动麻烦，可以直接一键导入。

```JSON
{
  "scopes": {
    "tenant": [
      "cardkit:card:read",
      "cardkit:card:write",
      "contact:contact.base:readonly",
      "contact:user.base:readonly",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.group_msg",
      "im:message.p2p_msg:readonly",
      "im:message:readonly",
      "im:message:send_as_bot",
      "im:resource"
    ],
    "user": []
  }
}
```

然后：确定开通权限。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MGViYjYxMTI5MWQ1ODEzYzI3MGE2NThkZWVkMmFkNmZfWHN0NUFlT1c5b0drTWVTSnNlMFBnaTlzSWRsbEN2QzJfVG9rZW46SVloS2JLWTZIb1ZsVEV4TWVCbWMzMDRBbnFnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

5）点击事件与回调。

tips：如果没有做第三步的操作，就会提示无法建立长链接。**（配置完以后一定记得重启）**

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZThiNDgxOWViZWM0YWZhZmVkYWNhMjQyODgyMDA5M2FfUWU3WWh5R3BnbzN1MFpwWjdDMDdsVHo5VGdtblA0alpfVG9rZW46VVpEZGJ4VnBNb2JUUG54NGZ0YWNvVkU5bmhnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

接下来，点击“订阅方式”。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=Mjc5Y2EzY2M2MDMxNzQ4ZTVjYzgxMzdkZDRlMzQ4YTVfREVpM0pNZ3JLMXZTNjQxZ05RTVlrZHMxcXpPZlRFd0lfVG9rZW46RVVRSWIzd3VGbzBUZkJ4TjM4TGN0bW1obklmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

点击保存后，接下来啊，再点击“添加事件”。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MGM0MjUxMDg3OWJjNjhhZjg2YzU2ZjEyOGFkMzQ2Yjlfd2ZTc1dMTkVidFhuYVl1Ykhaa2dIVno1RGhyaEhOWHFfVG9rZW46S0Q1TGJPSjJSb2prMHZ4NWtyT2NiQmQ4bkhoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

将下面的事件添加进来。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjgxNmI3ZTIzNzA0NzFmMjhlOWM3OWFhYjVlZDQ4YTJfUFJ6OVVQRU4yd2VlQ3ZadzkzWEJEdmxXU20zS2NKaHFfVG9rZW46T3pLN2JicGQ5b1JNb2h4ZjFUb2NaTFVLbmxjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

```Plain
im.message.receive_v1
im.message.message_read_v1
im.chat.member.bot.added_v1
im.chat.member.bot.deleted_v1
```

  

6）应用发布

点击“创建版本”这个连接，进入应用发布界面。版本一般是1.0.1，如果修改了就是1.0.2不断递增。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=M2ZiYjA5ZGQyOGU1MTRjMmZmZjQ0MzM0MzU0YjY0ZGRfQnMxRTdlMnJ5azFaZFV5d1lNbHE2YUd1QnN4T1pSaVhfVG9rZW46UlJRemJLdzhwb2RSZWx4T2plbGNFRkE3bjJkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

第七步：

打开手机飞书。点击工作台，点击添加常用，找到创建的机器人，就这样愉快的和newclaw聊天了。

这个时候就可以和机器人愉快的聊天了。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=M2Q1Y2Q2YjIzNTg4NGQ1ZTVlNzVlOGZiYTNkNDI2NDhfTENtdXRkRURoeFU5TmpPbTFOZHNtR0Q0UGJBODI2VDNfVG9rZW46VXlEQ2JWUVk1b1BLYlh4Q0tGemNmdzRSbkloXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MTE5MTRhZWI5ZmIyZmY1MTM5NmRlYjlkMjExZTg2OWZfeFR4Mm91N0d6YWpuTGxiSHRWUE9vYzl1NGVJNGVkNERfVG9rZW46S2xkaWI2Q2JRb0ExTk54RXNncGM0RDZ1bmFiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

拿到飞书配对指令以后复制最后一行到终端，回车一下就配对成功，就可以跟机器人聊天了 （openclaw pairing approve feishu XTXXXXXXV）

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NGU0NTIzMjZhODZmYmZlNjhjNTU5MWY3NTc2NTljNzZfUnl6b3p6Q1hnd3gwZHlYcE9TeG40UGx5Wll6QzRoRXNfVG9rZW46S0lETWJFQVJyb05hdlh4dGxwaGNGaW1TbkpiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

当然，如果报错，那么直接把错误复制过去，让openClaw自己分析即可。然后他就自己修复了。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NmNmYjM4OTYyMTcyODYwMTUxODk2MTQ0MWRjNTY0YjFfU20zTWV5UWszOTNGd0tNMDRmaDJZZDg1ZlN6aGx0UzFfVG9rZW46T0hwVWJ4TGk4b2p3VGJ4dU1nVWN5bXhwbnRlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

tips：能配置两个机器人吗？

（当然可以，你直接这样问openclaw，然后按照他的说明自己配置）。

不过，有个问题是，飞书目前只有三月份可以无限使用，但是没有确保一直免费体验下去。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2EyYjIyZGMzZjUxMDNjMDA3OGE1YzA1ZDUzYWI3YWZfTHdEeDFoaWcwc2tOWHRYQ3paRGlPWTZneGZvUERhOEtfVG9rZW46QU9ZY2JDZ0RpbzZERFh4YXFJMGN6aEFubkNnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

3. ## openclaw的常用命令
    

日常操作指令建议复制到电脑保存

```Python
# ================= 日常操作指令 (OpenClaw 2026) =================
#注意事项： 请只复制以 openclaw 开头的英文部分。
# --- 基础运行 ---
# 前台启动网关（测试用，关闭后程序就关闭）
openclaw gateway

# 启动后台服务（关闭后程序还在后台）
openclaw gateway start

#登陆页面
http://127.0.0.1:18789/

# 停止后台服务（如果遇到不好使了就停掉重启）
openclaw gateway stop

# 重启网关（修改配置后必做）
openclaw gateway restart

# 还不好使试试强制启动网关，用 force 模式，如果端口被占用了它会自动清理
openclaw gateway --force

# --- 模型测试 ---
# 进入终端对话模式（测模型通不通）
openclaw tui

# 查看当前模型清单
openclaw models

# --- 检查与诊断 ---
# 查看实时日志（照妖镜）
openclaw logs
```

4. ## Token焦虑怎么办？
    

很多人说国外要vpn，没办法订阅GPT、Claude这些模型。而国内模型又太拉垮还比较贵。怎么办？

1. ### token套餐包月
    

大家可以访问这个推广码去https://codexzh.com/?ref=8C8102 注册，反正可以按日收费也可以按照月收费。

之前体验了，效果还是很OK的。可以按日充值，也可以充值月卡。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTdkODAzNmFhYjAyYTQ5MTQ5MzYyMDRkOTBkMjc2Y2VfbjNyUUhjR05seWtNelBFbTB3TERKQjZjMW1pdEZhWG5fVG9rZW46V1BaeGI0M3JQbzJxNmt4dGhvZmNBYlB4bjJjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

https://docs.codexzh.com/codex/openclaw ，配置codexzh也提供了linux/mac/win的一键配置脚本。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTJjNTJiMGU2YzE5OWNjZTMxZTZkY2QxYjk0MmE3ZjRfRGk1T2I0QWJBYmJtM0J6a0E5QnRHTXBwUzl0dWVTMExfVG9rZW46Wjlua2J5Yko5bzhJUzR4Z0l5YmNEYzNPbnFoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. ### OpenClaw LionCC 模型配置指导（含 key 获取）
    

3. #### openclawkey.ai令牌设置
    

4. ##### 注册登录，[https://openclawkey.ai/login](https://openclawkey.ai/login)；
    

直接使用用户名注册就行了。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjBjMjBiNzJhNDYwNDk2NTE5N2FjNDRmNGVkYWViOTNfSVNBZHo4TW9YTXQ2SDFwblQ2M3h4NXpzM2pkMEx5QjJfVG9rZW46Qm9saWJxcnpwb1pGWFJ4bHdNUmNnem82bm1vXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. ##### 控制台：登录后点击导航栏 **控制台**，进入控制台
    

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MDBkNDNmOWQ5ZTNlNzcwNGFiZjJlNTM2Y2QwNWI2NTNfYkhkZ2g4QTdoMWZEeVpId3lhN3VHVTZaUDZaVUh0UzdfVG9rZW46TVhkMGJaTnY3b0FpcGF4b0xNU2NNZ2ljbkdkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

3. ##### 进入 **控制台** -> **令牌管理**，可以在这里添加，编辑，复制您自己的令牌
    

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YWE3ZDRhNTgwODBhZGYzMDQyMGE1NDRhYjhkMjdjYWVfY0FqUWIxMnRxYldzVm1oVGdVZHVIc0s0SUYwd090MUdfVG9rZW46V0NVVGJoTUEwb1Jqb2l4eEJsWWNQa1lWbnJnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

4. ##### 令牌创建界面如下，选择默认分组就行。
    

选择 openclaw 分组

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ODY5Y2ViMzI3MmI0MzhlNTcwZDcwMmQ1NWY0MWU2ZGNfRXd0cjBEd0ZVc2RMczBkOXRremZaVmRCaFphNDVKNnJfVG9rZW46WXUzYmJIRU15b2M5enR4M0hrUmNsUXV5bmZoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

5. ##### 复制令牌
    

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ODg2ZjgzYjc3ZGIxNTkzYWM0MTczZWU3MjNmYzFlMTVfcTB0dG9Xd1MzbzVKZmZTMEhBUXVkUW5EQTNwTWlyRWVfVG9rZW46QlRWUWJlbE9tb01vY3V4TVpvU2NybDc5bndjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

6. ##### 端点信息和模型ID
    

7. 端点：[https://openclawkey.ai/v1](https://openclawkey.ai/v1)
    
8. 模型 ID 在模型广场找到自己需要的，点击箭头处直接复制模型 ID。
    

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NDJmMGI3MmRlNDM5NGY5YzM0NTM2ZDQzYjVlMzU1MjJfUW5BRWtqVTN6UUFtREVTQjNjNExTdUxXM3FOd0tzNmhfVG9rZW46VVVKdmJ4amNFb0hZUGR4RERwZWNXSXZZbm9lXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2IwMTQ2MjRkZGY5MWU0YTU2Y2E3ZWFjY2UwY2I5YTlfU1NsT1VacXR6OEo1MHBUbTVuRVR2T0hqdngxNW5ld2NfVG9rZW46WGZRbWJHbmVwb0I5aWl4am8wTmNJdks3blBoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. #### 使用脚本配置 AI 模型 API key（推荐）
    

3. ##### 运行模型配置脚本并选择语言
    

```Plain
curl -fsSL https://cnb.cool/wycbug/lioncc-openclaw-configurator-release/-/git/raw/main/openclaw-config-openclaw.cjs -o /tmp/openclaw-config.cjs && node /tmp/openclaw-config.cjs
```

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NjE2YWIzYThiNmYxY2I5N2I1ZTAyZWUzYjM5NjRjNDhfRUVDcE5rQUlta21GZFBhc0xya1lUSXpDOXR0OTZ0RlVfVG9rZW46V1lPeGJCWWhOb3BvazF4NTRHZGNINndpblhiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

2. ##### 选择功能
    

|   |   |
|---|---|
|操作名称|功能|
|配置 openclawkey API|配置密钥和模型|
|更改模型|仅更改使用的模型|

配置 openclawkey API

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NTI2MDRkYjdkYTNkYzEzMGRmMDgyYTdlNWU4MjU2MmRfMkdKN2g5SFlYckVMS0JDY1J6QTZZcFN5ZGZhajVwUEhfVG9rZW46UkxRSGJZMHl3b2dvd1B4UmxqaWNpNFJpbnNmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MGI0YThjMjFlMmE5ZDQwNWNhZWRhNWJiMTUxYTA0ZjFfOGxUc0N1S2V0VDFKRDBqSmIyeU5KRHN1MldGdE9ETDBfVG9rZW46WllaT2JFaExmb1hVS1p4b1B6WmNtWmc1blVnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGYxNmMzOTdiZDBlNWU4ODhkNzZmNzQ2MzY0Zjk2ZjNfTGR0U2NrdER0cnN6alh4S3VvblBmRWpzV1RsdXhFTmJfVG9rZW46T3pUMGI2aUhWb3h2Mzh4RGsxaGM1ME5jbkZmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MTc4OTZiZTUwNDBkYmI4ZDBiYmMzZmU1MDhhNzEzODRfb3NhOGJJNERnYzNTSm5HcHc4dThUSVFxRzhGcERLSG9fVG9rZW46UnVDeWIyOThXb0YzWmd4ZGF3c2NiQTdDblcxXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

3. ##### 测试配置效果
    

运行命令 openclaw tui

输入 /status

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NmZmMWI3Mjk3Y2ZiYTEyYjM4N2NkZjAxOTVkNWU3NDhfRGRCdWtDVGV4S0RyY2tPVGJYV2wyQktQN0l5bGZUS3NfVG9rZW46SGJHNWJzbjRKb0RlTEF4Yk00TWNxSFZsbmtMXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OWM2ZjY5YWNhOGQzYzE5YjM5NTkwMTk4ODU2YWQxZGNfc3g4enpjSXprYUltZVNUcHNSdHJXYVhYcFR1VGd1Y0VfVG9rZW46VUZsemJaYVdZb05MTHV4VUtYWWNpNWtvbk5nXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTZjYzVlYmMwNWQyYzU2YTk3YzQ0OTA1NmNiYzAzODRfd3JoYnJMblBHaFBDRzBGdlM3YUxMRDhUd2JkUVk3bkdfVG9rZW46TE9HaGJ3NTVDb0NVSWF4a05BYWNsMk01bmtlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

3. #### 手动配置 AI 模型 API key（备选）
    

**LionCC推荐使用以下模型：**

本配置适用于任何环境安装的OpenClaw!

Claude系列：claude-sonnet-4-6, claude-opus-4-6, claude-opus-4-5-20251101, claude-sonnet-4-5-20250929

GPT系列：gpt-5.4, gpt-5.3, gpt-5.2, gpt-5.1

  

1. ##### API及配置模型
    

替换以下命令的 sk-your-api-key-here 改成你在lionCC狮子后台创建的密钥

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTk0YzNlOGNlZDgwYWUzOWZlYzRiN2JmZGY4MWY4YjVfMEM2UjlQTHhFdTcwSFZRN25ydmppYmFSTjROaFBBdkRfVG9rZW46SmZEYWJxZjg1b09rM3J4QUdvaGMxTGFpbnFiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

替换以下命令的 your-model-here 改成你要使用的模型，上方有提供推荐的8个模型

  

确认你要使用的模型是 GPT 系列还是 Claude 系列

  

GPT 系列执行这个指令

```Bash
npx openclaw-config-generator apply lioncc-gpt --api-key sk-your-api-key-here --models your-model-here
```

Claude 系列这个指令

```Bash
npx openclaw-config-generator apply lioncc-claude --api-key sk-your-api-key-here --models your-model-here
```

  

执行命令会直接配置好 LionCC狮子API，以及你想要使用的模型，我这里演示为使用claude-sonnet-4-6模型，所以我执行的命令最终为这个。

```Bash
npx openclaw-config-generator apply lioncc-claude --api-key sk-m3vGJwyiwiDwelwnXlnW1vNU9wlGhS9RjCGfsPjSn1fVAh11 --models claude-sonnet-4-6
```

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=Mzc1NjgyNjgyODJhNjJjZWJiN2UxOWMzMDAwMjlkYzFfNzJBTDA2ODBtd3M4MDh2UVU1OU5rN1hEZzFGZVMyRkFfVG9rZW46WVRlWmJZcnJCb0tCRGN4TEJGSmNQenhrbjZnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

我们来测试一下是否成功。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NDIzYjY5ZGMyOGEyZWNiZTU4NTg3NGVlNzNmOTcyM2JfWUc2dVNKRVNrQzBuQXFYeE42Wm1WbzN3ZG5YdUVONVZfVG9rZW46WDl3WmJmR1lMb0tVWTV4TGkzWGNIaXpRbmxnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

2. ##### 切换模型
    

场景为，当前模型遇到故障无法使用时。

```Bash
npx openclaw-config-generator apply lioncc-gpt --api-key sk-m3vGJwyiwiDwelwnXlnW1vNU9wlGhS9RjCGfsPjSn1fVAh11 --models gpt-5.4
```

再次执行上面的命令，只是切换新的模型，比如我要切换成 gpt-5.4 模型

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=M2U3ZDVjNTU4NmI5NGJlZWY3NTUzNjUyZTgyOWEyOWNfSjM4WmdhR2hERGZZTFlWOFNpekM2YVJFUEFicWdYUjVfVG9rZW46TzdNTGJxeEY3b05UZXp4cHMwbGNycUlrblliXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

我们来测试一下是否有成功。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MjJlMmIyZTBhZjFmZmQ2ZTBhY2QxM2MzODdhZGVjMmNfbU5uRVU3VlF1ejVKU2Q4RWNTdDRqWkhrR0FHV2NrNkRfVG9rZW46V3FVbWJ3R2ZBb0c4Rk94RENHUGNvNWJnbjZjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjkzY2M3MTY2ZDI0M2RkMDg0YzdiNWZlOGRmMzRhMzdfQTUyVXhPMWVhb3FBWTExanFjM2ZHaDBLTWR2bWpxbmlfVG9rZW46V0xnTmIxTXB1b1g4Skp4eUlKNmNQcjVybjBjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

##### 3.3 注意事项

  

注意替换三个地方即可：

1、lioncc-claude/lioncc-gpt

2、apikey为你在lionCC后台创建的令牌

3、model为你要使用的模型

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OGE0MmZjN2E5YjFmYjhlMzJjOWJjNDhlOWZmOGIxZTRfeE5PV2tIcjdJcHN6anE5c1BDRWxtaVhtcTNZQUwwanVfVG9rZW46UnNoU2JVY2JPb2x2dTZ4Um1NV2NFN013bmxiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

# 二、先来三个应用认识openclaw

## 应用1:让openclaw帮我们分析文件

应用场景，直接分析文档内容。

譬如我电脑有一个excel文件，放在桌面上。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MjRjYjBmM2ZkYTA4MGQyOTI2NmE3ZTYwNGNjMTliMzVfa05YNzg3ZXM4WjNrUlExMWtLQ2M3SzZ2Z0ZGZjVhUnVfVG9rZW46Uk52RmJZazBpb0RqeDl4bE9XRmNWSUE1bkVnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

那么我通过手机就可以直接问他了。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YTgxN2RlYjQzNmNkMjNkZmExMmJjODg4Yzc0YTgwYmRfT0xLVllrTHVKelZKQjRwbzdydERJMjhYQWFOc3dBTHpfVG9rZW46R3lUaGJxM3NUb2tFN3d4bnBlR2NtTUpPbk5nXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

是不是很简单！

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NGVjMDJjYzkzYzY5Nzk3NDg2Nzg2M2Y0YjYxYWEyMjFfOFFJUG10QkdITWVIZFNmWkZiUkluaGFsMGtuT0l1bkFfVG9rZW46QTNlWWJSS3E4b1NabHV4ajBzZmNGcHBjblFkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

## 应用2:小红书爆款标题采集

总体思路：获取竞品爆款标题，保存到md文件。可以作为我们爆款标题的素材。

01 获取爆款标题。

我们首先让openclaw打开浏览器，帮我检索。

```Python
打开内置的浏览器，访问小红书，搜索十大行业关键词，获取点赞超过500的，每个行业收集50条，保存到～/Download/baokuan.md 然后标题、点赞量、原始地址。
```

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YWQwMjMxYjU4YTE0OTQ0YjNkZDRkMjVhYTkwZmRkMTJfNUx0TTNGUElGcjQxVEkyeUI2TTJldkphRkZubnk3ejNfVG9rZW46SlR4dGJHYVhTb21LOUN4VkJ6dmNhZTFvblJiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

我们知道，很多时候底层大模型会偷工减料，明明要50条，结果：

1、时间长、

2、内容长。

总会找各种理由，这个时候我们就要果断的说：“不要总是给我打折扣，我说啥就是啥”

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=M2M1YmI4YWMxNTBkNzA4YjE3YTNjMTI1MDIxNjk5ODNfUVV5NmpxWFF1MlpDbUFSQ2F1eDV0SXRlZGQ1NUNyZ21fVG9rZW46VDBxRGJualBCbzFLakF4ckZ0M2M1UTAzbjNmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

这个时候我们就可以拿到具体的爆款标题md文档。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjYxZjJmNTlkYmM1ZjY1YmRjNjA5MWEyNGQ4NzRlYmZfUHFvbGFuZEJlQUlnNkh3YklxMUt3V1pYdW9FR1BPdUdfVG9rZW46SUJENWJONVA2b2FEQjZ4eW10WWN6YVlZbk9iXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MDA5NWVmNDk4YWE5NjExOWUyNTJmNjRkMjI1OTJhZDFfNUdibTNpTndsT0FLNDJPZEx3STl5UUUwTnFMNlpKblJfVG9rZW46TWpFQWJuWWpKb0M3TXN4MkpFbWN5WmtkblhjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

## 应用3:QVerisAI介绍

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=N2NhNWFkZGE4NWRlMTQyNzRlMzNiZGM5NWM5MTE5NjFfSDgyZzEzTWg0Qjk2RUxXSDhWU09scktGQ2xNaTY2Zk1fVG9rZW46SmV2MmJJMGRqb2s2VEt4d2h3c2MwV2FubkpoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

核心解决的问题：

1、就是整个多个外部资源、

2、提供统一的接口让openclaw去调用。

特别是：在金融/加密货币数据、股票、天气数据查询类表现特别棒。

所以你会发现，一旦接上它，OpenClaw 就不只是“会聊天”，而是真的可以**查数据、调工具、给结果**。

教程就分为三步，5分钟就能配置好。

1、账号注册。（用gmail）都可以，官方默认1000次免费、每天赠送100次。基本上够满足日常了。

地址：https://qveris.ai/?ref=ea4t8y7bep6cDg

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YmY2M2UwNWE2N2QwYzFjNzI4ODJjOTcxMjg4NTBlZTdfNTJ4NENyYXBvbG5DRkR3TWZzM25hMXpDOGZodTlFV1FfVG9rZW46WFJIaGJQYlk1b1c5b3l4V0JuV2NZN05PbkFlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2、获取API key，然后给openclaw 安装对应的skill。

你只需要这样和openclaw对话，

```Python
通过 clawhub.ai 安装 qveris skill，并将环境变量QVERIS_API_KEY= sk-XXX
```

把sk-XXX 替换成你的API-key。

3、如果不生效，安装完成重启。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MjQyNmMzNTg5ZDY3YWU3Y2Y0ZjZiNDc0ODRmMWFjZTJfckVPUlFudnlYQ2lLU1NtemthanBFN2JyTFN0ZmxiTjNfVG9rZW46VVRVemJRU0R1b0h0MlF4YnNPemMwNk00bjNlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

装了之后，他可以做很多openclaw完成不了的事情：

- 查询金价、汇率、股票行情
    
- 看最近几分钟快速上涨的股票
    
- 查加密货币价格波动
    
- 查询天气和其他实时数据
    

也就是给openclaw插上了更多的翅膀，会查询、会使用！

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NjdjZGZmMzUzZTE4NWI3OWI2OTFlMzRjMGIzMjVlYzBfeHVoeEFkOVVwNjFMSmd2ckNOZFYwTGVORXJjRGdFQTVfVG9rZW46RnlnQ2JaV20zb0NGM054WHJoNGNWODAxbndlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

# 三、OpenClaw实战案例

## 案例1：一键保存到飞书并总结，归纳与提炼。

  

应用场景：很多时候，我们都会收集大量的资料，但是这些连接，往往都已经落灰了。

  

那么保存到飞书文档，每天晚上机器人将我们收藏的内容总结发给我们，每周总结再发给我们，是不是让我们效率会提高很多。

  

暂时无法在飞书文档外展示此内容

  

### 第一步骤：新建飞书应用，并授权。

https://open.feishu.cn/app?lang=zh-CN

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MTQyYjZkZGUzMjhlZjgzYjMwY2FhYzEwYTkyOTg3ZDZfRFJBTFZFcjYza3dMdVZUVFhSWENkUVpQdG8zOTlTdThfVG9rZW46VHJLcmI4eUROb3lRR294VnRtSWNQSWtMbmViXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

先记住咱们的APPID 和APP secert，后续会用到。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NWViOTNkZDM4ZjhjMTMyODA1MGZmNWQ2NjNmZmJiZjdfdzlsWHdmWVRWOWJQTTljZTAzZFc5aE50OVhpMDRub01fVG9rZW46SHBURmJWSkszb1pGWVV4cVpLRWN0YXJwbm1kXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

接下来点击权限管理，进行授权。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YWQxODM4NmNhOWE5MWMzNzQ3YmRkNjVkZjU3ZTM2ZTlfOTFQT2hjNjloaTlFU25YMlVCdHFzQktWZU5MUXc3WjJfVG9rZW46SVFvS2JQWDIxb0tRTXJ4M3FybWM1RDdXblFoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

然后倒入下面的内容：

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YTM0ZTc4MWU5MWVmZjA2OGRmNjZlYjJkZTQyYzU5YzZfbDZMdnpnQjJJQ1pRSFlzd1R1T2dwcFh1Vjh5QVdxVHJfVG9rZW46VUlRV2JxZzdSb1AxZnh4cERjMWNNbHFNbjJmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

```JSON
{
  "scopes": {
    "tenant": [
      "base:table:create",
      "base:table:delete",
      "base:table:read",
      "base:table:update",
      "bitable:app",
      "bitable:app:readonly"
    ],
    "user": []
  }
}
```

完毕后记得发布，才可以。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NmY0YWY3NDYyMWI4MTgyZjY3YzQ0NDNmZDkwOGQwMDNfSkdaMHo0aUlCWTJ6NGhkelBBbUJuUXpVWmphNkNaNmNfVG9rZW46SElQVGJRS1VZb3ByUVd4SjNXS2NWazI4bmdHXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

### 第二步骤：文档授权和应用绑定起来。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjJjMzlkYmQ4ZjA5ZWE4OTYwN2I2MWM5ZTUxM2FlZTNfVXZvZnFRN2x1QlBBZU1rdUlKZGVYYTVha3JiWkJ4ZVFfVG9rZW46V2diYmJ4cDBob3h6NGh4YXhZdmNlbUEzbkZlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

新建一个飞书多维表格。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDJlOGY5NzViY2QzN2U5NDhkYmVjYWYyYWY2ZDBmOGFfNzNIN1VmWVpyc0dVUGZrVklkWlljT3dZWGU4RUlqUmJfVG9rZW46QVVuemJ3anpTb1lKZzJ4RFllNmNMME9TbmVoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

这个时候，搜索我们刚才创建的应用。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NDcxYTU5ZTVlYjY2ZjhkNjA3ZjY3YTIyNzMzNjBkZjJfQW9VaUtqaUhBYTVJMWU0eDg1NlVFQmx0UVc2UVBVa25fVG9rZW46RUNzQWJuQ3M4b2FiVjh4blM2TGN3YlJ2bkNlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

现在需要获取另外两个参数：

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=Njc5MjgyNGE1NmM4NjVhM2U4NzMzYTRiNjRlZDZiNWRfWExtdHFza0NlVFhIaEJCWUdzQm5DSFBTcE5SUzdKZGRfVG9rZW46V0NLa2JIWWhSb3ZuZFB4TWRESmNwVlF2bjFvXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

这个时候我们保存了四个参数分别是：

```Python
| 参数                | 说明         | 获取方式       |
| ----------------- | ---------- | ---------- |
| FEISHU_APP_ID     | 飞书应用 ID    | 飞书开放平台创建应用 |
| FEISHU_APP_SECRET | 飞书应用密钥     | 同上         |
| FEISHU_APP_TOKEN  | 多维表格 token | 从表格 URL 获取 |
| FEISHU_TABLE_ID   | 数据表 ID     | 从表格 URL 获取 |

```

然后把这几个参数保存成一个文本文档，然后放到执行的目录下，让openclaw自己去读。

譬如说：“～/Downloads/feishu.txt”

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MjQwZWIwOWY3OTJiMTVmYzA2NjAyOWFmZWE5ZGQwNjdfczZONjU0ZkFOaE4zV3V2RE1mMTBvVVJzdVpMUmF1WUhfVG9rZW46SGFrc2IycE5Jb281dVB4RGkwbGNKS0oyblZiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

### 第三步骤：调用skill保存到飞书文档

```Python
调用https://clawhub.ai/harven-droid/wechat-article-parser 这个skill，给我安装，我配置的飞书的内容都在～/Downloads/feishu.txt
中，你获取后移动到.openclaw的配置文件夹下。
```

后续使用的时候，直接这样说就行了，

```Python
调用wechat-article-parser这个skill。 将我的微信文章https://mp.weixin.qq.com/s/r4Yok1FA91k_eaJ7f_QKIA 保存到飞书文档
```

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YWMxOWU4NGI5N2U1NzcyNTY2MGQ3MDM2ZGMzZmRlOGRfTXBQV1ZseE9sWGdLaUU5RGI0WGp5d0ZYaUZzTzdOOENfVG9rZW46Wk9VdWJnUzJrb2NoT1J4NG5GRmNXcmNzbmpwXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

## 案例2：下载B站视频，直接提取内容，并生成一篇文章。

  

暂时无法在飞书文档外展示此内容

主要分为几个部分：

### 第一步骤：如何下载B站音频

这里我们用的是bilix这个skill，完全免费，可以直接下载b站的视频/音频。

我们这样说：

```Python
现在我们需要完成b站视频的下载，用到这个skill是工具： bilix（B 站专用下载工具） ，帮我安装.
```

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ODFiYzQyMGU2NTIxNjNjYzI1YmM3Y2E5ODcxMGQ5MmRfQXZTOTd2bjJIelBPZHVvMnhFR25jRERNaTVxT0RUVjBfVG9rZW46WU1uNWJBcmRmbzR2YlB4aVhGTGNEWnJYblBoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

遇到问题，让openclaw自己修改。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YmM2NTg4YzRlOGQ2Y2ZmYzcyZWZjZWFhOTE5OWQ2NTNfWDNSQnFPcDhOZDdhOGlwY1k3VTNIS0JJRWJKaDBTTDlfVG9rZW46RUlJbGJVc3Rtb2wxVVZ4Qk41a2MxZ3Q0bkhnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

### 第二步骤：如何提取内容

两种方法都可以：

01 用咱们第五章，应用3的方法。【适用：电脑性能比较好的用户】

02 讯飞可以免费5个小时语音文字。【适用，电脑性能不怎么样的旧电脑】

官方地址：https://www.xfyun.cn/

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YmE4OWY0ZWJkMjI3MTBjZmQyZTMwYTBkMWIxYmE1NTFfR29IdzJqTmR6RVJXUVh6SzRQdzNMMXc5NUljYldmbUlfVG9rZW46SDVMQmJwRlhxb0xVd0F4aE01a2N3aXdXblRlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

点击免费使用：

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NmYzZTlmZjM5ODUxNDJhZTI4MTBlYWU3ZTNmMmU5NmFfUUxOSTdxYjFuV2h1Y1RhbGFEd1JobzBQRmtweGlMbkJfVG9rZW46TTlmQmJQTlQwb2pSUEl4RERyWWNzWDhrbkhlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

继续购买

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NzFjNmRkMmU2ZjJiMjBjN2JkMmZjMjhjYThiYWRjN2VfTzVaQTVETUtEdnE5WmNaRmc0a3dQVnhDaDdLTW9lbElfVG9rZW46UWNkSmJNV2Zqb0lxRVR4VTRjMWNTczNibmpmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

最后购买成功之后，进入个人中心的页面。

https://console.xfyun.cn/services/new_lfasr，找到自己的认证信息。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NTcwODkzZjI0ZDcyMjljZTI2MGRiNTJhOWExMzYzZDVfdWRxeG53V2lLV3k1a1pMekpSWXhqSFAzcFR5VGp5ckNfVG9rZW46S1dQV2I3RTI5b1lPZk94bU5DamNhd3RybkllXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

当你有了这些信息之后，接下来可以吧这些信息复制下来保存成一个文本文档，丢到你的下载文件夹，

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NmI5NTQxMzNiZjFiZDcwYWZlNTA2MzA3OWYzMzhhYWFfTFl3ZHFlZ0JFQklCaDV5UjR5R0F3OGNsNWcxWFpLYjVfVG9rZW46RGFMa2IxQ0pIb1ZJOGl4aFQ0UmNycEJWbnpnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

你直接说：

```Python
给我安装skill，skill地址：https://clawhub.ai/harven-droid/iflytek-asr
讯飞skill需要的参数放到~/Downloads/xunfeiasr.txt 的这个文件下，你获取到可以放到.openclaw下的配置文件夹下。
```

当这个skill安装好之后，后续您

  

```Python
用iflytek-asr这个skill给我将语音转换为文本
```

### 第三步骤：如何改稿。

改稿其实很简单，大瑜写了一个skill,第一次只需要这样说就行。

```Python
给我安装skill，skill地址是：https://clawhub.ai/harven-droid/wechat-style-writer
```

这个skill安装好，你只需要这样说就行。

```Python
用wechat-style-writer这个skill，给我生成卡兹克风格的文章。
```

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YjJkZThmMjY4OGFkYTk0ZDY0YjAyMzcxNWMyYTVkMWVfb2lVYmdLSElqOTdlOVA3U0VCbEJ4dVV5SGFaQUpQeEdfVG9rZW46TXZpWWJSbW4xbzY3Tkx4UUlYeWNtQTl3bkVlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

## 案例3: 批量抓取抖音/小红书视频+提取文案@新侠

  

目前市面上抓取小红书有两个途径：

  

1.用自己的cookie（也就是自己账号的登录信息），这个方法好处是上手简单，没有成本。坏处就是很容易把自己的账号搞成风控。

2.纯API接口解决方案。好处是不用自己的账号，坏处就是每次调用需要费用。

  

抓取抖音的方法比较多，且API接口也比小红书便宜许多。

  

这次我们介绍下第二个方案，用API接口。但不同的是不是我们自己去调用API接口，而是让OpenClaw帮我们去调用，我们只需要用自然语言去描述需求就好。

  

### 第一步骤：首先登录tikomni.com，注册一个账号。

  

注册完成后会赠送0.05💲。抖音接口的调用费是0.0015💲，小红书接口的调用费是0.015💲。大家可以先从抖音开始测试。

  

注册完成后进入控制台 - API密钥 页面，创建一个API密钥。

  

必须注意这个密钥需要妥善保存好，因为他只会出现一次。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ODVmM2M2ZmFkM2M4YzlkNTFmZTdjOTdlODdjZjdjMDFfZjI3eXAwNG9nRTc5V3V0VlBiR3hXcGVjdXhYZ0xmZDNfVG9rZW46VW90WmIwUGVHb0hPUk54QU5MRmNmUnVVbmRpXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

### 第二步骤：然后我们直接和OpenClaw对话：

```Plain
帮我安装这个skill
npx @tikomni/skills list
```

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NmQyYzU2NWM3OTc2OTk2N2VmMTg0NWQwYWVmOWY1NmRfWGZCazRBQUZQV2NLSjM4Z3pZREF1NmZKSTdnczE2dEdfVG9rZW46SjJ1ZWJXVWJ3b294b0V4NGVCOGNQVk1ObjJlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

然后OpenClaw就会自动帮你把这个Skill安装好。

他还会贴心的提示你，需要重新加载skills目录才会生效，你直接回复“重载”就可以。

  

### 第三步骤：配置API key和数据存储位置

安装完成后，我们还需要配置一下API key和数据存储位置。

  

你可以直接和OpenClaw描述

```Plain
这个social-media-crawl skill还需要配置一下环境变量
刚刚安装后在/skill 根目录下有一个env.example文件，请你帮我复制成.env 文件在/skill根目录
帮我配置如下变量
TIKOMNI_API_KEY="这里替换成你的apikey"
TIKOMNI_OUTPUT_ROOT="这里写你希望存放原始结构化数据的绝对文件夹路径"
TIKOMNI_CARD_ROOT="这里写你希望存放markdown卡片的绝对文件夹路径"
```

  

当然，你也可以手动编辑环境变量。

你可以直接让OpenClaw帮你安装一个VSCode。

再用VSCode去编辑。

在 /.openclaw/workspace/skills 目录下找到env.example文件，可以直接重命名为.env 也可以新建一个.env文件，把evn.example文件中的内容粘贴过去

然后编辑如下变量内容

TIKOMNI_API_KEY="这里替换成你的apikey" TIKOMNI_OUTPUT_ROOT="这里写你希望存放原始结构化数据的绝对文件夹路径" TIKOMNI_CARD_ROOT="这里写你希望存放markdown卡片的绝对文件夹路径"

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ODc3MjM1NmU3MzFlMGYwMGU2ZGFjMTQ1MGVkMDkwNDBfZ2hwV3pwaFJHSWN3SDdtRnlzald4RE5PU3JBbWRuSHRfVG9rZW46TVJ6UmJSaTBkb3Q0SXZ4UXVXZGNKTDJObkdiXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

### 第四步骤：测试结果

至此SKILL的安装和相关配置就完成了，我们来测试一下。

直接丢一个抖音博主的主页链接，简单描述一下“采集抖音主页”

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MDI5MTljYWNkMDA1YmJjZWM5NjgyYjU4NDViZjQ0OGNfTVBKTVhvTWZvZXdvUUx1aENiN3RYaFoxZXpDZlFCamhfVG9rZW46SmFxZ2J5QkVsb1A3R3h4OTJHamN3VUwxbmJjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

他抓取了20条作品，但这不是我想要的，我要的是抓取全部作品，没关系，我们表达清楚需求

强势一点“全量采集”

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MmNjNzk5NDUzODljMzYxNTNjOGM4NDdjZTE1NGIwZjhfZkl2bzZ6YnBTSzNnamdrT0h2YXhIVVpyanZEVWdMUlVfVG9rZW46UkdGV2JvYmVwb1Y1Vjh4bk1GYmNyMjRlblRoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

等个几分钟，OpenClaw就会屁颠屁颠的过来告诉你，全部搞定了。

效果如下：

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MmFiOTU1ZTJkYzc4ZGYxYWY3MDc5M2MxNGIxN2U2NDJfV21RUnF1Rmd2MDFxU0s3VzcwMzlSMXJJd3RydGs4Nm9fVG9rZW46T2xOV2JPajd4b0Vua0l4STBBemNvdE5Ybm5nXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTMzNWQ3YThhNzFiZGY5OWVjZjBkNmU1ODA3ZGY5OWNfZ2tBSzhrUWc5UDNvOXVoVU53ZWFJaXdPazdqaHA4MGxfVG9rZW46TFhrdGJnQ0k4b3lib094Y3AxVGMxM0tVbmJmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

## 案例4: OpenClaw协助打磨内容

案例3我们讲了如何把某个博主的作品采集下来并分析，接下来我们讲讲如何借助OpenClaw帮我们打磨内容。

  

### 第一步骤：分析什么是好内容

要打磨内容，我们必须要知道什么是好的内容

  

我说：

> - 我：「分析这个作者的文风和结构」
>     

  

它就会：

1. 读取这 150+ 条文案

2. 分析文风（语气、用词、句式）

3. 分析结构（开头、正文、结尾的套路）

  

可以让他把分析后的结论生成分析报告，并要求他生成一个按xxx博主风格写作的skill

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ODBjYTdmZGQyNjhiNWEwMzJiYzE4Nzg0OWIwNmQyZjNfMnhqT0F6V0p6cmdkWUppRzdmR2FqYnVrR3pQWWROaHNfVG9rZW46UGxROGJDdFFWb0drYVp4eHMycWNSMmlhbmVoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

**写公众号长文也是类似的逻辑**

我把自己之前写的 4-5 篇精华文章发给它学习。

我说：

> - 我：「学习我的写作风格：[文章1] [文章2] [文章3] [文章4] 」
>     

它就会：

1. 读取这 4-5 篇文章

2. 分析我的结构（开头、正文、结尾）

3. 分析我的写法（语气、用词、句式）

4. 生成一份风格指南

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTFlMTA5YjdmOTU5MzA0MGNhODlmMGEyZWQxNGQzYThfVVQ2UFRDUm9FY1JGRGE1dmxYcFkxcFAzN2F5ckhkY2lfVG9rZW46VjFxRGJGYjQ4b2Ria1V4bE9MQWM1TmhTbk9iXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

一样让他学习生成一个我的风格的长文写作skill。

  

### **第二步骤：****整合成 content-studio 工作流**

把这些能力整合成一个完整的工作流。

现在整个链路是：

```Bash
content-studio（内容创作总管）
  ├─ 记录选题
  ├─ 深化选题（fast research：本地检索 + WebSearch + WebFetch → 生成 Brief）
  ├─ 生成内容（按形态分流）
  │ ├─ 抖音口播 → video-writer（短视频写手）
  │ └─ 公众号文章 → mp-writer（公众号写手）
  ├─ 发布归档
  └─ 素材沉淀
```

你可以直接把这个架构发给你的OpenClaw，让他协助你一起打磨一个适合你的内容创作工作流

  

### 第三步骤：完整工作流演示，从选题到发布

#### Step 1：记录选题

我在 Telegram 里发：

我：「记录选题：OpenClaw 零基础实战」

OpenClaw 回复：

OpenClaw：「已记录到选题记录.md，当前状态：待深化」

它会在`选题管理/01-选题记录.md`里加一条：

```Plain
## OpenClaw 零基础实战-状态：待深化-记录时间：2026-02-05-初步想法：写一篇 OpenClaw 的实战教程，从安装到配置到实际使用
```

---

#### Step 2：深化选题

接下来我说：

我：「深化选题：OpenClaw 零基础实战」

OpenClaw 开始工作：

1. 检索本地素材库：- 搜索`wiki/AI/工具/`下的 OpenClaw 相关笔记- 搜索`wiki/自媒体/方法论/`下的教程写作方法- 搜索`wiki/自媒体/素材库/金句库/`下的可复用金句
    
2. WebSearch 调研：- 搜索"OpenClaw 安装教程"- 搜索"OpenClaw 实战案例"- 搜索"OpenClaw vs Codex"
    
3. WebFetch 深度阅读：- 读取 OpenClaw 官方文档- 读取阿里云无影云电脑的 OpenClaw 部署教程- 读取社区里的实战分享
    
4. 生成 Brief 文件：
    

OpenClaw 回复：

OpenClaw：「已生成 Brief 文件，保存在`选题管理/01-选题记录/OpenClaw零基础实战-Brief.md`」

Brief 文件内容大概是这样的：

```Plain
## 核心观点-OpenClaw 不是"一键安装"的工具，需要折腾-但它给你的是对电脑的最高操作权限-会越用越像你，成为你的"第二大脑"## 目标读者-愿意花时间折腾的人-想把 AI 助手接进日常工作的人## 大纲1.OpenClaw 是什么（对比 Codex/Claude Code）2.云电脑准备（为什么推荐阿里云无影云电脑）3.安装接入（详细步骤 + 截图）4.踩坑与配置（5个坑 + 推荐配置）5.实战演示（完整工作流）## 素材来源-官方文档：https://docs.openclaw.ai/-阿里云教程：https://help.aliyun.com/...-我的实际踩坑经历（topic:391 聊天记录）
```

---

#### Step 3：讨论大纲

我看了 Brief 后，觉得大纲还可以，但有些地方需要调整。于是我说：

我：「大纲看起来不错，但"踩坑与配置"这部分要详细一点，每个坑都要写清楚"问题 → 尝试 1 → 尝试 2 → 最终方案"」

OpenClaw 回复：

OpenClaw：「收到，我会按"踩坑优先法"来写这部分，每个坑都写完整的解决过程」

---

#### Step 4：生成草稿

我确认大纲后，说：

我：「好，开始写草稿吧」

OpenClaw 开始写作：

1. 读取作者风格指南： - 读取`作者风格指南.md`（我的写作风格、语气、禁忌词） - 读取`公众号爆款写作.md`（标题公式、结构模板）
    
2. 生成标题： - 生成 4 种类型的标题（冲突对比型、疑问引导型、数字+效果型、否定+反转型） - 我选了"数字+效果型"：「复盘：我花30分钟在云电脑上搭了个OpenClaw，现在选题/素材整理全自动（附SOP）」
    
3. 生成正文： - 按大纲逐章节生成- 每生成一章节，我都会看一遍、提意见 - 比如我说"开头太激进了，不要说'全自动'，要说'需要持续调整'" - 它就会立刻改
    
4. 质量检查： - 检查是否有"元信息章节"（如"参考资料""延伸阅读"） - 检查是否有 Markdown 超链接（应该用纯文本链接） - 检查段落长度（每段 2-4 句）
    
5. 落盘草稿：
    

OpenClaw 回复：

OpenClaw：「草稿已生成，保存在`选题管理/02-待排版/OpenClaw零基础实战/index.md`」

---

#### Step 5：多轮修改

草稿生成后，我会多轮修改。

比如：

- 修改 1：优化开头
    

我：「开头这边你写的太过激进了。整个过程我只需要在手机上发几条信息，剩下的全自动，这太激进了。其实过程中我还是持续地去对整个的内容不停地跟它调整，实际上我们也花费了很多的 token 和时间」

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OWY5NmZjNWJhNTdjMzQ2YTM0ZjVjODk5ZDZhOGY5MThfVW9IRHJ3ZnBFY05mNnpvZTFjbVBxMFdjT2JackFZZ1VfVG9rZW46WU9MdmJGWFFBb2dTYnd4THV4cGNHeUhwbmlkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

OpenClaw 回复：

OpenClaw：「收到，我重写开头部分，删掉"全自动"，补充"需要持续调整、花费 token 和时间"」

  

- 修改 2：充实实战演示部分
    

我：「对于实战演示，你写的实在太简单了。这部分应该重新写，它是整个文档的精华，你要写得再具体一点」

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTM0M2QxOTIwOTc3YWQwYTJmNjJmZjA3OGQ4Y2RiNzNfM0xiTTNyeTg3TUl4eVZQNk1DM3piNEI4ckZhTlFxYklfVG9rZW46VmJjdGJZWGhjb0dldU94a1ZPVWNHRVlsbmtxXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

OpenClaw 回复：

OpenClaw：「收到，我重写"实战演示"部分。我会详细展示：1. content-studio 的演化过程（4个阶段，每个阶段都说明"为什么要加这个功能"）2. 完整工作流演示（7个步骤，从选题到发布）」

然后它开始重写，加入了批量抓取作者主页、分析文风、学习爆款文章等关键细节。

  

- 修改 3：优化文件组织规则
    

我：「我发现你把 image 放在了代码库的根目录下面，而且草稿正文中并没有直接引用这些图片。应该是每一篇文章都要建立一个子文件夹，在这个文件夹下面放它的草稿 MD 文档以及对应的图片」

OpenClaw 回复：

OpenClaw：「收到，我立刻调整文件结构，并把规则写入 mp-writer/SKILL.md」

  

- 修改 4：从官方文档提取截图
    

我：「你说的配图，你就直接从官方的教程去把配图弄下来不行吗？因为我已经安装完了，我没有办法再去截图了」

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWY3MzVlYjBkZjIxYzhmOWE1Njc0MzBkZjcyYjY3MjlfUFdMTE9oTUlkMVZWUElsTUp4c285WDRYaTM4QXN0SGtfVG9rZW46U0FXdmJWRW9Mb2dIUU94dDdyWWMxdE5pbjFkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

OpenClaw 回复：

OpenClaw：「对，我可以直接从阿里云官方文档把配图下载下来。我现在去读官方文档，提取截图」

  

- 修改 5：直接发对话截图，自动放到对应位置
    

我：「这 4 张图是我觉得在创作这篇文章的过程中，跟你不断对话、修正后的截图。你可以把它们放到对应的位置上」

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MWViOWE2NGQxODI5OTU3MmVlNWZkZDNlZjU0ZDY0NThfdXc3WHR5QWY1cldxTjVCa3I0akpMQkF0NnpJdTRpVGxfVG9rZW46SzJCMWJvQWtkb1lrd2t4WEJlcGNkZnpTblVjXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

OpenClaw 回复：

OpenClaw：「收到。我先把这4张图片保存到 images 目录，然后看看它们的内容，再放到对应的位置」

然后它自动：

1. 识别这4张图是对话截图

2. 分析每张图对应哪个修改环节（优化开头、充实实战演示、文件组织、安装教程）

3. 把图片放到"Step 5：多轮修改"的对应位置

4. 更新草稿里的图片引用

  

关键点：我只需要在 Telegram 里直接发对话截图，OpenClaw 就能自动识别内容、放到对应的位置、更新文档引用。全程不需要我手动操作。

---

经过这些修改后，我觉得草稿可以了，就说：

我：「这版可以了，草稿定案」

---

#### Step 6：推送到公众号草稿箱

  

最后一步是推送到公众号草稿箱。(具体配置可以参考案例5）

我说：

我：「推草稿」

OpenClaw 开始工作：

1. Markdown → HTML 排版：- 把 Markdown 转成公众号 HTML- 处理图片（上传到图床、替换链接）- 处理代码块、引用块、列表等格式
    
2. 推送到草稿箱：- 调用公众号 API- 推送到草稿箱
    

OpenClaw 回复：

OpenClaw：「已推送到公众号草稿箱」

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MzI1MGFmMjQ3MzdmOTkyYmM3MTIxNDQyNDljYTYyMWJfaVhaT2hkRkQ5YktaRXViVnd2QkJweEJFZnFCaktjNjlfVG9rZW46REpBRmJJYW9xbzFkeWZ4Yk1reWN2VjlvblJnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

## 案例5：Openclaw 接入公众号，进行自动化发布@用户8260

  

> 目标：把公众号的 AppID/AppSecret 配置到 OpenClaw，并完成 IP 白名单配置，从而实现「自动生成内容 → 写入草稿箱（或发布）」的自动化链路。

> 流程图（概览）：先看一遍整体路径，再按下方步骤逐项配置。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YjRhOTA3NTQzZDc0YzFkMmViODBlMDQ2ZGIzOTNhNDdfc3FESnpLOUpwc2VDM3AwNDNLMkFtUmxWSVBDVjRqZEFfVG9rZW46V3NiZGJwMkFob3lGNUh4cjRHQWNsZ1RCbmJlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

---

### 第一步骤：前置条件

- 你已拥有一个**微信公众号账号**（订阅号/服务号均可）
    
- 你可以登录微信公众平台后台
    
- OpenClaw Gateway 已部署并能正常运行
    

---

### 第二步骤：进入公众号后台（开发配置页）

首先登录公众号后台（示例链接）：https://developers.weixin.qq.com/console/product/mp/wxed360a4cdff46867?tab1=basicInfo&tab2=apiMonitoring

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=N2ZlN2VmMjZkODg4NTQ5NDIxNDQ3NTkyOGZhOTAwZWZfTkpnQ2VyWlM2SktyUkhxNGFmNjdZMkxYM2Y5NloxRmtfVG9rZW46VFdYWmJ5YWNQb1YyS3R4Z3B1Q2Nvbk93bmpoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

我们主要关注这几个点：

- 选择合适的公众号
    
- 关注 AppID
    
- 关注开发密钥部分的 **AppSecret**
    
- **API IP 白名单**（后面要填 OpenClaw 给你的出口 IP）
    

---

### 第三步骤：将 AppID / AppSecret 配置到 OpenClaw

把对应公众号的 AppID / AppSecret 配置给 OpenClaw（建议在**私聊**中操作）。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MjcxYWI3MjFmZTI2Mzg0OGU3YTFiNDUyOTQyODg2NGZfMHZISTkxREluVnNYbjd6MTBXVkZ6UzV2c3hYMlZOTGxfVG9rZW46WkFTRGJhZm83b1lPaGh4ckt5WWMyNUZWbkFlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

安全提示（强烈建议保留）

- AppSecret 相当于「公众号的密码」，**不要发到群聊/公开渠道**。
    
- 如果不小心泄露过：去微信公众平台 **重置密钥（rotate）**，并同步更新 OpenClaw 配置。
    

  

### 第四步骤：配置 API IP 白名单

OpenClaw 在接入过程中会给你一个（或多个）出口 IP。

把这些 IP 填入公众号后台的 **API IP 白名单**。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDFkYzNmOGQ2ZjlhNjhkZmVlNGNlYzJjYTFlYjViMWRfVEVxQTVteElnV2N3U2F0M0hvcklBSVhWNFczQmh1NzBfVG9rZW46UGhGbWJrUEg1b2JyNUd4bGlDYmNmQnZnbktsXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

---

### 第五步骤： 重启网关并验证

完成配置后：重启一次 OpenClaw Gateway 让配置生效。

- `openclaw gateway restart`
    

### 第六步骤：如何验证

建议做一个最小闭环验证：

- 让 OpenClaw 生成一篇测试内容并尝试写入公众号
    

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGJkN2M5YjFiY2Q2MGFmZDZmOTBmMmRmZmRiNjExNmFfekFJSmpUOUU2U0Y0S3I2RWthdlNNTlQ1UkVFMGtMcUlfVG9rZW46V1BVV2JZUGs2b3lTUnh4dVhXSmNzSUFRbmVlXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

- 去公众号后台确认：是否成功进入**草稿箱**
    

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ODhlYzE1MjQ0MGI2NDVmYTExNWZhMDdjMjE3YjQ4Njhfenc1VEgzaXEyb2RSN0ZSbDRRbWdJdEFsUU5wQXAwWTNfVG9rZW46RFFQOGJJZjMwb2RpOTJ4dWF4VWNXYUVHbmlkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

---

### 第六步骤：理解能力边界和梳理常见问题

#### （1）能力边界说明（按当前测试）

- ✅ 支持：图片、文字、内部超链接、基础格式
    
- ❌ 不支持：账号名片展示
    
- ⚠️ 自动发布：通常需要公众号完成**认证**
    
    - 未认证：一般只能进入草稿箱
        
    - 已认证：可根据接口权限实现更自动化的发布链路
        

---

#### （2）常见问题（排错清单）

- **提示权限不足/接入失败**：优先检查公众号选对没、AppSecret 是否正确、IP 白名单是否已放行。
    
- **能写草稿但不能发布**：通常是公众号未认证或权限不足。
    
- **配置改了没生效**：确认已重启网关，并检查 OpenClaw 侧是否仍在报 IP 白名单错误。
    

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=N2U5YzY3MWQxYWE0YjcxYWUxMjlkNWE2MjJkYjYwZTNfSTBpdmhqcXNLS3RiajZoR3k0bE5DMnFIcDdETlR6RGhfVG9rZW46VGRpdWJEQkY4bzhOb0d4cDFScGNYb3h2bjdmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

  

# 四、如何配置多个数字员工（高阶学习）

达成效果：通过配置多个飞书群，每个群不互相影响。

1. ## 什么是数字员工
    

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OWVjYjZhYjE3NmYyNTI0MzczZTI3OTgyYmRlNjdhYmVfYVFEVEpsemRPcnpyYVozUXZ6T3VYMVRzZmhOeUJOazZfVG9rZW46UnNld2J3SlRUb2JKUnR4MXFuT2NaWjg1bjBnXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

是不是很多牛马，拼了命的给你干活。

2. ## 如何配置你的数字员工
    

很多人用openclaw可能只用一个agent。简单的说就是：

写文章用它

写代码用它

做运营还是用这个agent。

一开始很爽。然而，三天后全乱套了。语气开始混乱、前后风格开始不一样。

```Python
- 让 AI 写文章写到一半，突然问了个技术问题，结果它回来写文章时语气都变了!!!
- 一个 Agent 又写代码又搞运营，上下文越来越长，token 消耗飙升!!!
- 让它一会儿当 CTO 一会儿当运营总监，人格分裂是迟早的事!!
```

一个🦞干多个人的活，迟早会精神崩溃。

解决办法，拆开成多个agent！让专业的人干专业的事。

1. ### 多agent（多个数字员工）可以解决什么事情？
    

一句话来讲就是角色相互隔离，上下文不污染，每一个角色只负责一件事。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NjU1NmNiMzNiNzRiMWIwYzVmMWVjZWM0NTEwY2NlYzRfb253VEc0OXBQRHZJSElWU2RhaDZhbDVMZUxPQnNPeUdfVG9rZW46WTRTcWJ4NVdSbzlMcGp4dTFCUGNIT0oxbmNmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. ### 实践（一个提示词搞定数字员工配置）
    

其实配置多个数字员工的方式很简单。

第一步：去新建APP机器人应用。譬如运营机器人就是一个应用、写作机器人就是一个应用、文案收集都是一个机器人。

具体方式参考第一章2.1部分。

第二步：【如果是单账号多群的话】需要在飞书见一个群，后续将对应机器人拉到一个群中。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ODc5OTUxMTQ3NzU5NWZmM2Q0NDZjZTZmOTI3YmI1NjZfenZuTHlLeld2dWNkTFp6cG1hR21ZWDhNNlBhNEZXNjNfVG9rZW46TDc0V2I3dVdZbzhsdTZ4UHhRTGNyS1labmliXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

并获取群id

第三步：将下面的提示词发给openclaw

暂时无法在飞书文档外展示此内容

这个时候我们就会收到回复：

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=MDFlNmQwMjgxZWExZTZmMjNmN2YwM2ViMGMyMDQ1MjdfUllVUWYxZG4yem5NMTdoQlU1MWhMc0hiM3NXbGh1NkFfVG9rZW46WVpVaWJCNnI3b2s3Qkx4V2VlcGNaZzd0bnBmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

第四步：输入信息之后，然后就等openclaw自己改了。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTA5NjgyMDkxNTZlZGExN2ZlMzAwZWY0ODllZjI2NmZfUU5kM0l2T0U3cjZqdGtVMm5BTnllem9LM0d3U0kwSElfVG9rZW46VUlsd2JkdE9pb09nRjB4RGlnUWNlME0wbmVoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

改好之后，重启：openclaw gateway restart即可。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YmZmYjNiZDAxODQzMzcxMDM0ODgyZWY2MGNmYTdmZTJfb0lLWW55NFNOTHpadmZxZVNxT0NvZURsYm9ndHNRYVlfVG9rZW46VFEzVmJMNkJwb0piVFF4ZkpIbmNEbVJJblRoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

# 五、Agent skills介绍（高阶学习）

这个章节，无意于告诉你Skill的起源、发展等等，或者和你讲解SKILL和MCP有什么区别，那些对于非专业人士都太遥远了。

1. ## Skill 到底是什么？
    

很多新手会把 Prompt、Tool、Skill 混在一起。

你可以这样记：

- **Prompt**：告诉 Agent 这次怎么说
    
- **Tool**：让 Agent 能搜索、读文件、发消息、跑命令
    
- **Skill**：告诉 Agent 遇到某类任务时，应该怎么做
    

所以 Skill 更像一个“任务说明书”或者“操作手册”。

比如：

- 做研究时，要先搜索、再抓取、再整理证据
    
- 写代码时，要先判断任务类型，再选择合适的执行方式
    
- 想新建技能时，要按规范创建目录、写好 `SKILL.md`
    

这些就不是一句 Prompt 能稳定解决的事，而更适合写成 Skill。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NmQ0NmY3MWQwYTM3NWQ3MDlhZDdkNmNjYTZhNTNlYWVfM3NrVDljQnk1aE5yNkh3MUJxbVN1UDFEN2NDeG82a29fVG9rZW46RnFZSmIzbUtUbzgxM2l4TU56V2NVNVBxbjhmXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

2. ## 为什么要用 Skill？
    

因为没有 Skill，Agent 很容易变成一种状态：**这次做对了，下次又忘了。**

Skill 的价值主要有三点：

### 第一，结果更稳定

不用每次重新教 Agent。只要任务命中对应 Skill，它就会按固定方法做，不容易乱来。

### 第二，更适合零基础用户

你不需要自己设计复杂 Prompt，也不需要每次提醒 Agent 先做什么后做什么。装好 Skill，很多套路就已经内置了。

### 第三，能力能复用

同样一类任务，今天能用，明天还能用。你不是在“临时聊天”，而是在给 Agent 积累可重复使用的能力。

如果要说得更直接一点：

> **不用 Skill，你是在每次重新带一个实习生；用了 Skill，你是在给 Agent 安装 SOP。**

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YzRiMjdmMDgyNmZiYjFjMTc1YTU1YzllNzcyZmM4ZThfOVIxbEFteVh3V1BqMW55enRhcDdQSUhLTzlLRUUwR0VfVG9rZW46WEFxQ2JtbkdXb1JidHV4S3RSSWNSMTMxbkNkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

3. ## 零基础用户建议先装哪些 Skill？
    

如果你刚开始用 OpenClaw，我建议先装/先了解下面这几类。

安装的方式也非常简单，直接用自然语言和openclaw表达即可。

### 3.1 skill-creator

这是“自己做 Skill”时最重要的起点。

它适合这些场景：

- 你想新建一个 Skill
    
- 你想修改现有 Skill
    
- 你想按规范整理 Skill 目录结构
    
- 你不确定 `SKILL.md` 应该怎么写
    

简单说，**它是造 Skill 的工具箱**。

如果你未来想把自己的高频工作沉淀成 Agent 能反复使用的方法，这个几乎是必看。

---

### 3.2 clawhub

这是用来**搜索、安装、更新、发布 Skill** 的。

适合这些场景：

- 想看看有没有别人已经做好的 Skill
    
- 想安装一个现成 Skill 直接用
    
- 想把本地 Skill 升级到新版本
    
- 想把自己写好的 Skill 发布出去
    

可以把它理解成一个“Skill 市场 / Skill 包管理入口”。

对零基础用户来说，价值很直接：

> 先别急着自己造轮子，先看看社区里有没有现成的。

很多时候，你缺的不是能力，而是没找到合适的 Skill。

---

### 3.3 find-skill（或技能搜索类能力）

这个名字在不同环境里可能会有差异，但需求本质都一样：

**先找到适合当前任务的 Skill。**

这是新手最容易忽略的一步。

很多人一上来就自己写 Prompt，结果写半天，其实系统里可能已经有：

- research-skill
    
- weather
    
- github
    
- obsidian
    
- social-media-crawl
    
- acp-router
    
- coding-orchestrator
    

所以更好的顺序通常是：

1. 先找有没有现成 Skill
    
2. 有就直接用
    
3. 没有再考虑自己写
    

这能少走很多弯路。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=OTU1YjUzNDA2Y2I1YzgyZGNhZDU5OTcxN2RlYjY5YjlfaTRyZ2czSXJHQzNQdkRRTVRyNldvQXl4MkNZcHFsWHlfVG9rZW46WTN5QmJjTDhXb1VCOTB4RkpCemN2a2V5bkFoXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

4. ## 新手最实用的使用顺序
    

如果你是零基础，我建议直接按这个顺序上手：

### 第一步：先用现成 Skill

先别急着自己造。

从最常见的任务开始，比如：

- 调研
    
- 天气查询
    
- GitHub 操作
    
- Obsidian 笔记处理
    
- 社交媒体抓取
    

先体验一下“有 Skill 的 Agent”是什么感觉。

### 第二步：学会找 Skill

用 clawhub 或技能搜索类方式，先确认有没有现成方案。

这是最省时间的一步。

### 第三步：再学自己写 Skill

当你发现某类任务自己经常重复做，而且系统里又没有特别合适的 Skill，这时再用 `skill-creator` 去做自己的版本。

顺序别反。很多人就是死在“还没用明白，就急着自己定义一套世界观”。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=YzA5NDA1Y2VlYzZjZWY2YjBiZWE4OTJjZDc3MDMwNjNfMHRxVWM3RnZxRGFEMWNoYTdwMnhzUjVKd1NjdGVlQVlfVG9rZW46RDVFdWJkVXFvb2VOZUJ4czNqeWNna3dtbkhkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

5. ## 对零基础用户，一个最简单的判断标准
    

什么时候应该考虑 Skill？

看这条就够了：

> **如果一类任务你会反复做，而且每次都希望 Agent 按相似方式处理，那它就适合做成 Skill。**

比如：

- 每次调研都要“先搜集证据，再整理成固定格式”
    
- 每次写代码都要“先判断类型，再走对应执行流程”
    
- 每次写内容都要“按统一结构输出”
    

这些都很适合 Skill 化。

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=NGU2M2EwODU3MGJlZmM0NWY4NjI1MjJlMGRlOGU4N2VfaUtnRllTdHRmMkZDaUR2aVlXdUxoQnZZaThrZDRkaU5fVG9rZW46RkVOTGJqNmkzb3pNdUN4N2tFRmN1cDZubmdkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

# 六、直播安排

  

本期实战将安排3-4场直播，解决大家所有遇到的问题。

  

  

![](https://d7s4ezaanv.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDM1YWNlYjM2MzczMGRhZDI0YzBiNmI2MjY3YjNmNDRfYUxGdTVaRGtGdXR6cXZnUFZIdmk4UFNVVmtDcmlDWVlfVG9rZW46U09HTmJyWUJybzVjREp4YUphcGNYSFNXbnFkXzE3NzQ2MDk2Nzk6MTc3NDYxMzI3OV9WNA)

# 七、百问百答

  

实战期间，嘉宾的经典答疑回复将由资料官搜集整理放到此文档中，持续更新...

[OpenClaw实战百问百答 | 2026年3月淘金计划](https://l14f33myrkm.feishu.cn/wiki/KrlxwBII6inl01kBqa2cbkAFnFe?from=from_copylink)