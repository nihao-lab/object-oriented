"""

"""
from data import Data

class C:
    def __init__(self):
        self.__data=Data()
        self.list=self.__data.read()
        self.star_id=self.list[-1].cid+1 if len(self.list) else 1001
    def add(self,m):
        m.cid=self.star_id
        self.star_id+=1
        self.list.append(m)
        self.__data.write(self.list)
    def updata(self,new):
        for itme in self.list:
            if itme.cid==new.cid:
                itme.__dict__=new.__dict__
                self.__data.write(self.list)
                return True
        return False

    def dele(self,cid):
        if cid in self.list:
            self.list.remove(cid)
            self.__data.write(self.list)
            return True
        return False
