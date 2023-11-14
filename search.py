import re
from render import Render
from fichier import Fichier
import subprocess
from myfunc import Myfunc
from myrecording import Myrecording
class Search(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="my thrift shop"
    self.figure=Render(self.title,template="search.html")
    self.recparams=["name","image","price","date"]
  def email(self,myscrit):
    self.figure.set_content(Fichier("./welcome","email.html").lire())
    self.figure.set_title("Se connecter à la boîte mail")
    print("hi there")
    return self
