class Button:
    html = ""
    def getHTML(self, typ):
        if typ == 'image':
            self.html = "<img> some_image </img>"
            return self.html
        elif typ == 'input':
            self.html = "<input> some_input </input>"
            return self.html
        if typ == 'flash':
            self.html = "<obj> some_object </obj>"
            return self.html
        if typ == 'text':
            self.html = "<txt> some_text </txt>"
            return self.html
    
buttonObj = Button()
button = ["image", "input", "flash", "text"]

for butt in button:
    print(buttonObj.getHTML(butt))
