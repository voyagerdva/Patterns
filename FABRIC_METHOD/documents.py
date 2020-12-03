# coding: utf-8

class Document:
    def show(self):
        raise NotImplementedError()
    
class ODFDocument(Document):
    def show(self):
        print("ODF format")
        
class MSOfficeDocument(Document):
    def show(self):
        print("MS Office document format")
        
class Application:
    def createDocument(self, typ):
        # параметризованный ФМ "createDocument"
        raise NotImplementedError()
    
class MyApplication(Application):
    def createDocument(self, typ):
        if typ == "odf":
            return ODFDocument()
        elif typ == "doc":
            return MSOfficeDocument()
        

app = MyApplication()
app.createDocument("odf").show()
app.createDocument("doc").show()
#            
