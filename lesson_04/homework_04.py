import re
from idlelib import replace
from itertools import count

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

Tom1 = adwentures_of_tom_sawer.replace("\n", " ")
print(Tom1)

# task 02 ==
""" Замініть .... на пробіл
"""
Tom2 = Tom1.replace('....', ' ')
print(Tom2)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
Tom3 = Tom2.replace('   ', ' ')
print(Tom3)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(Tom3.count('h'))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count = 0
for i in Tom3.split():
    if i.istitle() == True:
        count = count + 1
print(count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print(Tom3.find('Tom',1))

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+', Tom3)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3])
print(adwentures_of_tom_sawer_sentences[3].lower())
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for i in adwentures_of_tom_sawer_sentences:
    if i.startswith('By the time'):
        print("Рядок починається з 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last = adwentures_of_tom_sawer_sentences[-1]
count = 0
for i in last.split(' '):
    count = count + 1
print(count)