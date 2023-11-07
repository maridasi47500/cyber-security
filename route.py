import re
from hello import Hello
from erreur import Erreur
from render import Render
from javascript import Js


class Route():
  def __init__(self):
    self.params={}
    self.route={
r"/$":"Hello#hi",
r"/bienvenue$":"Hello#hi",
r"/new$":"Hello#new",
r"/create$":"Hello#create",
r"/myshop$":"Hello#myshop",

}
  def get_route(self,myroute,myparams,mydata=None):
    print(myroute,myparams)
    print("myroute")

    self.params=myparams
    if myroute.endswith("ico"):
        myProgram=Pic(myroute)
        return myProgram
    elif myroute.endswith(".wav"):
        myProgram=Son(name=myroute)
        return myProgram
    elif myroute.endswith(".js"):
        myProgram=Js(name=myroute)
        return myProgram
    else:
        for i in self.route:
          j=self.route[i]
          if re.match(myroute, i):
            print(j, "my func found")
            loc = {}
            print("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"').work(params=params).encode()".format(params=myparams))
            exec("myvar="+j.split("#")[0]+"('"+j.split("#")[1]+"')",globals(),loc)
            print(loc["myvar"])
            print("=my var")
            print(mydata)
            print("=my data")
            loc["myparams"]=myparams
            #loc["mydata"]=None


            if mydata:

                loc["myvar"].set_mydata(mydata)
                print(loc["myvar"].get_mydata())
                print("=mydata")

            exec("myvar=myvar.work(params=myparams)",globals(),loc)

            return loc["myvar"]
        mytext=(Erreur().err404())
        return mytext
