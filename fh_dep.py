"""
http://120.132.109.87:10088/jfycfx

"""
import requests

if __name__ == '__main__':
    url = 'http://120.132.109.87:10088/jfycfx'
    sent = '张三的爸爸是谁？'
    resp = requests.get(url, params={'text': sent})
    print(resp.text)
    with open('fh_dep.json', 'w') as fw:
        fw.write(resp.text)
