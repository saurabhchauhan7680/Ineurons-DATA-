#Practice 
from distutils.log import INFO
import logging as lg
lg.basicConfig(filename="Saurav",level=lg.INFO)

class test:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def test_custom(self,v):
        return self.v-self.a
    def __str__(self):
        print("This is my first test of adsorption")
o=test(4,5,6,7)
o.test_custom(25)
o.__str__

