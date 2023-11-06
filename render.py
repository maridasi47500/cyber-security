from fichier import Fichier
import os
from db import Db
class Render():
  def __init__(self,title):
    self.title=title
    self.body=title
    self.template="./template/index.html"
    self.headingone=title
    self.collection={}
    self.my_params={"myoutput":""}
    self.collection_string=""
  def get_my_params(self):
    return self.my_params
  def set_my_params(self,name,param):
    self.my_params[name]=param
  def set_collection(self,name,collection):
    self.collection[name]=collection
  def render_collection(self,path,view,mycollection,as_,erreur):
    try:
      myview=open(os.path.abspath(path+"/"+view), "r").read()
      string=""
      count=0
      print(len(mycollection),"my collection")
      for res in mycollection:
        for x in myview.split("<%="):
           if "%>" not in x: 
             string+=x
             continue
           else:
             y=x.split("%>")
             myexpr=y[0]
             print(myexpr)
             try:
               mystr=y[1]
             except:
               mystr=""
             try:
               loc={as_: res}
               print(loc)
               string+=eval(myexpr, globals(), loc)
             except:
               string+=""
             string+=mystr

      return string
    except Exception as e:
      return "<p>{erreur}</p>".format(erreur=(erreur+str(e)))
  def render_body(self):
    string=""
    myinclude=False
    for x in self.body.split("<%="):
       print(x)
       y=x.split("%>")
       myexpr=y[0]
       try:
         mystr=y[1]
         myinclude=True
       except Exception as e:
         mystr=""
         myinclude=False
       if myinclude:
         try:
           print(myexpr, "monexpression")
           loc={"self": self,"Db":Db,"render_collection":self.render_collection, "my_params":self.my_params}
           exec("myres="+myexpr,globals(),loc)
           if type(loc["myres"]) is bytes:
             string+=loc["myres"].decode()
           else:
             string+=loc["myres"]
         except Exception as e:
           print(e,"m error")
           string+=""
         string+=mystr
         myinclude=False
       else:
         string+=myexpr
    self.body=string
  def get_title(self):
    return self.title
  def get_headingone(self):
    return self.title
  def get_body(self):
    return self.body
  def set_content(self,mybody):
    if len(mybody) > 0:
      if type(mybody) is bytes:
        print(mybody)
        self.body+=str(mybody)
      else:
        self.body+=mybody
    else:
      self.body+=''
  def ajouter_a_mes_mots(self,mot):
    self.body += mot
  def render_figure(self):

    template=open(self.template,"r").read()
    self.body= template.format(mots=self.get_headingone(),debutdemesmots=self.get_title(),partiedemesmot=self.get_body())
    self.render_body()
    return self.body
