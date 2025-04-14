import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')

        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')

        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')

        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []

        for name in self.__name_items:
            if name in self.__item_price:
                total.append(self.__item_price[name])

        if len(total) > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for name in self.__name_items:
            if self.__tax_rate.get(name) == 20:
                twenty_percent_tax.append(name)

        for price in twenty_percent_tax:
            total.append(self.__item_price[price])

        if len(total) > 10:
            return (sum(total) * 0.2) * 0.9
        else:
            return sum(total) * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for name in self.__name_items:
            if self.__tax_rate.get(name) == 10:
                ten_percent_tax.append(name)

        for price in ten_percent_tax:
            total.append(self.__item_price[price])
            total.append(self.__tax_rate[price])

        if len(total) > 10:
            return (sum(total) * 0.1) * 0.9
        else:
            return sum(total) * 0.1

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
            num_str = str(telephone_number)
            if not num_str.isdigit():
                raise ValueError('Необходимо ввести цифры')

            if len(num_str) != 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')

            return f'+7{num_str}'


    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [['часы', lambda x: x.hour],
                ['минуты', lambda x:x.minute],
                ['день', lambda x:x.day],
                ['месяц', lambda x:x.month],
                ['год', lambda x:x.year]]

        for value in date:
            new_list = f'{value[0]}: {value[1](now)}'
            date_and_time.append(new_list)

        return date_and_time


item = OnlineSalesRegisterCollector()

item.add_item_to_cheque('молоко')
item.delete_item_from_check('молоко')
item.add_item_to_cheque('чипсы')
item.add_item_to_cheque('кефир')

print(item.number_items)
print(item.name_items)
print(item.check_amount())
print(item.twenty_percent_tax_calculation())
print(item.ten_percent_tax_calculation())
print(item.total_tax())
print(item.get_telephone_number(9098763466))
print(item.get_date_and_time())