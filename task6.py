task_list = [23, 'Jane', ['Lesson 23', 560, {'currency' : 'KES'}], 987, (76,'John')]

for elements in task_list:
    print(type(elements))

#task6a
element_2 = task_list[2]
shmoney = element_2[2]
print('\n')
print(shmoney['currency'])

#task6b
print(element_2[1])

#task6c
print(len(task_list))

#task6d
#what magic is this ?

#task6e
task_list[1] = 'Jane'
print(task_list)

