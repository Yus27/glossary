import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'glossary_project.settings'
import django
django.setup()

Data = []
Data.append({"x": 1, "y": 2})
Data.append({"x": 3, "y": 4})
print(Data)


# text = """Однажды, в студеную зимнюю пору,
# Я из лесу вышел; был сильный мороз.
# Гляжу, поднимается медленно в гору
# Лошадка, везущая хворосту воз.
#
# И, шествуя важно, в спокойствии чинном,
# Лошадку ведет под уздцы мужичок
# В больших сапогах, в полушубке овчинном,
# В больших рукавицах... а сам с ноготок!
#
# — Здорово, парнище!— «Ступай себе мимо!»
# — Уж больно ты грозен, как я погляжу!
# Откуда дровишки?— «Из лесу, вестимо;
# Отец, слышишь, рубит, а я отвожу».
#
# (В лесу раздавался топор дровосека.)
# — А что, у отца-то большая семья?
# «Семья-то большая, да два человека
# Всего мужиков-то: отец мой да я...»..."""
#
#
# import pymorphy2
# morph = pymorphy2.MorphAnalyzer()
# def toNormalForm(token):
#     p = morph.parse(token)[0]
#     return p.normal_form
#
# import re
# tokens = re.split("\W+", text)
# words = [toNormalForm(token) for token in tokens]
# print(words)
#
#





# def addTags():
#     from glossary.models import Tag
#     for i in range(10):
#         t = Tag(tag = "те111г%d" % i)
#         t.save()
#         print(t)
#
# def addSources():
#     from glossary.models import Source
#     for i in range(10):
#         s = Source(authors="Авторы%d"%i, caption="Заголовок%d"%i)
#         s.save()
#         print(s)

