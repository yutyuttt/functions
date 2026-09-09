def swap(lst, ind1, ind2):
    lst[ind2], lst[ind1] = lst[ind1], lst[ind2]

lst = [1, 2, 3, 4 ,5]
print(lst)

swap(lst, 2, 3)
print(lst)