# -*- coding:utf-8 -*-
# blog：https://blog.teqiyi.com

from wxPaySdk import WxPay

if __name__ == "__main__":
    AppKey = 'aach********127401'
    AppId = 'wx12********31c23'
    mch_id = '151********561'
    notify_url = 'http://********.com'
    spbill_create_ip = '11********238'

    # 初始化 微信支付
    wxpay = WxPay(AppKey, AppId, mch_id, notify_url, spbill_create_ip)

    ## 向微信统一下单API发出请求，传递参数过去，获得回传结果后提取数据， (提取订单号，支付url)
    content = wxpay.getPayLink('测试', '10')
    print(content)



    ## 验证签名 (需要支付回调的xml参数)  验证通过 True/False
    wxpay.verify()
