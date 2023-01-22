#int
number = 5

#float
fnumber = 3.5
#nnnn=input ("введите сойй возаратос")
#str
name ="Саша"

#bool
status = True




print ("что нужно KKKK")
#екранировние
print ("что \"нужно\" віівезит")
# перовд стоки
print ("привет \nмир")
#конкатенаця
print ("привет  миня зовоу   " + name)

23
a=2
b=3
c=a+b
print (c)

# Какойто очень длиднніе тескис тадівлаод іжваові жажіфвдлаождівлаоф іжваждфліов аджфівоа жфдлівоажд філвао фжілваоіжфвла жіфдвлао ждфіваожідвлаоіфвждал фівжадл
print ("хелов ворд")
print ("Helo Word")


age = 26
name = 'Swaroop'
print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python?'.format(name))

l = 5 
b = 5
area=l*b 
print('Площадь равна',area)
print('Периметр равен', 2 *(l + b))


number = 23
guess = int(input('Введите целое число : ')) 
if guess == number:
	print('Поздравляю, вы угадали,') # Начало нового блока
	print('(хотя и не выиграли никакого приза!)') # Конец нового блока 
elif guess < number:
	print('Нет, загаданное число немного больше этого.') # Ещё один блок 
# Внутри блока вы можете выполнять всё, что угодно ...
else:
	print('Нет, загаданное число немного меньше этого.')
# чтобы попасть сюда, guess должно быть больше, чем number
	print('Завершено')
# Это последнее выражение выполняется всегда после выполнения оператора if



number = 23 
running = True 
while running:
	guess = int(input('Введите целое число : ')) 
	if guess == number:
		print('Поздравляю, вы угадали.')
		running = False # это останавливает цикл while 
	elif guess < number:
		print('Нет, загаданнwое число немного больше этого.') 
	else:
		print('Нет, загаданное число немного меньше этого.')
else:
	print('Цикл while закончен.')
	# Здесь можете выполнить всё что вам ещё нужно 
print('Завершение.')



while True:
	s = input('Введите что-нибудь 23 для завершеня : ') 
	if s == '23':
		break
	print('Длина строки:', len(s)) 
print('Завершение')




def sayHello():
	print('Привет, Мир!') # блок, принадлежащий функции 
# Конец функции
sayHello() # вызов функции 
sayHello() # ещё один вызов функции


x = 50
def func(x):
	print('x равен', x) 
	x=2
	print('Замена локального x на', x) 
func(x)
print('x по-прежнему', x)




def say(message, times = 1): 
	print(message * times)
say('Привет') 
say('Мир', 5)


import sys
print('Аргументы командной строки:') 
for i in sys.argv:
	print(i)
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')



# Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы'] 
print('Я должен сделать', len(shoplist), 'покупки.') 
print('Покупки:', end=' ')
for item in shoplist: 
	print(item, end=' ')
print('\nТакже нужно купить риса.') 
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist) 
print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist) 
print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0] 
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)





# 'ab' - сокращение от 'a'ddress'b'ook
ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
		'Larry'     : 'larry@wall.org',
		'Matsumoto' : 'matz@ruby-lang.org', 
		'Spammer' : 'spammer@hotmail.com'
	}
print("Адрес Swaroop'а:", ab['Swaroop']) 
# Удаление пары ключ-значение
del ab['Spammer']
print('\nВ адресной книге {0} контакта\n'.format(len(ab))) 
for name, address in ab.items():
	print('Контакт {0} с адресом {1}'.format(name, address)) 
# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org' 
if 'Guido' in ab:
	print("\nАдрес Guido:", ab['Guido'])




def reverse(text):
	return text[::-1]
def is_palindrome(text):
	return text == reverse(text) 
something = input('Введите текст: ')
if (is_palindrome(something)): 
	print("Да, это палиндром")
else:
	print("Нет, это не палиндром")



import sys, warnings
print(sys.version_info)
if sys.version_info[0] < 3:
	warnings.warn("Для выполнения этой программы необходима как минимум \
	версия Python 3.0",
		RuntimeWarning)
else:
	print('Нормальное продолжение')


import os, platform, logging
if platform.platform().startswith('Windows'):
	logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
			os.getenv('HOMEPATH'), \
			'test.log')
else:
	logging_file = os.path.join(os.getenv('HOME'), 'test.log') 
print("Сохраняем лог в", logging_file)
logging.basicConfig( 
	level=logging.DEBUG,
	format='%(asctime)s : %(levelname)s : %(message)s', 
	filename = logging_file,
	filemode = 'w', 
)
logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("Программа умира333333ет")