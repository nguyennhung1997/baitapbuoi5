import sys
import re
import os.path

"""Baby Names exercise
Định nghĩa hàm extract_names() dưới đây và gọi từ hàm main().
Cấu trúc các tag html trong các file baby.html như sau:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
Các bước nên làm tuần tự:
 -Trích xuất năm
 -Lấy và in ra tên và thứ hạng phổ biến
 -Xây danh sách [year, 'name rank', ... ] và in ra
 -Sửa hàm main() để dùng hàm extract_names.
"""

RE_YEAR_IN = r'<h3 align="center">Popularity in (\d+)<\/h3>'
RE_RANK_ITEMS = r'<tr align="right"><td>(.+?)<\/td><td>(.+?)<\/td><td>(.+?)<\/td>'


def find_year(html_content):
    match = re.search(RE_YEAR_IN, html_content)
    # We us group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)
    if match:
        #  match <h3 align="center">Popularity in 1990</h3>
        #  group(1) 1990
        return match.group(1) or ''


def find_ranks(html_content):
    matches = re.findall(RE_RANK_ITEMS, html_content)
    results = list()
    for match in matches:
        #  match(2) Jessica
        if match:
            # append rank male
            results.append("{name} {rank}".format(name=match[1], rank=match[0]))
            # append rank female
            results.append("{name} {rank}".format(name=match[2], rank=match[0]))

    #  sort alphabet
    results.sort()
    return results


def extract_names(filename):
    with open(filename, "r", encoding='utf-8') as f:
        html_content = f.read()
        year_in = find_year(html_content)
        ranks = find_ranks(html_content)
        # add year_in to first item in list ranks
        ranks.insert(0, year_in)
        return ranks


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # Với mỗi tên file, gọi hàm extract_names ở trên và in kết quả ra stdout
    # hoặc viết kết quả ra file summary (nếu có input --summaryfile).
    for file_name in args:
        if os.path.exists(file_name):
            print(extract_names(file_name))
        else:
            print('not found: %s', file_name)


# python3 babynames.py baby1990.html baby1998.html baby2008.html
if __name__ == '__main__':
    main()