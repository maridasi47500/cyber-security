from mymodel import Mymodel
from db import Db
class Myrecording(Mymodel):
    def set_image(self,uploaded_io):
        if isinstance(uploaded_io, list):
            for record in uploaded_io:
                open("./uploads/%s"%record.filename, "wb").write(record.file.read())
        else:
            open("./uploads/%s"%uploaded_io.filename, "wb").write(uploaded_io.file.read())
        print("name")
        self.image=uploaded_io.filename
    def get_image(self):
        return self.image
    def create(self):
        x=Db().createitem((self.title, self.image, self.price))
    def set_price(self,string):
        self.price=string
    def get_price(self,string):
        return self.price
    def set_title(self,string):
        self.title=string
    def get_title(self,string):
        return self.title


