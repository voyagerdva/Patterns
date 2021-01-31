class Controller():
    def action(self):
        pass

class Action1(Controller):
    def action(self):
        print("Action 1")

class Action2(Controller):
    def action(self):
        print("Action 2")

######################################
Action1().action()
Action2().action()

