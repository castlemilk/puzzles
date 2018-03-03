from subprocess import PIPE, Popen
import re


def display_output(f):
    def wrapper(*args, **kwargs):
        if kwargs["debug"]:
            return print(f(*args, **kwargs))
        else:
            return f(*args, **kwargs)
    return wrapper


@display_output
def get_output(command, debug = False):
    """
        Fetch output of a given command and return raw result
        """
    out, err = Popen(command.split(' '), stderr=PIPE, stdout=PIPE).communicate()
    return out.decode("utf-8")


def parse_iostat_mac(output):
    """
    Attempt to parse iostat output on mac
    :param output:
    :return:
    """
    lines = output.split('\n')
    headers = list(filter(lambda x: x != '', re.split(' [ ]+', lines[0])))
    keys = list(filter(lambda x: x != '', re.split('[ ]+', lines[1])))
    values = list(filter(lambda x: x != '', re.split('[ ]+', lines[2])))
    for i, header in enumerate(headers):
        d[header] = {}
        for key in keys[i * 3: i * 3 + 2]:
            d[header][key] = {}
            for value in values[i * 3: i * 3 + 2]:
                d[header][key] = value
    return d


if __name__ == '__main__':
    output = get_output('iostat', debug=False)
    d = {}
    lines = output.split('\n')
    print(lines)
    headers = list(filter(lambda x: x != '', re.split(' [ ]+', lines[0])))
    keys = list(filter(lambda x: x != '', re.split('[ ]+', lines[1])))
    values = list(filter(lambda x: x != '', re.split('[ ]+', lines[2])))
    for i, header in enumerate(headers):
        d[header] = {}
        for key in keys[i * 3: i * 3 + 2]:
            d[header][key] = {}
            for value in values[i * 3: i * 3 + 2]:
                d[header][key] = value


