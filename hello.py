import re
from render import Render
from fichier import Fichier
import subprocess
from myfunc import Myfunc
from myrecording import Myrecording
class Hello(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="my thrift shop"
    self.figure=Render(self.title)
    self.recparams=["name","image","price","date"]
  def get_figure(self):
    return self.figure
  def dates(self,myscrit):
    self.set_json(True)
    self.figure.set_body("")
    self.figure.set_json(Fichier("./welcome","date.json").lire())
    print("hi there")
    return self
  def new(self,myscrit):
    self.figure.set_content(Fichier("./welcome","new.html").lire())
    print("hi there")
    return self
  def email(self,myscrit):
    self.figure.set_content(Fichier("./welcome","email.html").lire())
    self.figure.set_title("Se connecter à la boîte mail")
    print("hi there")
    return self
  def myshop(self,myscrit):
    self.figure.set_content(Fichier("./welcome","myshop.html").lire())
    print("hi there")
    return self
  def hi(self,myscrit):
    try:
      if myscrit["s"] is not None:
        self.figure.set_my_params("s",myscrit["s"][0])
        self.figure.set_template("search.html")
        myhtml="search.html"
    except:
      myhtml="index.html"

      print("hi there")
    self.figure.set_content(Fichier("./welcome",myhtml).lire())
    return self
  def mysum(self,myscrit):
    self.set_json(True)
    self.figure.set_body("")
    xx=self.get_mydata()(uploads=["date"])
    print(xx,"xx")
    self.figure.set_my_params("mydate",xx["date"])
    self.figure.set_json(Fichier("./welcome","mysum.json").lire())

    return self
  def create(self,myscrit):
    xx=self.get_mydata()(uploads=self.recparams)
    print("create with my params : ", xx)
    rec=Myrecording(xx)
    self.figure.set_content("<a>redirected permanently</a>")

    if rec.create():
      print("uploaded and save...")
      self.set_redirect("/myshop")
    return self
