import re
from render import Render
from fichier import Fichier
import subprocess
from myfunc import Myfunc
from myrecording import Myrecording
class Hello(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="aide informatique"
    self.figure=Render(self.title)
    self.recparams=["name","image"]
  def get_figure(self):
    return self.figure
  def new(self,myscrit):
    self.figure.set_content(Fichier("./welcome","new.html").lire())
    print("hi there")
    return self
  def myshop(self,myscrit):
    self.figure.set_content(Fichier("./welcome","myshop.html").lire())
    print("hi there")
    return self
  def hi(self,myscrit):
    self.figure.set_content(Fichier("./welcome","index.html").lire())
    print("hi there")
    return self
  def create(self,myscrit):
    rec=Myrecording(myscrit).new(self.get_mydata()(self.recparams))
    self.figure.set_content("<a>redirected permanently</a>")

    if rec.create():
      print("uploaded and save...")
      self.set_redirect("/myshop")
    return self
