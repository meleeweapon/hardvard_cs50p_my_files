from itertools import accumulate
from functools import reduce
from operator import concat

# accumulate = lazily evaluated reduce ?

foo = range(1, 5)

mul = lambda x,y:x*y

print(list(accumulate(foo, mul)))

print(reduce(mul, foo))

# no

# can reduce even be lazily evaluated,
def lazyReduce(iter, func):
    result = None
    for x in iter:
        result = func(result, x)
    yield result # doesn't make sense


# convert 3x3 matrix to flat arr

matr = [[1,2,3],[4,5,6],[7,8,9]]

# imperative ver:
def imp(matr):
    result = []
    for x in matr:
        for y in x:
            result.append(y)
    return result

print("fl:  ", reduce(concat, matr))
print("imp: ", imp(matr))