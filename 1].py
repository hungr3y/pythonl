d = {'a': 127, 'b': 128, 'c': 130}
sub_dicts = {'a': {
                'a1': -10,
                'a2': -20, },
             'b': 128,
             'c': 130}
items = d.items()
print(items)
print(type(items))

li = [key, error]
print(d)

def update_dictionary(d):
    b = {}
    d['c'] = 159
    keys = d.keys()

    print(keys)
    for key in keys:
        print(f'Key is {key} value is {d[key]}')


update_dictionary(d)
