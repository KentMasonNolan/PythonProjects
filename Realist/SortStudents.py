def sort_by_mark(my_class):
    output = sorted(my_class, reverse=True)
    return output


def sort_by_name(my_class):
    output = sorted(my_class, key=lambda a: a[1])
    return output


my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

print(sort_by_mark(my_class))
print(sort_by_name(my_class))
