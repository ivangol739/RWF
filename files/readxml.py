import os
import xml.etree.ElementTree as ET

def read_files(file_path):
    parser = ET.XMLParser(encoding="UTF-8")
    tree = ET.parse(file_path, parser)
    return tree


def parse_xml(word_max_len=6, top_words_amt=10):
    text = ""
    root = read_files(file_path).getroot()
    new_list = root.findall("channel/item")
    for item in new_list:
        text += item.find("description").text + " "
    text_list = text.split()

    long_worlds_list = []
    for word in text_list:
        if len(word) > word_max_len:
            long_worlds_list.append(word)

    word_count = {}
    for long_word in long_worlds_list:
        if long_word in word_count:
            word_count[long_word] += 1
        else:
            word_count[long_word] = 1

    sort_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:top_words_amt]
    result_list = [word for word, count in sort_word_count]
    return result_list


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(), "data", "newsafr.xml")
    parse_xml()
