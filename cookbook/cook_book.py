import pprint


def parse_recipes():
	cook_book = {}
	with open("recipes.txt", encoding="UTF-8") as f:
		cont = f.read().strip().split("\n\n")
	for line in cont:
		parts = line.split("\n")
		dish_name = parts[0]
		cook_book[dish_name] = []
		for ingredient_line in parts[2:]:
			ingredient_name, quantity, measure = map(str.strip, ingredient_line.split("|"))
			cook_book[dish_name].append({
				"ingredient_name": ingredient_name,
				"quantity": int(quantity),
				"measure": measure,
			})
	return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
	menu = {}
	for dish in dishes:
		if dish in cook_book:
			for ingredient in cook_book[dish]:
				if ingredient["ingredient_name"] in menu:
					menu[ingredient["ingredient_name"]]["quantity"] += int(ingredient["quantity"] * person_count)
				else:
					menu[ingredient["ingredient_name"]] = {
						"measure": ingredient["measure"],
						"quantity": int(ingredient["quantity"] * person_count)
					}
		else:
			print("Такого блюда нет")
	return menu


cook_book = parse_recipes()
pprint.pprint(get_shop_list_by_dishes(cook_book, ["Омлет", "Омлет"], 2))
pprint.pprint(get_shop_list_by_dishes(cook_book, ["Омлет", "Утка по-пекински", "Запеченный картофель"], 1))