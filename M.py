"""

"""
class Commodity:
    def __init__(self,name:str='',price:int='',cid:int=''):
        self.name=name
        self.price=price
        self.cid=cid
    def __str__(self):
        return f"商品名称{self.name},商品单价{self.price},商品编号{self.cid}"
    def __repr__(self):
        return "Commodity('%s',%s,%s)"%(self.name,self.price,self.cid)
    def __gt__(self, other):
        return self.price>other.price
    def __eq__(self, other):
        return self.cid==other
