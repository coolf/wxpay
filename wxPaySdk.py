# -*- coding:utf-8 -*-
#blog：https://blog.teqiyi.com
import hashlib
import time, requests
import random, sys
import string
from urllib.parse import quote
import base64, datetime
from XmlOtherDict import Xml2Dict, Dict2Xml




class WxPay(object):

    def __init__(self, AppKey, AppId, mch_id, notify_url, spbill_create_ip):
        self.AppKey = AppKey
        self.AppId = AppId
        self.mch_id = mch_id
        # 软件标题
        self.notify_url = notify_url
        # 服务器IP
        self.spbill_create_ip = spbill_create_ip

    # 计算sing
    def Sing(self, data):
        ret = []
        for k in sorted(data.keys()):
            if (k != 'sign') and (k != '') and (data[k] is not None):
                ret.append('%s=%s' % (k, data[k]))
        params_str = '&'.join(ret)
        params_str = '%(params_str)s&key=%(partner_key)s' % {'params_str': params_str, 'partner_key': self.AppKey}
        params_str = hashlib.md5(params_str.encode('utf-8')).hexdigest()
        sign = params_str.upper()
        return sign

    # 验签 验证回调sing。 传入回调xml 数据
    def verify(self, xml):
        data = Xml2Dict(xml).result
        data = data['xml']
        Sing = self.Sing(data)
        if Sing == data['sign']:
            return True
        else:
            return False

    # 二维码扫码 传入购买标题和价格（分）
    def getPayLink(self, body, total_fee):
        data = {
            'appid': self.AppId,
            'mch_id': self.mch_id,
            'nonce_str': str(int(round(time.time() * 1000))) + str(random.randint(1, 999)) + '12321',
            'body': body,
            'out_trade_no': datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            'total_fee': total_fee,
            'spbill_create_ip': self.spbill_create_ip,
            'notify_url': self.notify_url,
            'trade_type': 'NATIVE',
        }
        sign = self.Sing(data)
        data['sign'] = sign
        request_xml_str = Dict2Xml('xml', data).result
        url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
        r = requests.post(url, data=request_xml_str)
        r.encoding = 'utf8'
        content = Xml2Dict(r.text).result['xml']
        return content
