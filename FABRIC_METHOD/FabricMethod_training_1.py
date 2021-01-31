class English():
    def talk(self):
        print("Eng, hello!")

class Franch():
    def talk(self):
        print("France, bonjour")

############################################
def intro(lang):
    lang.talk()

intro(Franch())
intro(English())
#=============================================

class Parent:
    def action(self):
        print("parent talk")

class Child(Parent):
    def action(self):
        print("Child listen")

c = Child()

c.action()