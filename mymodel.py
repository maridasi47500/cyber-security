class Mymodel():
    def __init__(self,params):
        for x in params:
            loc={"self": self,"params": params,"y": params[x]}
            exec("self.set_"+x+"(y)",globals(),loc)

