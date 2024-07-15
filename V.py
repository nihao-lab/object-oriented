"""

"""
from M import Commodity
from C import C
from TOOS.iterable import Toos
class V:
    def __init__(self):
        self.__c=C()
    def __show(self):
        for itme in self.__c.list:
            print(itme)

    def __print(self):
        print('1建添加')
        print('2建查看全部')
        print('3建删除')
        print('4建修改')
        print('5键查看最贵')
        print('6键价格排序')
        print('7根据编号查找是什么商品')

    def __get_number(self,meseage):
        while True:
            try:
                nmuber=int(input(meseage))
                return nmuber
            except:
                pass

    def __select(self):
        n=input('请输入：')
        if n=="1":
            self.__add()
        elif n=='2':
            self.__show()
        elif n=='3':
            self.__dele()
        elif n=='4':
            self.__updata()
        elif n=='5':
            self.__max()
        elif n=='6':
            self.__stor()
        elif n=='7':
            self.__cid__name()


    def __add(self):
        m=Commodity()
        m.name=input('请输入商品名称：')
        m.price=self.__get_number('请输入价格：')
        self.__c.add(m)

    def __updata(self):
        new_m=Commodity()
        new_m.cid=self.__get_number('请输入要修改的编号：')
        new_m.name=input('请输入修改的名称：')
        new_m.price=self.__get_number('请输入修改的价格：')
        if  self.__c.updata(new_m):
            print('修改成功')
        else:
            print('修改失败')

    def __dele(self):
        number=self.__get_number('请输入要删除的编号：')
        if self.__c.dele(number):
            print('删除成功')
        else:
            print('编号不存在')

    def __max(self):
        max_=max(self.__c.list, key=lambda obj:obj.price)
        print('最贵的是：%s,价格是：%s'%(max_.name,max_.price))
    def __stor(self):
        new=sorted(self.__c.list, key=lambda obj:obj.price, reverse=True)
        for itme in new:
            print(itme)

    def main(self):
        while True:
            self.__print()
            self.__select()

    def __cid__name(self):
        res=Toos.show_id(self.__c.list,lambda obj:obj.cid==self.__get_number('请输入编号：'))
        if type(res)==str:
            print(res)
        else:
            print('对应的商品名称是%s'%(res.name))








