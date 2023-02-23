pair = lambda x: lambda y: {"head": x, "tail": y}
head = lambda pair: pair["head"]
tail = lambda pair: pair["tail"]
notEqual = lambda x: lambda y: (x,y) if x != y else None

def arr2fl(arr):
    result = None
    for x in range(len(arr) - 1, -1, -1):
        result = pair(arr[x])(result)
    return result

def fl2arr(fl):
    result = []
    while fl != None:
        result.append(head(fl))
        fl = tail(fl)
    return result

simpLoop = lambda list: None if list == None else pair(head(list) + 2)(simpLoop(tail(list)))

for x in range(10):
    for y in range(10):
        pass


nestedLoop = lambda xs: lambda xe: lambda ys: lambda ye:\
    None \
    if xs > xe \
    else \
        pair((xs, ys))(nestedLoop(xs+1)(xe)(0)(ye)) \
        if ys > ye \
        else pair((xs, ys))(nestedLoop(xs)(xe)(ys+1)(ye))

stretchList = lambda fl: lambda xs: lambda xe: \
    None \
    if fl == None \
    else \
        pair(head(fl))(stretchList(tail(fl))(0)(xe)) \
        if xs >= xe \
        else pair(head(fl))(stretchList(fl)(xs+1)(xe))

# loop = lambda fl1: lambda fl2: None if fl2 == None else pair(notEqual(head(fl1))(head(fl2)))(loop(tail(fl1))(tail(fl2)))
loop = lambda x: lambda fl2: None if fl2 == None else pair(notEqual(x)(head(fl2)))(loop(x)(tail(fl2)))
loop2 = lambda fl1: lambda fl2: None if fl1 == None else pair(loop(head(fl1))(fl2))(loop2(tail(fl1))(fl2))
