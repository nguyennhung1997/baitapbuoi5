# 1
from datetime import date

def day_diff(release_date, code_complete_day):
    release_date = release_date.split('/')
    code_complete_day= code_complete_day.split('-')
    formated_release_date = date(int(release_date[2]), int(release_date[1]),  int(release_date[0]))
    formated_code_complete_day = date(int(code_complete_day[0]), int(code_complete_day[2]),  int(code_complete_day[1]))
    date_for_testing = formated_release_date - formated_code_complete_day
    return date_for_testing.days
# day_diff()

# 2
def alpha_num(input):
    str_list = input.split()
    text_contain_num_list = []
    for i in str_list:
        if any(chr.isdigit() for chr in i):
            text_contain_num_list.append(i)
    # if len(text_contain_num_list) == 0:
    #     print("Không có từ nào bao gồm chữ số trong chuỗi đã nhập.")
    # else:
    #     print(text_contain_num_list)
    # pass
    return text_contain_num_list