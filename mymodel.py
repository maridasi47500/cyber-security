class Mymodel():
    def __init__(self,params):
        for x in params:
            loc={"self": self,"params": params}
            exec("self.set_"+x+"(params["+x+"])",globals(),loc)

