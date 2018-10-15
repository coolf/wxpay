# wxpay
微信扫码支付sdk

## 必要模块 ##

    hashlib
    requests
    xml


## 官方文档 ##

    https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=6_5


##  python3 sdk ##

    基于官方文档
    初始化 sdk


----------


    AppKey = '微信支付平台查看'
    AppId = '微信支付平台查看'
    mch_id = '微信支付平台查看'
    notify_url = '支付回调url'
    spbill_create_ip = '服务器发起请求ip'

## 初始化微信支付 ##
    wxpay = WxPay(AppKey, AppId, mch_id, notify_url, spbill_create_ip)

## 统一下单api ##
    # 向微信统一下单API发出请求，传递参数过去，获得回传结果后提取数据， (提取订单号，支付url)
    content = wxpay.getPayLink('测试', '10')

    print(content)
    //{'return_code': 'SUCCESS', 'return_msg': 'OK', 'appid': 'wx1*****d531c23', 'mch_id': '15*****61', 'nonce_str': 'dqL4*****gmG0bE', 'sign': 'C32CC4B1A*****84614ACC31FD4E', 'result_code': 'SUCCESS', 'prepay_id': 'wx1511192365*****608681a1237036923', 'trade_type': 'NATIVE', 'code_url': 'weixin://wxpay/bizp*****l?pr=tyckRj8'}
    #提取数据执行自己的逻辑代码

## 回调验签 ##
    ## 验证签名 (需要支付回调的xml参数)  验证通过 True/False
    wxpay.verify()

## sdk demo ##
    https://github.com/ouerrrr/wxpay
    python3 dome.py