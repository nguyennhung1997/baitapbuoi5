import sys
from typing import Counter


def read_file(filename):
    file = open(filename, "r")
    file_content = file.read()
    file_content = file_content.lower()
    return file_content


def get_words(filename):
    file_content = read_file(filename)
    word_list = file_content.split()
    counter = Counter(word_list)
    result = sorted(counter.items())
    return result


def get_top_words(filename):
    file_content = read_file(filename)
    word_list = file_content.split()
    counter = Counter(word_list)
    result = counter.most_common(20)
    return result


def main():
    if len(sys.argv) != 3:
        print('usage: ./countword.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    words = []
    if option == '--count':
        words = get_words(filename)
    elif option == '--topcount':
        words = get_top_words(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

    for item in words:
        print(item[0], item[1])


if __name__ == '__main__':
    main()
