import re
from hello import Hello
from email import Email
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
r"/signup$":"Hello#signup",
r"/login$":"Hello#signin",
r"/hello$":"Email#voiremail",
r"/create$":"Hello#create",
r"/dates$":"Hello#dates",
r"/signout$":"Hello#signout",
r"/mysum$":"Hello#mysum",
r"/myshop$":"Hello#myshop",

}
  def get_route(self,myroute,myparams,mydata=None,session={},cookies=False):
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
            loc["mysession"]=session
            loc["mydata"]=mydata
            loc["cookies"]=cookies
            print("SESSION !",session)
            #loc["mydata"]=None


            if mydata:

                loc["myvar"].set_mydata(mydata)
                print(loc["myvar"].get_mydata())
                print("=mydata")

            exec("myvar=myvar.work(params=myparams, session=mysession,data=mydata,cookies=cookies)",globals(),loc)
            exec("myvar.delete_notice()",globals(),loc)

            return loc["myvar"]
        mytext=(Erreur().err404())
        return mytext
