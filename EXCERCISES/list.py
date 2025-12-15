'''
MICRO-CODING SESSIONS🧑‍💻🧑‍💻


TASK-1

You have this list of marks:

[35, 80, 42, 90, 28]

Passing mark is 40. Go through each mark. If the mark is 40 or above, keep it.

'''
marks=[35, 15, 80, 42, 90, 28]
passed_marks=[]
for i in marks:
    if i>= 40:
        passed_marks.append(i)
print(passed_marks)     

'''TASK-2

You have temperatures:

[30, 42, 25, 40, 45]

How many days had temperature above 40?

'''
temperature=[30,42,25,40,45]
high_temp=[]
for i in temperature:
    if i>40:
        high_temp.append(i)
print(len(high_temp))
