s = '#abc#de#eg#'

def rev(s):
    """concatenates inside out"""
    return len(s) != 0 and rev(s[1:]) + s[0] or s

def reverse_str(s):
    ll = []
    for each in s[::-1]:
        if not each.isalnum():
            ll.append(each)
            continue
        temp = [x for x in each[::-1]]
        ll.append(''.join(temp))
    print(''.join(ll))

def reverse_str2(s):
    ll = [ x[::-1] for x in s[::-1] if x.isalnum() ]
    return ''.join(ll)
