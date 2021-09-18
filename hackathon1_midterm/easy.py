# 1
def day_diff():
    release_date = input('Nhập ngày release sản phẩm (dd/mm/yyyy): ')
    release_date = release_date.split("/")
    code_complete_day = input('Nhập ngày hoàn thành code (yyyy-dd-mm): ')
    code_complete_day = code_complete_day.split("-")

    from datetime import date
    formated_release_date = date(int(release_date[2]), int(release_date[0]),  int(release_date[1]))
    formated_code_complete_day = date(int(code_complete_day[0]), int(code_complete_day[1]),  int(code_complete_day[2]))
    date_for_testing = formated_release_date - formated_code_complete_day
    print(date_for_testing)
    pass
# day_diff()

# 2
def alpha_num():
    str = input("Nhập chuỗi string: ")
    str_list = str.split()
    text_contain_num_list = []
    for i in str_list:
        if any(chr.isdigit() for chr in i):
            text_contain_num_list.append(i)
    if len(text_contain_num_list) == 0:
        print("Không có từ nào bao gồm chữ số trong chuỗi đã nhập.")
    else:
        print(text_contain_num_list)
    pass
# alpha_num()