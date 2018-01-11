us_date = '07.17.2017'


# 1
month = us_date[0:2]
day = us_date[3:5]
year = us_date[6:]

eu_date = day + '.' + month + '.' + year
print(eu_date)


# 2
date_lst = us_date.split('.')
eu_date = date_lst[1] + '.' + date_lst[0] + '.' + date_lst[2]
print(eu_date)