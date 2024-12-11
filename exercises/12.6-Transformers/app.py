incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
def data_transformer(data):
    # lambda user: f'{user["name"]} {user["last_name"]}' --> otra forma :)
    full_name = lambda user: user["name"] + ' ' + user["last_name"]
    return list(map(full_name,data))

print(data_transformer(incoming_ajax_data))
