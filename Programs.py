'''functions'''
# ------------------------------------------------------------------------------
''' multiplication of number by function methods'''
# def mul(list1):
#     total=1
#     for x in list1:
#       total=total*x
#     return total

# list1=[1,2,3]
# print(mul(list1))

''' function for comparison of three number'''
# def max(num1,num2,num3):
#   if num1>num2 and num1>num3:
#     return num1
#   elif num2>num1 and num2>num3:
#     return num2
#   else :
#     return num3

# print(max(323,43,234))

''' function for reversing a string '''
# def rev(word):
#    for x in range(len(word)-1,-1,-4):
#      print(word[x],end="")

# rev('vimlesh')
''' function for sum of number in list '''
# def sum(list1):
#   sum=0
#   for x in list1:
#     sum=sum+x
#   return sum
# list1=[3,4,3]
# print(sum(list1))
''' recursion function for sum of number in list '''
# def calsum(num):
#   if num:
#     return num+calsum(num-1)
#   else:
#     return 0

# print(calsum(2))

'''taking variable length parameters for functions'''
# *args is used to give variable number of arguments in parameter
# **kwargs is used to give variable numbe of argument with keywords in params

# def func(**kwargs):
#     for i in kwargs:
#         print(i)
# func(name='vimlesh',age='22')

# ------------------------------------------------------------------
'''TAKING Multiple inputs and printing the string in lexographic order'''
# from itertools import permutations
# word,k = input().split()

# y=int(k)
# s=word.upper()
# x=list(permutations(s,y))
# x.sort()
# for i in x:
#     r = ''.join(i)
#     print(r)

'''Taking multiple input at the same time '''
# word,k = input().split()

# x, y, z, n = (int(input()) for _ in range(4))
# print(x,y,z,n)

# n=int(input())
# record=[[input(),float(input())] for i in range(n)]
# print(record)

''' list compreshension with nested list'''
# if __name__ == '__main__':
#   n=int(input())
#   re=[[input(),float(input())] for i in range(n)]

# li=[]
# for i in range(len(re)):
#     li.append(re[i][1])

# se=sorted(list(set(li)))
# se.remove(min(se))
# print(min(se))
# print("\n".join([a for a,b in sorted(re) if b==min(se)]))

'''getting queery sum and rounding off'''
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     # query_name = input("avg of stu")

# k=list(student_marks.keys())
# v=list(student_marks.values())
# newdict={name:sum(avg)/3 for name,avg in zip(k,v)}
# print('{:.2f}'.format(newdict[input()]))

'''getting digit till  2 decimal places '''

# float = 2.154327
# format_float = "{:.2f}".format(float)
# print(format_float)
''' eval function '''
# if __name__ == '__main__':
#     l=[]
#     N = int(input())
#     for i in range(N):
#         s=input().split()
#         cmd=s[0]
#         args=s[1:]
#         if cmd != "print":
#             cmd += "("+",".join(args)+")"
#             eval("l."+cmd)
#         else:
#            print(l)
'''use of counter'''
# from collections import Counter

# n = int(input())
# rooms = [int(x) for x in input().split()]
# cnt = Counter(rooms)
# for k,v in cnt.items():
#     if v==1:
#         print(k)
#         break

''' OOPS For Details of Company Employee'''
# class Programmer():
#     company = 'microsoft'

#     def __init__(self, name, salary, sex, position):
#         self.name = name
#         self.salary = salary
#         self.sex = sex
#         self.position = position

#     def getDetails(self):
#         print(
#             f'name of employee is {self.name} ,salary is {self.salary} ,gender is {self.sex},his position is {self.position}')

# harry = Programmer('harry', 1000, 'male', "developer")
# berry = Programmer('berry', 10, 'male', 'ml')
# kabir = Programmer('kabir', 400, 'male', 'frontend')
# kivy = Programmer('kivy', 101, 'male', 'backend')
# harry.getDetails()

'''oops for squareroot'''
# import math
# class Calculator:
#     def calculate(self,num,operation):
#               if operation=='square':
#                   print(num**2)
#               elif operation=='sqrt':
#                   print("{:.2f}".format(math.sqrt(num)))
#               elif operation=='cube':
#                   print(num**3)

# number=Calculator()
# number.calculate(10,'square')
# number.calculate(11,'sqrt')

