import collections
import urllib
import re
import urllib.request
from bs4 import BeautifulSoup

class Mesmots():
    def __init__(self,x):
        self.mots=x
        print("mesmots", self.mots)
        self.res=[]
        self.nbres={}
        self.mesmots={"/email":"email mail connexion mes emails boite mail mail google",
        "/signup":"email mail inscription mes emails boite mail mail google",
        "/banq":"banque banque en ligne mona banq monabanq banque",
                }
    def getdescription(self,data):
        y = BeautifulSoup(data)
        c = y.find('body').findAll(text=True, recursive=False)
        mystring=""
        for i in c:
            print(i)
            mystring+=i
            if len(mystring) > 100:
                break
        return mystring
    def getpic(self,html):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.match(r"^.*<link rel=\"icon\" type=\"image/x-icon\" href=\"\s*(.+?)\s*\">.*$", str(html))
        # Part 3: return the first group if match was successful.
        if m:
            return m.group(1)
        else:
            return ""
    def gettitle(self,html):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.match(r"^.*<title>\s*(.+?)\s*</title>.*$", str(html))
        # Part 3: return the first group if match was successful.
        if m:
            return m.group(1)
        else:
            return ""
    def get_results(self):
        print("hey results")
        try:
          try:
            print("hey 1")
            for y in self.mots.split(" "):
                print("hey 2")
                res=0
                for z in self.mesmots:
                    print("hey 3")
                    try:
                        print("hey 4")
                        if (y) in self.mesmots[z]:
                            self.nbres[z]+=1
                    except Exception as e:
                        print("hey 5",e)
                        print("my error 1",e)
                        if (y) in self.mesmots[z]:
                            self.nbres[z]=1
          except Exception as e:
            print("hey 6",e)
            print("my error",e)
          print("hey 7")
          print("items",self.nbres.items())
          sorted_x = sorted(self.nbres.items(), key=lambda kv: kv[1])
          sorted_dict = collections.OrderedDict(sorted_x)
          print("my sorted dict",sorted_dict)
          for w,value in sorted_dict.items():
              print("tem sorted ")
              print(w, value)
              print(value > 0)
              if value > 0:
                  myurl = 'http://localhost:8081'+w
                  print(myurl)
                  response = urllib.request.urlopen(myurl)  
                  #print(response)
                  print("-->my data")
                  data = response.read()            
                  print("length my data")
                  print(len(data))
                  print("my data")
                  title= self.gettitle(data)
                  print("title",title)
                  mystring= self.getdescription(data)
                  mypic= self.getpic(data)
                  print("description",mystring)
                  self.res.insert(0,{"pic":mypic,"title":title, "description": mystring,"url": w})
        except Exception as e:
            print("my erroooor",e)
        return self.res
