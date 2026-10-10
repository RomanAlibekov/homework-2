import pprint


def read_recipes(file_path):
    """
    Читает файл с рецептами и возвращает словарь cook_book.
    """
    cook_book = {}
    with open(file_path, encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break

            ingredients_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                line = f.readline().strip()
                ingredient_name, quantity, measure = [part.strip() for part in line.split('|')]
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure,
                })

            cook_book[dish_name] = ingredients
            f.readline()  # пропустить пустую строку

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """
    Формирует список покупок для указанных блюд на определённое число персон.
    """
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге")
            continue

        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count

            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {
                    'measure': measure,
                    'quantity': quantity,
                }

    return shop_list


def main():
    cook_book = read_recipes('recipes.txt')

    # Вывод для проверки
    for dish, ingredients in cook_book.items():
        print(f"\n{dish}:")
        for ing in ingredients:
            print(f"  {ing['ingredient_name']} — {ing['quantity']} {ing['measure']}")

    # Список покупок
    shop_list = get_shop_list_by_dishes(
        ['Запеченный картофель', 'Омлет'],
        2,
        cook_book,
    )
    print("\nСписок покупок:")
    pprint.pprint(shop_list, sort_dicts=False)


if __name__ == '__main__':
    main()