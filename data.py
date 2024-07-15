"""

"""
from pathlib import Path
from M import Commodity
class Data:
    def __init__(self):
        self.lj='data.txt'
    def read(self):
        """
        路径不存在的时候，返回空列表
        :return: list|list(Commodity)
        """
        if not Path(self.lj).exists():return []
        # not是取反，假就变真，第一次是假的，就变成真，就执行空列表，第二次是真的，就取假，假就不执行空列表。执行下边的
        with open(self.lj,'r',encoding='utf8')as file:
              n=eval(file.read())
              return n
    def write(self,list_):
        with open(self.lj,'w',encoding='utf8')as file:
            file.write(list_.__repr__())
