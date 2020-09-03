def check_email(string):
    return bool(string.find(' ') == -1 and -1 < string.find('@') < string.find('.', string.find('@')) - 1)
