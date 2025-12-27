def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """
    Создает список покупок на основе списка блюд и количества персон.

    Args:
        dishes (list): Список названий блюд.
        person_count (int): Количество персон.
        cook_book (dict): Словарь с рецептами блюд.

    Returns:
        dict: Словарь с ингредиентами и их количеством.
    """
    shop_list = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredient in cook_book[dish_name]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Рецепт для блюда '{dish_name}' не найден!")  # Обработка отсутствия рецепта
    return shop_list

# Пример использования (нужно предоставить cook_book)
cook_book = {
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 2, 'measure': 'кг'},
        {'ingredient_name': 'Молоко', 'quantity': 200, 'measure': 'мл'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 200, 'measure': 'г'},
        {'ingredient_name': 'Чеснок', 'quantity': 6, 'measure': 'зубч'}
    ],
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 1, 'measure': 'шт'}
    ]
}

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(shop_list)