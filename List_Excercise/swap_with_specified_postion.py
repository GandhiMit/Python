
def swap_based_position(list1, pos1, pos2):

    list1[pos1], list1[pos2] = list1[pos2], list1[pos1]

    return list1


def swap_pop_method(list_l, pos11, pos21):

    fele = list_l.pop(pos11)
    sele = list_l.pop(pos21)

    # Insert
    list_l.insert(pos11, sele)
    list_l.insert(pos21, fele)

    return list_l


if __name__=='__main__':

    list_ideal = [1, 2, 3, 4, 5]
    # pos_1, pos_2 = 1, 3
    # new_list = swap_based_position(list_ideal, pos_1, pos_2)
    # print(new_list)

    pos1, pos2= 2,3
    new_lisr_pop= swap_pop_method(list_ideal, pos1, pos2)
    print(new_lisr_pop)