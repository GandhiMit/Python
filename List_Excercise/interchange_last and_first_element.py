
def swap_List(list):

    size = len(list)
    temp= list[0]

    list[0]= list[size-1]

    list[size-1]= temp

    return list


def swap_list_alt(list):

    list[0], list[-1] = list[-1], list[0]

    return list


list_1 = [10, 11, 22, 32]

new_list= swap_List(list_1)
print(new_list)

new_list_alt= swap_list_alt(list_1)
print(new_list_alt)
