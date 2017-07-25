import datetime
import os


def check_date_type(date):
    """
    funct for check all date, format - yyyy-mm-ddThh:mm:ss.ms
    :param date: yyyy-mm-ddThh:mm:ss.ms
    :return: bool
    """

    if int(date.split('T')[0].split('-')[0]) < 2000:
        return False
    if int(date.split('T')[0].split('-')[1]) not in range(1, 13):
        return False
    if int(date.split('T')[0].split('-')[2]) not in range(1, 32):
        return False
    if int(date.split('T')[1].split(':')[0]) not in range(0, 24):
        return False
    if int(date.split('T')[1].split(':')[1]) not in range(0, 60):
        return False
    if date.split('T')[1].split(':')[2][-1] != 'Z':
        last_part = date.split('T')[1].split(':')[2]
    else:
        last_part = date.split('T')[1].split(':')[2][0:-1]
    if not float(last_part):
        if last_part != '00':
            return False

    return True


def check_type(var_type, var, var_name, message):
    """
    funct for check type of required param
    :param var_type: type like int, unicode ect
    :param var: variable
    :param var_name: name of variable
    :param message: error message
    :return: bool
    """

    result = True
    if not isinstance(var_type, tuple):
        var_type = (var_type,)

    if None in var_type:
        var_type += (type(None), )

    if 'date' in str(var_type).lower():
        check_result = check_date_type(var) or type(var) in var_type
    else:
        check_result = type(var) in var_type

    if not check_result:
        print(message.format(var_name, var_type, type(var), var))
        result = False

    if not result:
        logger(message.format(var_name, var_type, type(var), var))

    assert result, message.format(var_name, var_type, type(var), var)

    return result


def check_data_in_dict(dct, tuple_var_types, err_msg):
    """
    check data for every element in dict

    element = {'key': 1}
    check_data_in_json_object(element, (key, int), error_msg)

    :param dct: dict
    :param tuple_var_types: keys and types, can be tuple_var_types = (dict_key, type(dict_key)) or
    (('key1', 'key2'), (type1_key, type2_key)), type can be None and 'Date'
    :return: True if all ok, False if there are any mistakes
    """

    result = []

    dict_keys = tuple_var_types[0]
    if not isinstance(dict_keys, tuple):
        dict_keys = (dict_keys, )
    for dict_key in dict_keys:
        result.append(check_type(tuple_var_types[1], dct.get(dict_key), dict_key, err_msg))

    if False in result:
        return False
    else:
        return True


def check_data_in_list(lst, tuple_var_types, err_msg):
    """
    check data for every element in list
    a_lst = [{...}, {...}]
    # you can check it:
    if check_data_in_list(a_lst, dict, error_msj):
        for element in a_lst:
        ...

    :param lst: list
    :param tuple_var_types: type of list_elements, can be tuple_var_types = type() or tuple(type())
    :return: True if all ok, False if there are any mistakes
    """

    result = []

    if type(tuple_var_types) is not tuple:
        tuple_var_types = (tuple_var_types,)
    if 'date' not in str(tuple_var_types).lower():
        for lst_element in lst:
            result.append(check_type(tuple_var_types, lst_element, 'element', err_msg))

    if False in result:
        return False
    else:
        return True


def logger(*args, **kwargs):
    """
    Log all params in file. every day, every hour
    :return:
    """
    path_first_part = 'D:\\ApiTestLogs\\'
    path = '{0}{1}\\'.format(path_first_part, datetime.datetime.strftime(datetime.datetime.now(), '%y/%m/%d'))\
        .replace(r'/', '_')
    if not os.path.exists(path_first_part):
        os.mkdir(path_first_part)
    if not os.path.exists(path):
        os.mkdir(path)
    file_name = '{0}-00.txt'.format(datetime.datetime.strftime(datetime.datetime.now(), '%H'))

    f = open(path + file_name, 'a+')
    f.write('\n{0}\n'.format(datetime.datetime.now()))
    for key in kwargs:
        f.write('{0}:{1}\n'.format(key, kwargs[key]))
    for k in args:
        f.write('{0}\n'.format(k))
