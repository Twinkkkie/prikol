# 1
dic = {'Россия': 'Москва',
       'Украина': 'Киев',
       'Италия': 'Рим',
       'Испания': 'Мадрид',
       'Болгария': 'София'}
country = input()
for k, v in dic.items():
    if k == country:
        print(k, v)

# 2
dic = {1: 'word_1',
       2: 'word_2',
       3: 'word_3',
       4: 'word_4',
       5: 'word_5'}
for key in dic.keys():
    if key % 2 == 1:
        del dic[key]
print(dic)
