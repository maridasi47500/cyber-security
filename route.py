import re
from hello import Hello
from search import Search
from erreur import Erreur
from mypic import Pic
from render import Render
from javascript import Js
from stylesheet import Css


class Route():
  def __init__(self):
    self.params={}
    self.route={
r"/$":"Hello#hi",
r"/?s=(.*?)$":"Hello#search",
r"/bienvenue$":"Hello#hi",
r"/email$":"Hello#email",
r"/create$":"Hello#create",
r"/dates$":"Hello#dates",
r"/mysum$":"Hello#mysum",
r"/myshop$":"Hello#myshop",

}
  def get_route(self,myroute,myparams,mydata=None):
    print(myroute,myparams)
    print("myroute")

    self.params=myparams
    if myroute.endswith("ico"):
        myProgram=Pic(myroute)
        return myProgram
    elif myroute.endswith("png"):
        myProgram=Pic(myroute)
        return myProgram
    elif myroute.endswith(".wav"):
        myProgram=Son(name=myroute)
        return myProgram
    elif myroute.endswith(".css"):
        myProgram=Css(name=myroute)
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
