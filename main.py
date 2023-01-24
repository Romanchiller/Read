with open('data.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        name = line.strip()
        ingridients_number = int(f.readline())
        ingridients = []
        for i in range(ingridients_number):
            ing = f.readline().strip()
            product, number, unit = ing.split('|')
            ingridients.append({'product': product,
                                'number': int(number),
                                'unit': unit})
        f.readline()
        cook_book[name] = ingridients


print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ing_list = []
    res = {}
    for key, value in cook_book.items() :
        if key in dishes:
            ing_list += value
    for el in ing_list:
        el['number'] = el['number']*person_count
        if el['product'] in res:
            res[el['product']]['number'] += el['number']
        else:
            res[el.pop('product')] = el
    return print(res)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)

