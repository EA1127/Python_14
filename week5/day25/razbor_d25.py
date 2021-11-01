"""
Task-1

Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, 
Telegram. При регистрации в WhatsApp и SnapChat необходимо передавать свой номер 
телефона, который должен быть int. При регистрации в Telegram необходимо передавать
номер телефона и username. Во всех классах есть метод send, в WhatsApp он принимает 
только text и выдает строку “I am sending a text ...” и вместо … должен быть сам 
текст сообщения. В SnapChat send принимает image и text, при этом image должен быть 
булевым типом данных. Если image True, то выдается сообщение 
“I am sending a text … with some image ”, 
если  False - сообщение “I am sending a text … without image”. 
В Telegram метод send принимает voice message в виде строки и выдает сообщение
“I am sending a voice message ...”. Создайте объекты от этих классов и вызовите 
метод send у всех объектов.
"""

class WhatsApp:

    def __init__(self, phone:int):
        self.phone = phone

    def send(self, text:str):
        print(f"I'm sending a message {text}")

class SnapChat:
    def __init__(self, phone:int):
        self.phone = phone

    def send(self, image:bool, text:str):
        if image:
            print(f"I'm sending a text {text} with some image")
        else:
            print(f"I'm sending a text {text} without image")

class Telegram:
    def __init__(self, phone:int, username:str):
        self.phone = phone
        self.username = username

    def send(self, voice_message:str):
        print(f"I'm sending a message {voice_message}")

obj1 = WhatsApp(996555777111)
obj1.send('Hello Makers!!!')

obj2 = SnapChat(996555888444)
obj2.send(image=True, text='Whats going on?')

obj3 = SnapChat(996700222333)
obj3.send(image=False, text='heeeeeey!!!')

obj4 = Telegram(996500666999, 'easy_bootcamp14')
obj4.send(voice_message='ufffffff what you want...')


"""
Task-2

Создайте два класса A и B. В обоих классах есть метод count. В классе A 
он подсчитывает, сколько гласных букв в слове, которое передается в качестве 
аргумента в методе count, а в классе B он подсчитывает количество согласных. 
Создайте объекты от этих классов и вызовите этот метод у каждого объекта.
"""

class A:
    def count(self, word:str):
        self.count = 0
        vowels = ['a', 'o', 'y', 'i', 'e', 'o', 'u']
        for letter in word:
            if letter in vowels:
                self.count += 1
        return self.count

class B:
    def count(self, word:str):
        self.count = 0
        vowels = ['a', 'o', 'y', 'i', 'e', 'o', 'u']
        for letter in word:
            if letter.isalpha() and letter not in vowels:
                self.count += 1
        return self.count
        
a = A()
print(a.count('Makers14$%!'))

b = B()
print(b.count("Bootcamp_14@&*"))