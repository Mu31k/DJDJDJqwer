string = 'App1Test'


def to_underscore(string):
    if type(string) != int:
        comps = []
        for i in string[::-1]:
            comps.append(i)
            if i.islower() != True and i != '1' and i != '2' and i != '3' and i != '4' and i != '5'\
                    and i != '6' and i != '7' and i != '8' and i != '9' and i != '0':
                comps.append('_')
        comps.reverse()
        del comps[0]
        return ''.join(comps).lower()
    else:
        return str(string)


print(to_underscore(string))





# import re
#
# def to_underscore(string):
#     return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()