# FOR
"""
for i in range(1, 6, 2):
  print(i)


  
word = "Hello, world!!!"
for i in word:
  print(i)
  
  word = "Hello, world!!!"
for i in word:
  print(i *3)
  
    
word = "Hello, world!!!"
for i in word:
  if i =="e":
    print("Yes")



count = 0
word = "Hello, world!!!"
for i in word:
  if i == "w":
    count += 1
    
  print("count", count)
  
"""

#   WHILT

"""
i = 5
while i <=15:
  print(i)
  i += 2
  
  
isHasCar = True

while isHasCar:
  if input("Enter data: ") == "Stop":
    isHasCar = False
"""


for i in range(1, 11):
  print(i)
  
  
for i in range(1, 11):
  if i == 5:
    break # Заканчивает выполнение
  print(i)  
  
  
  
for i in range(1, 11):
  if i == 5:
    break
  
  if i % 2 ==0:
    continue # Пропускает итерацию
  
  print(i)    

  
found = None
for i in "hello":
  if i == "l":
    found = True
    break
    
else:
  founl = False
  
print(found)