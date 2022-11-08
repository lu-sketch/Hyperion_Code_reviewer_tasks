### ISBN numbers ###

list1 = [9, 8, 7, 1, 3, 5, 4, 8, 7, 1, 3, 1, 5]
list2 = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
list3 = [0, 3, 4, 3, 0, 0, 3, 5, 7, 0]
list4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def isbn13():
    """ This function determines if the number entered as an ISBN-13 number,
    is a valid ISBN-13 number"""
    result_isbn13 = [num1 * num2 for num1, num2 in zip(list1, list2)]
    print(result_isbn13)
    total13 = sum(map(int, result_isbn13))
    print('Total : ', total13)
    for x in range(0, len(list1)):
        result_isbn13.append(list1[x] * list2[x])
    if total13 % 10 == 0:
        my_lst_str = ''.join(map(str, list1))
        print('Valid ISBN-13', my_lst_str)
    else:
        print('Invalid ISBN-13')


def isbn10():
    """ This function determines if the number entered as an ISBN-10 number,
       is a valid ISBN-10 number"""
    result_isbn10 = [i1 * i2 for i1, i2 in zip(list3, list4)]
    print(result_isbn10)
    total10 = sum(result_isbn10)
    print('Total : ', total10)
    convert_list = [9,8,7]
    for x in range(0, len(list3)):
        result_isbn10.append(list3[x] * list4[x])
    if total10 % 11 == 0:
        print('Valid ISBN-10')
        converted_isbn10 = list3 + convert_list
        my_lst_str = ''.join(map(str, converted_isbn10))
        print('Converted ISBN-10 to ISBN-13 : ', my_lst_str)

    else:
        print('Invalid ISBN-10')


isbn13()
isbn10()
