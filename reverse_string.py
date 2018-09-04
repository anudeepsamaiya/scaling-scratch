s = '#abc#de#eg#'

def recursive_rev(s, temp, index=0):
    index += 1
    size = len(s)
    if index <= size:
        temp = s[size-index]
        print(temp)
        return rev(s, temp, index)

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
