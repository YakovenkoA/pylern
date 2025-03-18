
nums = [5, 7, 2, 4, 7, True, "Hello", 4.5, [4, 567]]

nums[0] = 50

print(nums)
print(nums[3])
print(nums[8])
print(nums[-1])



"""  errore  number = [5, 2, 7]
number[2] """


number = [5, 2, 7]
number.append(100)
number.append(True)
number.insert(1, True)
number.sort()
number.reverse()
number.pop()
number.pop()
number.remove(6)


print(number)
