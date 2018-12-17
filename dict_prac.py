# ld1 = [{'a':1},{'b':2},{'c':3}]
# print(ld1[0])
# res = {}
# for d in ld1:
#     res.update(d)
# print(res)

# d1 = {'a':1, 'b':2, 'c':3}
# lt = [('a',1),('b',2),('c',3)]
# ls = [{'a',1}, {'b',2},{'c',3}]

# print(dict(lt))
# print(dict(ls))

# d = {'a':1, 'b':2}
# res = {v:k for k, v in d.items()}
# print(res)

# d = {'a':1, 'b':2, 'c':3, 'd':1}
# res = {}
# for k, v in d.items():
#     res[v] = res.get(v, [])
#     res[v].append(k)
# print(res)

# from collections import defaultdict

# m = ['a','b','a','b','a','c']
# d = defaultdict(lambda: 0)
# for k in m:
#     d[k] += 1
# print(dict(d))

# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# print([x*2+10 for x in foo])

# m = {'Bob': {'age':30, 'country':'America'},
# 'Mary':{'age':20, 'country':'China'},
# 'Frank':{'age':25, 'country':'America'}}

# result = {}
# for k, v in m.items():
#     result.setdefault(v['country'], []).append(k)
# print(result)

# result = {}
# for k, v in m.items():
#     result.setdefault(v['country'], []).append(v['age'])
# print(result)

# key_list = ['a','b','c','d']
# value_list = [11,22,33]
# D = dict(zip(key_list,value_list))
# print(D)

# D = {}
# D['name'] = 'Bob'
# D['job'] = 'dev'
# print(D)

# D1 = {'a':1, 'b':2, 'c':3}
# D2 = {'c':8, 'd':9}
# D1.update(D2)
# print(D1)

# D = {'a':1, 'c':2, 'b':3}

# for k in D:
#     print('{} --> {}'.format(k,D[k]))

# for k, v in D.items():
#     print('{} ---> {}'.format(k,v))

# a = [1,2,3,4,5,6,7,8,9,10]

# d = [x**2 for x in a]
# print(d)
# d = [x**2 for x in a if x % 3 == 0]
# print(d)

# d1 = {'a':1, 'b':2, 'c':3}

# d2 = {k:d1[k]*2 for k in d1}
# print(d2)
# d2 = {k:v*2 for k,v in d1.items()}
# print(d2)

d = {c:c*4 for c in ['a','b','c','c']}
print(d)