#! -*- coding: utf-8 -*-
import sys

INCOMING_PARAMS_SETTING = {
    '--integer': True,
    '--boolean': True,
    '--string': False,
}


def param_value_or_none(param_name):
    count = 0
    for arg in sys.argv:
        count += 1
        if param_name in arg:
            if '=' in arg:
                return arg.split('=')[1]
            else:
                return sys.argv[count]

    return None


def help_message(file_name):
    msg = ''
    for param, required in INCOMING_PARAMS_SETTING.items():
        if not required:
            param = '[{}] '.format(param)
        msg += param + ' '
    msg = 'Use: {f_name} {msg}'.format(f_name=file_name, msg=msg)
    return msg


def getopt():

    result = []
    file_name = sys.argv[0]

    if len(sys.argv) == 1 or True in ['help' in arg for arg in sys.argv]:
        return help_message(file_name)

    for param_name, required in INCOMING_PARAMS_SETTING.items():
        value = param_value_or_none(param_name)

        if required:
            if value is None:
                return ' '.join([param_name, 'required'])
            result.append({param_name: value})
        else:
            result.append({param_name: value})

    return result


if __name__ == '__main__':
    print getopt()
