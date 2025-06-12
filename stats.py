
def sort_on(dict):
    return dict["count"]


def sort_a_dict(dict_to_sort):
    list_of_dicts_to_sort = []
    for char, count in dict_to_sort.items():
        list_of_dicts_to_sort.append({"char":char, "count":count})
    list_of_dicts_to_sort.sort(reverse=True, key=sort_on)
    return list_of_dicts_to_sort


def count_str_words(str_to_count):
    return len(str_to_count.split())

def count_str_chars(str_to_count):
    char_counts = {}
    for c in str_to_count.lower():
        try:
            char_counts[str(c)] += 1
        except KeyError:
            char_counts[str(c)] = 1
    return char_counts