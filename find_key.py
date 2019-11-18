data = {
    "A": {
        "a1": 1,
        "a2": 2,
        "a3": 3
    },
    "B": {
        "b1": {
            "b11": 4,
            "b12": 5
        },
        "b2": {
            "b21": 6,
            "b22": 7
        }
    }
}

def find_item(obj, key):
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            item = find_item(v, key)
            if item is not None:
                return item

print(find_item(data, 'b21'))
print(find_item(data, 'a1'))