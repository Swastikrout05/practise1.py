a = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
a = list(dict.fromkeys(a))
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b = list(dict.fromkeys(b))
Overlapping_list = []

if len(a)<len(b):
    for num in a:
        if num in b:
            print(num)
            Overlapping_list.append(num)
    print('Done!')

if len(b)>len(a):
    for num in b:
        if num in a:
            print(num)
            Overlapping_list.append(num)
    print('Done!!')

print('Overlapping_list')