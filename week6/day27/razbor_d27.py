"""
Классная работа
По теме: Инкапсуляция

Создайте класс Terminal. Создайте объект-карточку от этого
класса, передав номер своей карточки и пин код. При этом,
необходимо проверить валидность карточки: номер карточки
должен содержать строго 16 цифр, а пин код - 4 цифры (для этого
используйте инкапсуляцию). При создании карточки в ней
содержится 0 сом. Далее в классе должны быть следующие
методы:

 метод put, который будет принимать в качестве
аргументов: пин код карточки, вторым аргументом -
сумму денег, которую вы хотите закинуть на эту
карточку. Прежде, чем закидывать деньги, необходимо
проверить введенный пин код на совпадение
(используйте инкапсуляцию)

 метод get_money, который также принимает первым
аргументом пин код, вторым аргументом - сумму денег,
которую вы хотите извлечь из карточки. Здесь также
необходимо использовать валидацию: проверка пин
кода + сумма денег должна быть округленной до
десятичных чисел, типа 10, 100, 200, 5000 и т.д. (67,
899, 45.6 - невалидные данные). И только после
проверки деньги извлекаются.

Примените данные методы к своей карточке несколько раз и в
конце выдайте, сколько денег на карточке. Примечание: нельзя
извлечь сумму денег, если она больше, чем сумма денег на
карточке; также нельзя вытащить пин код карточки (эти данные
должны быть скрыты)
"""

class Terminal:

    def _check_card(self, card):
        if len(card) == 16 and card.isdigit():
            return True
        else:
            print('Invalid card number')

    def _check_pin(self, pin):
        if len(pin) == 4 and pin.isdigit():
            return True
        else:
            print('Invalid PIN')

    def __init__(self, card, pin):
        if self._check_card(card=card) and self._check_pin(pin=pin):
            self.__card = card
            self.__pin = pin
            self.money = 0
        else:
            print('Card is not initialized')

    def _validation(self, pin):
        if self.__pin == pin:
            return True
        else:
            return False

    def put(self, pin, money):
        if self._validation(pin=pin):
            self.money += money
            print(f'You have {self.money} on balance')
        else:
            print(f'Incorrect PIN!')

    def _check_money(self, money):
        if money % 10 == 0:
            return True
        else:
            print("Invlid amount of money")
            return False

    def _check_balance(self, money):
        if self.money < money:
            print('Insufficient Balance')
            return False
        else:
            return True

    def get_money(self, pin, money):
        if self._validation(pin=pin):
            if self._check_money(money=money) and self._check_balance(money=money):
                self.money -= money
                print(f"You have {self.money} on balance")
        else:
            print("Incorrect PIN!")

card = Terminal(card='1234567812345678', pin='9811')
card.put(pin='9811', money=1000)
card.get_money(pin='9811', money=800)
card.put(pin='9811', money=7000)
print(card.money)


card2 = Terminal(card='0987654312348971', pin='2968')
card2.put(pin='2968', money=2000)
card2.get_money(pin='2968', money=300)
print(card2.money)


# getter  setter сами используйте для получения приватных данных ;)