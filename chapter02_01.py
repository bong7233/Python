# Chapter02-1
# 파이썬 완전기초
# Print 사용법

#기본출력
print('Python start!')
print('Python start!')

print()

#separate 옵션
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('010', '7777', '1234', sep='-')

print()

#end 옵션

print('welcome to', end=' ')
print('IT news', end=' ')
print('web site')

#file 옵션

import sys

print('Learn python', file=sys.stdout)

# format 사용(d : 3, s : 'python', f : 3.1234)

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two'))

# %s

print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))


print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('niceboy'))
print('{:10.5}'.format('niceboy'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))


# %f

print('%f' % (3.14314))
print('{:f}'.format(3.14314))

print('%06.2f' % (3.14159452))
print('{:06.2f}'.format(3.1459252))
