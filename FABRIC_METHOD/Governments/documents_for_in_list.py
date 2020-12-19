# coding: utf-8

class Document:
    def show(self):
        print("Some default document!!!")
    
class ODFDocument(Document):
    def show(self):
        print("ODF format")
    
class MSOfficeDocument(Document):
    def show(self):
        print("MS Office document format")
        

# class Application:
#     def createDocument(self, typ):
#         # параметризованный ФМ "createDocument"
#         raise NotImplementedError()
    
class MyApplication():
    def createDocument(self, typ):
        if typ == "odf":
            return ODFDocument()
        elif typ == "doc":
            return MSOfficeDocument()
        else:
            return Document()
        

app = MyApplication()

formatList = ["odf", "doc"]

for format in formatList:
    app.createDocument(format).show()
    
app.createDocument("xls").show()
            
