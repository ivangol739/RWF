import os
import pprint

def read_file(file_path):
	with open(file_path, "r", encoding="UTF-8") as f:
		return f.readlines()


def read_files(file_paths):
	text_in_files = {}

	for file_path in file_paths:
		try:
			content = read_file(file_path)
			text_in_files[len(content)] = [os.path.basename(file_path), content]
		except Exception as e:
			print(f"Ошибка при чтении файла {file_path}: {e}")
	return text_in_files


def sort_and_write(files, output_path):
	with open(output_path, "w", encoding="UTF-8") as finalfiles:
		long_files = sorted(files.keys(), reverse=False)
		for long in long_files:
			finalfiles.write(f"{files[long][0]} \n")
			finalfiles.write(f"{str(long)} \n")
			finalfiles.write(f"{''.join(files[long][1])} \n")


if __name__ == "__main__":
	file_paths = [
		os.path.join(os.getcwd(), "data", "1.txt"),
		os.path.join(os.getcwd(), "data", "2.txt"),
		os.path.join(os.getcwd(), "data", "3.txt")
	]

	text_in_files = read_files(file_paths)
	sort_and_write(text_in_files, "finalfiles.txt")
