# 4 задание 
seconds = int(input())
days = seconds // 86400 
hours = seconds // 3600 % 24
minutes = seconds // 60 % 60 
sec = seconds % 60
print(days, hours, minutes, sec, sep=':')