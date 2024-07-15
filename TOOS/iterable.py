"""
根据编号查找
"""
class Toos:
    @staticmethod
    def show_id(list_,func):
        for item in list_:
            if func(item):
                return item
            #为真 我直接返回符合要求的对象，你爱取对象的啥值，取啥值

        # 我的lambda obj:obj.cid==self.__get_number('请输入编号：')，是判断语句，只会返回真或者假
        # 不是赋值语句，所以即使不存在，是返回假而已，而不是报错
        # 遍历完，都不存在，我 就返回编号不存在的字符串。
        return ('编号不存在')
