import collections
import urllib
import re

class Mesmots():
    def __init__(self,x):
        self.mots=x
        self.res=[]
        self.nbres={}
        self.mesmots={"/email":"email mail mes emails boite mail mail google"}
    def getdescription(self,data):
        y = BeautifulSoup(data)
        c = y.find('body').findAll(text=True, recursive=False)
        mystring=""
        for i in c:
            print i
            mystring+=i
            if len(mystring) > 100:
                break
        return mystring
    def gettitle(self,html):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.match(r"^.*<title>\s*(.+?)\s*</title>.*$", html)
        # Part 3: return the first group if match was successful.
        if m:
            return m.group(1)
            return ""
    def partiedemesmots(self):
        for y in self.mots.split(" "):
            res=0
            for z in self.mesmots:
                if self.nbres[z] is None:
                    self.nbres[z]=0
                if y in self.mesmots[z]:
                    self.nbres[z]+=1
        sorted_x = sorted(self.mesmots.items(), key=lambda kv: kv[1])
        sorted_dict = collections.OrderedDict(sorted_x)
        for w in sorted_dict:
            if sorted_dict[w] > 0:
                myurl = 'http://localhost:8081'+w
                response = urllib.urlopen(myurl)  
                data = response.read()            
                title= self.gettitle(data)
                mystring= self.getdescription(data)
                self.res.insert(0,{"title":title, "description": mystring,"url": "/"})
        return self.res
