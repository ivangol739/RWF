import json
import os
import pprint
from collections import Counter

def read_file_json(file_path):
	with open(file_path, encoding="UTF-8") as f:
		return json.load(f)


def parse_json():
	text = ""
	json_data = read_file_json(file_path)
	for i in json_data["rss"]["channel"]['items']:
		text += i["description"] + " "
	return text


def max_repeat_worlds(word_max_len=6, top_words_amt=10):
	words_list = []
	text = parse_json().split()
	for word in text:
		if len(word) > word_max_len:
			words_list.append(word)

	world_count = {}
	for item in words_list:
		if item in world_count:
			world_count[item] += 1
		else:
			world_count[item] = 1

	world_count_sort = sorted(world_count.items(), key=lambda x: x[1], reverse=True)[:top_words_amt]
	print(world_count_sort)
	top_10_word_list = [word for word, count in world_count_sort]
	print(top_10_word_list)
	return top_10_word_list


if __name__ == "__main__":
	file_path = os.path.join(os.getcwd(), "data", "newsafr.json")
	parse_json()
	max_repeat_worlds()


#