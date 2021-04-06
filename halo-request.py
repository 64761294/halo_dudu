import requests
import json

# 登录
def Login(host,username,password,accessKey):
    prams = {'username':username,'password':password}
    header = {
        'Content-Type': 'application/json',
        'API-Authorization':accessKey
    }

    Login = requests.post(host+'/api/admin/login',json=prams,headers=header)
    # print(token.text)
    # 存储access_token
    loginres = json.loads(Login.text)
    token = loginres['data']['access_token']
    return token

# 添加日志
def addLog(host,username,password,accessKey,content,email,author):
    # 发起日志请求
    token = Login(host,username,password,accessKey)
    header = {
        'Content-Type': 'application/json',
        'API-Authorization':accessKey
    }
    journal_url = host+'api/admin/journals?admin_token='+token
    print(journal_url)
    jourdata = {
        "allowNotification": True,
        'author':author,
        'sourceContent':content,
        'email':email
    }
    journal_res = requests.post(url=journal_url,headers=header,json=jourdata)
    return journal_res

if __name__ == '__main__':
    # 在此调用addLog函数并传入相应参数
    """
    params:
        # host:博客域名
        # username:后台账号
        # password:密码
        # accessKey:api密钥
        # content:日志内容,当前只支持字符串
        # email:邮箱
        # author:作者
    """