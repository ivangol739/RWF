import os
import pprint


def read_files():
	text_in_files = {}

	current_dir = os.getcwd()
	file_path1 = os.path.join(current_dir, "data", "1.txt")
	file_path2 = os.path.join(current_dir, "data", "2.txt")
	file_path3 = os.path.join(current_dir, "data", "3.txt")

	with open(file_path1, "r", encoding="UTF-8") as f1:
		content1 = f1.readlines()
		text_in_files[len(content1)] = ["1.txt", content1]

	with open(file_path2, "r", encoding="UTF-8") as f2:
		content2 = f2.readlines()
		text_in_files[len(content2)] = ["2.txt", content2]

	with open(file_path3, "r", encoding="UTF-8") as f3:
		content3 = f3.readlines()
		text_in_files[len(content3)] = ["3.txt", content3]

	return text_in_files


def sort_and_write(files):
	with open("finalfiles.txt", "a", encoding="UTF-8") as finalfiles:
		long_files = sorted(files.keys(), reverse=False)
		for long in long_files:
			finalfiles.write(f"{files[long][0]} \n")
			finalfiles.write(f"{str(long)} \n")
			finalfiles.write(F"{''.join(files[long][1])} \n")
		return

text_in_files = read_files()
sort_and_write(text_in_files)
