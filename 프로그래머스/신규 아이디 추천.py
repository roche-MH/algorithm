import re
def round_1(new_id):
    return new_id.lower()

def round_2(new_id):
    new_id = re.sub('[^a-z0-9-_.]','',new_id)
    return new_id

def round_3(new_id):
    while new_id.count('..'):
        new_id = new_id.replace('..','.')
    return new_id

def round_4(new_id):
    if len(new_id) > 1:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    elif new_id == '.':
        new_id = ''
    return new_id

def round_5(new_id):
    if len(new_id) == 0:
        new_id = 'a'
    return new_id

def round_6(new_id):
    if len(new_id) > 15:
        if new_id[:15][-1] == '.':
            return new_id[:14]
        return new_id[:15]
    return new_id

def round_7(new_id):
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id

def solution(new_id):
    new_id = round_1(new_id)
    new_id = round_2(new_id)
    new_id = round_3(new_id)
    new_id = round_4(new_id)
    new_id = round_5(new_id)
    new_id = round_6(new_id)
    new_id = round_7(new_id)
    return new_id
