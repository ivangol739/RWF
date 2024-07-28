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


pprint.pprint(parse_recipes())
