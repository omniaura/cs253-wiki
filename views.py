import utils

class ViewPage(utils.Handler):
    def get(self):
        self.render("edit.html", login=False)

class EditPage(utils.Handler):
    pass

class Register(utils.Handler):
    pass

class Login(utils.Handler):
    pass