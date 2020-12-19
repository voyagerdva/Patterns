class Button:
    html = ""
    def getHTML(self):
        return self.html

class ButtonFactory():
    def createButton(self, typ):
        targetclass = typ.capitalize()  # формирует имя целевого класса (с большой буквы), совпадающего с Image, Input или Flash
        return globals()[targetclass]()


class Image(Button):
    html = "<img> some_image </img>"
    
class Input(Button):
    html = "<input> some_input </input>"
    
class Flash(Button):
    html = "<obj> some_object </obj>"
    
class Text(Button):
    html = "<txt> some_text </txt>"
        
    
""" ДЛЯ ДОБАВЛЕНИЯ НОВОГО ТИПА КНОПКИ ДОСТАТОЧНО ДОБАВИТЬ НОВЫЙ КЛАСС С НУЖНЫМ ЗНАЧЕНИЕМ КНОПКИ 
    И ДОБАВИТЬ СООТВЕТСТВУЮЩЕЕ ИМЯ В "КЛИЕНТСКИЙ" СПИСОК.
    ЕДИНЫЙ МЕТОД getHTML В ИНТЕРФЕЙСЕ BUTTON ДЕЙСТВУЕТ КАЖДЫЙ РАЗ ОДИНАКОВО, НО ВОЗВРАЩАЯ КАЖДЫЙ РАЗ РАЗНЫЕ ЗНАЧЕНИЯ ОДНОЙ И ТОЙ ЖЕ ПЕРЕМЕННОЙ html, СООТВЕТСТВУЮЩИЕ ТОМУ НАСЛЕДУЕМОМУ КЛАССУ, ЭКЗЕМПЛЯР КОТОРОГО В ТЕКУЩИЙ МОМЕНТ НА ТЕКУЩЕЙ ИТЕРАЦИИ ВЫЗЫВАЕТ ЭТОТ МЕТОД  """
   
buttonObj = ButtonFactory()
button = ["image", "input", "flash", "text"]

for butt in button:
    print(buttonObj.createButton(butt).getHTML())
