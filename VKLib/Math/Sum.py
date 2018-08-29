from ..Collection import  Crash

class Calculator():

    def Add(self, a, b):
        return a+b

    def Sub(self, a, b):
        return a-b

    def RelativeCrash(self, a, b):
        return Crash.Crasher.Crash([a,b])