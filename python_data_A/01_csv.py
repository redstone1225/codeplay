import csv
f = open('python_data_A\csv_data\yp.csv', 'r', encoding='UTF8')
data = csv.reader(f, delimiter=',')
header = next(data) 
max = -100
max_date = ""
min = 100
min_date = ""
my_day = "2008-12-25"
my_birthday = []
my_temp = []
for row in data:
    row[0] = row[0].lstrip('\t')
    if row[-1] == '':
        row[-1] = -999
    if row[-2] == '':
        row[-2] = 999
        
    row[-1] , row[-2] = float(row[-1]), float(row[-2]) 
    if - 999 < row[-2] < min:
        min = row[-2]
        min_date = row[0]
    if max < row[-1] < 999:
        max = row[-1]
        max_date = row[0]
print(min, min_date, max, max_date)
f.close()
if row[0] == my_day

print(f"최저기온 : {min} 날짜 {min_date}")
print(f"최고기온 : {max} 날짜 {max_date}")
print(f"탕탕절 최고기온")