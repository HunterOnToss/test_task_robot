#! -*- coding: utf-8 -*-


def sort_list(linked_list):
    result_list = []
    first_idx = 0
    last_idx = len(linked_list) - 1

    while len(result_list) < len(linked_list):
        last_elem = linked_list[last_idx]
        first_elem = linked_list[first_idx]

        result_list.append(first_elem)
        result_list.append(last_elem)

        first_idx += 1
        last_idx -= 1

    return result_list


if __name__ == "__main__":
    link_list = [1, 2, 3, 4, 5, 6, 7, 8]
    result = sort_list(linked_list=link_list)
    print "До сортировки:    {}".format(link_list)
    print "После сортировки: {}".format(result)
