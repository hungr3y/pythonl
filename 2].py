# d = {'a': [127,], 'b': [128,], 'c': [130,]}
#
# def update_dictionary(d, key, value):
#     keys = d.keys()
#     for kek in keys:
#         if kek == key:
#             d[key].append(value)
#         elif key not in keys:
#             newkey = 2*key
#             if newkey in keys:
#                 d[newkey].append(value)
#             else:
#                 d[newkey] = value
#                 break
#
#
# update_dictionary(d, 5, 200)
# print(d)

#***********************************************

d = {'a': [127, ], 'b': [128, ], 'c': [130, ]}


def update_dictionary(dict_test, key, value):
    keys = dict_test.keys()
    if key in keys:
        dict_test[key].append(value)
    else:
        if key*2 in keys:
            dict_test[key*2].append(value)
        else:
            dict_test[key*2] = [value,]

update_dictionary(d, 5, 200)
print(d)

