from hw4_task_9_checks import Checks

class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text
search = Input('/Вход','in')
search.check_text()

class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text
reg = Button('/Регистрация', '/Button')
print('Регистрация ' + reg.text + ' имеет расположение ' + reg.loc)
reg.check_text()

class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text
name = Title('/Заголовок', '/name')
print('Заголовок ' + name.text + ' имеет расположение ' + name.loc)
name.check_text()

class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text
url = Link('/Ссылка', '/link')
print('Ссылка ' + url.text + ' имеет расположение ' + url.loc)
url.check_text()


