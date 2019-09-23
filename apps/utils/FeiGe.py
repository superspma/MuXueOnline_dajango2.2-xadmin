import requests
import json


def send_single_sms(apikey, code, mobile):
    # url = 'https://sms.yunpian.com/v2/sms/single_send.json'
    # text = '【慕学生鲜】您的验证码是#{}#。如非本人操作，请忽略本短信'.format(code)
    # res = requests.post(url=url, data={
    #     'apikey': apikey,
    #     'mobile': mobile,
    #     'text': text,
    # })
    # re_json = json.loads(res.text)
    # return re_json
    res = {'code': 0}
    return res


if __name__ == '__main__':
    apikey = 'd6c4ddbf50ab36611d2f52041a0b949e'
    res = (send_single_sms(apikey, '654321', 17621078991))
    print(res)
    res_json = json.loads(res)
    code = res_json['code']
    msg = res_json['msg']
    if code == 0:
        print('发送成功！')
    else:
        print('发送失败：{}'.format(msg))
