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
        x=Db().createitem((self.name, self.image,self.price,self.date))
        return x
    def set_price(self,string):
        self.price=string
    def get_price(self,string):
        return self.price
    def set_name(self,string):
        self.name=string
    def get_name(self,string):
        return self.name

    def set_date(self,string):
        self.date=string
    def get_date(self,string):
        return self.date

