def create_list():
  list = []
  pin = open('grid.txt')
  for n in range(20):
    temp_string = pin.readline()
    temp_list1 = temp_string.split()
    temp_list2 = []
    for str in temp_list1:
      temp_list2.append(int(str))
    list.append(temp_list2)
  return list
  
def check_upper_rows(list1, list2, list3, list4):
  i = 0 
  temp_high = 0 
  while i < 17:
    across = list1[i] * list1[i + 1] * list1[i + 2] * list1[i + 3]
    down = list1[i] * list2[i] * list3[i] * list4[i]
    diag1 = list1[i] * list2[i + 1] * list3[i + 2] * list4[i + 3]
    diag2 = list1[i + 3] * list2[i + 2] * list3[i + 1] * list4[i]
    if across > temp_high:
      temp_high = across
    if down > temp_high:
      temp_high = down
    if diag1 > temp_high:
      temp_high = diag1
    if diag2 > temp_high:
      temp_high = diag2
    i += 1
  while i < 20:
    down = list1[i] * list2[i] * list3[i] * list4[i]
    if down > temp_high:
      temp_high = down
    i += 1
  return temp_high

def check_lower_row(l):
  temp_high = 0 
  i = 0 
  while i < 17:
    across = l[i] * l[i + 1] * l[i + 2] * l[i + 3]
    if across > temp_high:
      temp_high = across
    i += 1 
  return temp_high
  
master_list = create_list()
highest = 0 
i = 0
while i < 17:
  temp = check_upper_rows(master_list[i], master_list[i + 1], master_list[i + 2], master_list[i + 3])
  if temp > highest:
    highest = temp
  i += 1

while i < 20:
  temp = check_lower_row(master_list[i])
  if temp > highest:
    highest = temp
  i += 1

for l in master_list:
  print(l)
print('highest = ' + str(highest))







