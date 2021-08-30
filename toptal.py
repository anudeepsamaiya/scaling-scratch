def solution1(S):
    dots = S.split(".")
    qs = [x.split("?") for x in dots]
    exs = [x.split("!") for item in qs for x in item]

    _max = 0
    for items in exs:
        for item in items:
            length = len(item.split())
            if length > _max:
                _max = length
    return _max


test = """
photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11
"""

def solution3(S=test):
    from collections import defaultdict
    from datetime import datetime

    names = S.split("\n")
    output = []
    loc_map = defaultdict(dict)

    def get_padding(length):
        if length >= 10:
            return 2
        if length >= 100:
            return 3
        return 1

    def get_serialno(date, loc):
        _temp = sorted(
            [date, *loc_map[loc].get("dates", [])]
        )
        loc_map[loc]["dates"] = _temp
        loc_map[loc]["padding"] = padding = get_padding(len(_temp))
        serialno = str(loc_map[loc]["dates"].index(date) + 1)
        return serialno.rjust(padding, '0')

    def get_name(loc, date):
        loc = loc.strip()
        dates = loc_map[loc]["dates"]
        padding = loc_map[loc]["padding"]
        serialno = str(dates.index(date) + 1)
        return loc.strip() + serialno.rjust(padding, '0')

    for name in names:
        if not name:
            continue
        extension, loc, date = name.split(",")
        loc = loc.strip()
        date = datetime.strptime(date.strip(), "%Y-%m-%d %H:%M:%S")
        get_serialno(date, loc)

    for name in names:
        if not name:
            continue
        extension, loc, date = name.split(",")
        loc = loc.strip()
        date = datetime.strptime(date.strip(), "%Y-%m-%d %H:%M:%S")
        name = f"{get_name(loc, date)}.{extension.split('.')[1]}"
        output.append(name.strip())

    print(output)
    return output



if __name__ == "__main__":
    solution3()
