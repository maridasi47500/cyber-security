from render import Render
from subprocess import check_output as runmyscript

class Myfunc():
    pic=False
    js=False
    css=False
    mymusic=False
    json=False
    figure=Render("hi") 
    upload=False
    redirect=False
    myfile=False
    mydata=False
    php=False
    myargs=False
    mydatafunc=False
    someparam={}
    my_params=figure.get_my_params()
    cookies=False
    myattributes=[]
    figure=False
    params=False
    
    myprmogram=False
    run=False
    path=False
    runthisprogram=False
    session=False
    def set_php(self,x):
        self.php=x
    def get_php(self):
        return self.php
    def set_param(self,x,y):
        print("set param")
        if not self.session:
            self.session={}
        self.set_session_param(x,y)
        self.set_session_param("mysession",True)
        self.figure.set_my_params(x,y)
    def set_session_param(self,x,y):
        print("set session")
        if not self.session:
            self.session={}
        self.session[x]=y
    def get_session_param(self,x):
        return self.session[x]
    def sign_out(self):
        if not self.session:
            self.session={}
        for k in self.session:
            self.session[k]=None
        self.session["mysession"]=True
        self.session["notice"]="deconnectée"
    def delete_session(self):
        if not self.session:
            self.session={}
        for k in self.session:
            self.session[k]=None
        self.session["mysession"]=True
        self.session["notice"]=""
    def get_session(self):
        if not self.session:
            self.session={}
        return self.session
    def set_my_session(self,x):
        if not self.session:
            self.session={}
        for k in x:
            self.session[k]=x[k]
        self.session["mysession"]=False
        self.session["notice"]=False
    def delete_notice(self):
        if not self.session["mysession"]:
          self.session["notice"]=""
    def set_session(self,x):
        if not self.session:
            self.session={}
        for k in x:
            self.session[k]=x[k]
        self.session["mysession"]=True
    def set_someparam(self,x,y):
        self.someparam[x]=y
    def set_someparam(self,x,y):
        self.someparam[x]=y
    def get_someparams(self):
        return self.someparam
    def get_someparam(self,x):
        return self.someparam[x]
    def set_myargs(self,x):
        self.myargs=x
    def get_myargs(self):
        return self.myargs
    def set_json(self,x):
        self.json=x
        if x:
            self.figure.set_body("")
    def get_json(self):
        return self.json
    def set_css(self,x):
        self.css=x
    def get_css(self):
        return self.css
    def set_redirect(self,x):
        self.redirect=x
    def get_redirect(self):
        return self.redirect
    def set_mydata(self,x):
        self.mydata=x
    def get_mydata_param(self,x):
        return self.mydata[x]
    def get_mydata(self):
        return self.mydata
    def set_runthisprogram(self,run=False):
        self.runthisprogram=run
    def get_runthisprogram(self):
        return self.runthisprogram
    def runprogram(self):
        if self.myfile and self.myfile.endswith(".sh"):
            return "sh"
        elif self.myfile and self.myfile.endswith(".py"):
            return "python3"
        elif self.get_progtam():
            return self.get_program()
        else:
            return None

    def run(self):
        arr=[]
        if self.get_runthisprogram():
            if self.get_myargs():
                arr=self.get_myargs()
                script=runmyscript(arr)
                self.figure.my_params["myoutput"]= script
            elif self.runprogram():
                arr.append(self.runprogram())
                if self.myfile:
                    arr.append(self.get_path()+"/"+self.myfile)
                script=runmyscript(arr)
                self.figure.my_params["myoutput"]= script
    def set_file(self,x):
        self.myfile=x
    def get_program(self,x):
        self.myprogram=x
    def set_program(self,x):
        self.myprogram=x
    def get_path(self):
        return self.path
    def set_path(self,x):
        self.path=x
    def get_figure(self):
        return self.figure
    def get_pic(self):
        return self.pic
    def get_music(self):
        return self.mymusic
    def get_js(self):
        return self.js
    def set_attributes(self,name):
        self.myattributes=name
    def get_attributes(self):
        return self.myattributes
    def set_uploads(self,name):
        self.upload=name
    def set_params(self,x):
        self.params=x
    def get_params(self):
        return self.params
    def get_uploads(self):
        return self.upload
    def get_upload(self):
        return self.upload
    def get_html(self):
        return self.get_figure().render_figure().encode()
    def file(self,params):
        print("frgthjk")
    def set_cookies(self,w):
        self.cookies=w
    def get_cookies(self):
        return self.cookies
    def set_mydatafunc(self,w):
        self.mydatafunc=w
    def get_mydatafunc(self):
        return self.mydatafunc
    def work(self,params,session={},data={},cookies=False):
        loc={"self":self, "params": params}

        loc["session"]=session
        loc["params"]=params
        loc["data"]=data
        print("THIS = MY COOKIES",cookies.get_dict())
        x=cookies.get_dict()
        try:
            print(x["current_user"])

        except:
            x["current_user"]=None


        loc["cookies"]=x
        exec("myvar=self", globals(), loc)
        exec("myvar.set_my_session(session)", globals(), loc)
        exec("myvar.set_mydatafunc(data)", globals(), loc)
        exec("myvar.set_cookies(cookies)", globals(), loc)
        exec("myvar.figure.set_session(cookies)", globals(), loc)
        exec("myvar.set_params(params)", globals(), loc)
        exec("myvar.{myfunc}(params)".format(myfunc=self.path), globals(), loc)

        return loc["myvar"]

