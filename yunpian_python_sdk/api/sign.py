# -*- coding: utf-8 -*-
'''
Created on Jun 19, 2017

@author: dzh
'''
from ..model.constant import (YP_SIGN_HOST, APIKEY, SIGN, VERSION_V2, OLD_SIGN)
from .ypapi import YunpianApi, CommonResultHandler


class SignApi(YunpianApi):
    '''签名接口 https://www.yunpian.com/api2.0/sign.html'''

    def _init(self, clnt):
        super(SignApi, self)._init(clnt)
        self.host(clnt.conf(YP_SIGN_HOST, 'https://sms.yunpian.com'))

    def add(self, param, must=[APIKEY, SIGN]):
        '''添加签名API
        
        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        sign String 是 签名内容 云片网
        notify Boolean 否 是否短信通知结果，默认true true
        apply_vip Boolean 否 是否申请专用通道，默认false false
        is_only_global Boolean 否 是否仅发国际短信，默认false false
        industry_type String 否 所属行业，默认“其它” 物联网 其他值例如:1. 游戏 2. 移动应用 3. 视频 4. 教育 5.
        IT/通信/电子服务 6. 电子商务 7. 金融 8. 网站 9. 商业服务 10. 房地产/建筑 11. 零售/租赁/贸易 12.
        生产/加工/制造 13. 交通/物流 14. 文化传媒 15. 能源/电气 16. 政府企业 17. 农业 18. 物联网 19. 其它

        Args:
            param: sign notify apply_vip is_only_global industry_type
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2:rsp[SIGN]}[self.version()])
        return self.path('add.json').post(param, h, r)

    def update(self, param, must=[APIKEY, OLD_SIGN]):
        '''修改签名API
        
        仅“审核中”或者“审核失败”的签名可以进行修改，修改后会重新提交给客服审核。
        参数notify，apply_vip，is_only_global如果没有将会修改为默认值
        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        old_sign String 是 完整签名内容，用于指定修改哪个签名，可以加【】也可不加 云片网
        sign String 否 修改后的签名内容（如果要改签名内容） 云片网
        notify Boolean 否 是否短信通知结果，无此参数默认true true
        apply_vip Boolean 否 是否申请专用通道，无此参数默认false false
        is_only_global Boolean 否 是否仅发国际短信，无此参数默认false false
        industry_type String 否 所属行业，默认“其它” 物联网 其他值例如:1. 游戏 2. 移动应用 3. 视频 4. 教育 5.
        IT/通信/电子服务 6. 电子商务 7. 金融 8. 网站 9. 商业服务 10. 房地产/建筑 11. 零售/租赁/贸易 12.
        生产/加工/制造 13. 交通/物流 14. 文化传媒 15. 能源/电气 16. 政府企业 17. 农业 18. 物联网 19. 其它

        Args:
            param: old_sign sign notify apply_vip is_only_global industry_typ
        Results:
            Result
        '''
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2:rsp[SIGN]}[self.version()])
        return self.path('update.json').post(param, h, r)

    def get(self, param=None, must=[APIKEY]):
        '''获取签名API
        
        参数名 类型 是否必须 描述 示例
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        id Long 否 签名id，暂未开放，如果传入此参数将会指定获取某个签名 9527
        sign String 否 签名内容 云片网
        page_num Integer 否 页码，1开始，不带或者格式错误返回全部 1
        page_size Integer 否 返回条数，必须大于0，不带或者格式错误返回全部 20

        Args:
            param: sign notify page_num page_size
        Results:
            Result
        '''
        param = {} if param is None else param
        r = self.verify_param(param, must)
        if not r.is_succ():
            return r
        h = CommonResultHandler(lambda rsp: {VERSION_V2:rsp[SIGN]}[self.version()])
        return self.path('get.json').post(param, h, r)
