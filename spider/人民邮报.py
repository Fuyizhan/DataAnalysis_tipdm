import requests
ur1 = 'https://www.ptpress.com.cn/'
login_info = 'https://www.ptpress.com.cn/login/getUserName'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
cookie_str = 'acw_tc=2760777f17037475248483727ee65e9a0fe9f98780f819d76d4a9bfdf6d695; JSESSIONID=3CC5DB90BFDFD4A72C7FAF15A320F6CC'

cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=')
    cookies[key] = value

r1 = requests.get(ur1, cookies=cookies, headers=headers)
r2 = requests.get(login_info, cookies=cookies, headers=headers)
print('获取用户的登陆信息：', r2.text)
r3 = requests.get(login_info, headers=headers)
print('获取用户的登录信息： ', r3.text)