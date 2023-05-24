from collections import deque

d = deque()
print(d)

d.append('a')
d.append('b')
print('append: ', d)

d.appendleft('z')
print('appendleft: ', d)

d.extend('cdef')
print('extend: ', d)

d.extendleft('ghij')
print('extendleft: ', d)

d.insert(5, 'k')
print('insert: ', d)

d.pop()
print('pop: ', d)

d.popleft()
print('popleft: ', d)

d.remove('b')
print('remove: ', d)

d.reverse()
print('reverse: ', d)

d.rotate()
print('rotate: ', d)

d.clear()
print('clear: ', d)

d3 = deque(maxlen=30)
print(d3)

# Para copiar uma versão atual do deque
d2 = d.copy()

print(d.count(d))
#print(d.index('a')) # Para achar a primeira ocorrencia de um elemento