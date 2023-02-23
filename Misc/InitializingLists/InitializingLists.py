from functools import reduce
from itertools import accumulate
from operator import concat, mul
import InitializiingLiistsFunctional as f


l1 = [1,2,3]
l2 = [3,1,4]
l1 = f.arr2fl(l1)
l2 = f.arr2fl(l2)
# print(head(l2))
print(f.fl2arr(f.loop2(l1)(l2)))

# doesn't work
# l5 = list(
#     filter(
#         lambda x: True if x != None else False, 
#         accumulate(
#             (f.fl2arr(k) for k in f.fl2arr(f.loop2(l1)(l2))), 
#             lambda x,y:concat(x,y), 
#             initial=list())))

# l3 = (fl2arr(k) for k in fl2arr(loop2(l1)(l2)))
# l3 = reduce(lambda x,y:concat(x,y), l3, list())
# l3 = filter(lambda x: True if x != None else False, l3)
# l3 = list(l3)
l3 = list(filter(lambda x: True if x != None else False, reduce(lambda x,y:concat(x,y), (f.fl2arr(k) for k in f.fl2arr(f.loop2(l1)(l2))), list())))
list1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print("----------------------------")
print("l3: ", l3)
print(list1)
print("----------------------------")
test = [1,2,3,4]
test = f.arr2fl(test)
print(test)
# print(f.simpLoop(f.simpLoop(test)))
# print(f.fl2arr(f.nestedLoop(0)(2)(0)(1)))
res = f.fl2arr(
    f.stretchList(test)(0)(2))
print(res)
print(l1)

# an attempt was made