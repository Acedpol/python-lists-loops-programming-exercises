my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here
new_list = []
for e in my_list:
    if type(e) == dict or type(e) == list:
        new_list.append(e)

print(new_list)