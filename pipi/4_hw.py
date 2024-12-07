# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого.
# Результаты выводить в консоль.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def sguare(self):
        print(self.width * self.height)

    def perimeter(self):
        print((self.width + self.height)*2)

rectangle_1=Rectangle(8,5)
rectangle_1.sguare()
rectangle_1.perimeter()

rectangle_2=Rectangle(5,11)
rectangle_2.sguare()
rectangle_2.perimeter()

rectangle_3=Rectangle(2,10)
rectangle_3.sguare()
rectangle_3.perimeter()

# 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b
# с ними нужно производить соответствующие действия и печатать ответ.

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

object=Math(6,3)
object.addition()
object.multiplication()
object.division()
object.subtraction()

# 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает
# текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Button:
    type: str= 'Кнопка'

    def __init__(self, text, loc=None):
        self.text = text
        self.loc = loc

    def click(self):
        print (f'Клик по кнопке  {self.text}')

text_box=Button('Text Box')
print(text_box.text)
text_box.click()

check_box=Button('Check Box')
print(check_box.text)
check_box.click()

radio_button=Button('Radio Button')
print(radio_button.text)
radio_button.click()

web_tables=Button('Web Tables')
print(web_tables.text)
web_tables.click()

buttons=Button('Buttons')
print(web_tables.text)
buttons.click()

links=Button('Links')
print(links.text)
links.click()

broken_links_images=Button('Broken Links - Images')
print(broken_links_images.text)
broken_links_images.click()

upload_and_download=Button('Upload and Download')
print(upload_and_download.text)
upload_and_download.click()

dynamic_properties=Button('Dynamic Properties')
print(dynamic_properties.text)
dynamic_properties.click()

practice_form=Button('Practice Form')
print(practice_form.text)
practice_form.click()

browser_windows=Button('Browser Windows')
print(browser_windows.text)
browser_windows.click()

alerts=Button('Alerts')
print(alerts.text)
alerts.click()

frames=Button('Frames')
print(frames.text)
frames.click()

nested_frames=Button('Nested Frames')
print(nested_frames.text)
nested_frames.click()

modal_dialogs=Button('Modal Dialogs')
print(modal_dialogs.text)
modal_dialogs.click()

accordian=Button('Accordian')
print(accordian.text)
accordian.click()

auto_complete=Button('Auto Complete')
print(auto_complete.text)
auto_complete.click()

date_picker=Button('Date Picker')
print(date_picker.text)
date_picker.click()

slider=Button('Slider')
print(slider.text)
slider.click()

progress_bar=Button('Progress Bar')
print(progress_bar.text)
progress_bar.click()

tabs=Button('Tabs')
print(tabs.text)
tabs.click()

tool_tips=Button('Tool Tips')
print(tool_tips.text)
tool_tips.click()

menu=Button('Menu')
print(menu.text)
menu.click()

select_menu=Button('Select Menu')
print(select_menu.text)
select_menu.click()

sortable=Button('Sortable')
print(sortable.text)
sortable.click()

selectable=Button('Selectable')
print(selectable.text)
selectable.click()

resizable=Button('Resizable')
print(resizable.text)
resizable.click()

defroppable=Button('Droppable')
print(defroppable.text)
defroppable.click()

dragabble=Button('Dragabble')
print(dragabble.text)
dragabble.click()

login=Button('Login')
print(login.text)
login.click()

book_store=Button('Book Store')
print(book_store.text)
book_store.click()

profile=Button('Profile')
print(profile.text)
profile.click()

book_store_api=Button('Book Store API')
print(profile.text)
profile.click()
