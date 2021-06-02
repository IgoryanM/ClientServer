import locale
import subprocess

# 1

dev = 'разработка'
soc = 'сокет'
dec = 'декоратор'

print('#1', dev, soc, dec, type(dev), type(soc), type(dec))

dev = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
soc = '\u0441\u043e\u043a\u0435\u0442'
dec = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print('#1', dev, soc, dec, type(dev), type(soc), type(dec), '\n')

# 2

test_list = [b'class', b'function', b'method']
for el in test_list:
    print('#2', type(el), el, len(el))
print()

# 3

test_list = ['attribute', 'класс', 'функция', 'type']
for el in test_list:
    try:
        print('#3', bytes(el, encoding='ASCII'))
    except:
        print(f'#3 {el} - невозможно записать в байтовом типе.')
print()

# 4

test_list = ['разработка', 'администрирование', 'protocol', 'standard']
b_test_list = []
for el in test_list:
    try:
        b_el = el.encode('utf-8')
        b_test_list.append(b_el)
        print('#4', b_el)
    except:
        print(f'#4 {el} - невозможно преобразовать в байты.')

print()

for b_el in b_test_list:
    try:
        el = b_el.decode('utf-8')
        print('#4', el)
    except:
        print(f'#4 {b_el} - невозможно преобразовать в строку.')
print()

# 5
#
# ping_list = ['yandex.ru', 'youtube.com']
#
# for el in ping_list:
#     args = ['ping', el]
#     subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
#     for line in subproc_ping.stdout:
#         line = line.decode('cp866').encode('utf-8')
#         print(line.decode('utf-8'))
# print()

#6

with open('test.txt', 'w+') as f:
    f.write('сетевое программирование, сокет, декоратор')

def_coding = locale.getpreferredencoding()
print(def_coding)

with open('test.txt', encoding='utf-8', errors='replace') as f:
    for line in f:
        print(line)
