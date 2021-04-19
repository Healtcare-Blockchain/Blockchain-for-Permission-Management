import json

def open_json():
    # read file
    with open('Connection_Settings.json', 'r') as connectionfile:
        data=connectionfile.read()

    # parse file
    obj = json.loads(data)

    return obj

def save_json(obj):
    with open('Connection_Settings.json', 'w') as connectionfile:
        try:
            json.dump(obj, connectionfile)
            return 'Saved successfully'
        except:
            return 'Something went wrong'


def get_default():
    obj = open_json()
    for x in obj:
        if obj[x]['default'] == 'true':
            return x

def connection_settings():
    obj = open_json()
    link = obj[get_default()]['HTTPProvider']['link']
    port = obj[get_default()]['HTTPProvider']['port']
    connection_string = link + ":" + port
    return connection_string

def set_default():
    old_default = get_default()
    print("Existing connections:")
    list_settings()
    new_default = input("\nChose a connection to make default:\n")

    if new_default == old_default:
        return('This is already your default connection setting')
    else:
        obj = open_json()
        for x in obj:
            if x == new_default:
                obj[new_default]['default'] = 'true'
                obj[old_default]['default'] = 'false'
                return save_json(obj)
        choice = input ('This is not an existing connection want to create a new one? y|n')
        if  choice == 'y':
            return 'not yet implemented'
        elif  choice == 'n':
            return 'not yet implemented'

def list_settings():
    obj = open_json()
    for x in obj:
        print(x)

def change_connection_settings():
    # TODO
    return 0

def create_connection_settings():
    # TODO
    return 0


# {
#     "development": {
#         "default": "false",
#         "HTTPProvider": {
#             "link": "http://127.0.0.1",
#             "port": "8085"
#         }
#     },
#     "private_chain": {
#         "default": "true",
#         "HTTPProvider": {
#             "link": "http://104.248.81.215",
#             "port": "8545"
#         }
#     }
# }