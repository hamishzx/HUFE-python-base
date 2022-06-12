import random

lst_who = ['我','你','他']
lst_where = ['在宿舍','在教室','在操场']
lst_what = ['学习','打游戏','睡觉']
print("{0}{1}{2}".format(lst_who[random.randint(0,2)], lst_where[random.randint(0,2)], lst_what[random.randint(0,2)]))