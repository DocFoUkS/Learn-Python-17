# -*- coding: utf-8 -*-


def discounted(price, discount, max_discount=20):
    """
        Функция для расчета цены с учетом скидок
    """
    # Проверка на правильный тип значений вводимых аргументов
    if type(price) not in (int, float):
        raise ValueError('Неверно введен аргумент price')
    elif type(discount) not in (int, float):
        raise ValueError('Неверно введен аргумент discount')
    elif type(max_discount) not in (int, float):
        raise ValueError('Неверно введен аргумент max_discount')
    else:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)


if __name__ == "__main__":
    print(discounted(12323, 15))
    print(discounted('12323', 15))
