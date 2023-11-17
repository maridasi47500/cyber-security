from myfunc import Myfunc
from fichier import Fichier
import subprocess
class Php(Myfunc):
    def __init__(self,name):
        self.name=name
        x=Fichier("./phishing",name.split("/")[-1]).lirefichier()
        #proc = subprocess.Popen("php ./phishing"+name.split("/")[-1], shell=True, stdout=subprocess.PIPE)
        #script_response = proc.stdout.read()
        self.content=x
        self.php=True

    def get_html(self):
        return self.content
