def get_variable_name(var, scope=locals()):
    return [name for name, value in scope.items() if value is var]

def write_account(file_name, info, write_type='a'):
    f = open(file_name, write_type)
    f.write(f'This is information from {get_variable_name(info)[0]}')
    for i in str(info).split(' '):
        f.write(i + '\n')
    f.close()

def write_positions(file_name, info, write_type='a'):
    f = open(file_name, write_type)
    f.write(f'This is information from {get_variable_name(info)[0]}')
    for k in dict(info[0]):
        f.write(f'{k} : {dict(info[0])[k]}'  + '\n')
    f.close()
