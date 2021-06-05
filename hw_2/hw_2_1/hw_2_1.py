import csv
import re


def get_data():
    columns = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    main_data = [columns, ]

    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']

    for file in file_list:
        with open(file) as f:
            f_reader = f.read()
            for column in columns:
                reg_str = re.search(r'{}[^\n]*'.format(re.escape(column)), f_reader)
                value = (reg_str.group().split('   ')).pop()
                if column == 'Изготовитель системы':
                    os_prod_list.append(value)
                elif column == 'Название ОС':
                    os_name_list.append(value)
                elif column == 'Код продукта':
                    os_code_list.append(value)
                elif column == 'Тип системы':
                    os_type_list.append(value)

    for i in range(len(file_list)):
        temp = [os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]]
        main_data.append(temp)

    return main_data


def write_to_csv(file):
    data = get_data()
    with open(f'{file}.csv', 'w') as f:
        f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        f_writer.writerows(data)

    with open(f'{file}.csv') as f:
        print(f.read())


write_to_csv('')
