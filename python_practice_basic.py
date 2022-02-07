#print basic string

str1 = 'python'
print(str1)
lenth = len(str1)
print("lenth of a string", lenth)

str2 = "123456"
print(str2)
print(type(str1))
print(type(str2))
lenth = len(str2)
print("lenth of a string", lenth)

# indexing strings
frst_letr = str1[0]
print("first letter of string:", frst_letr)

scnd_letr = str1[1]
print("second letter of string:", scnd_letr)

thrd_letr = str1[2]
print("Third letter of string:", thrd_letr)

frth_letr = str1[3]
print("Fourth letter of string:", frth_letr)

fifth_letr = str1[4]
print("Fifth letter of string:", fifth_letr)
sixth_letr = str1[5]
print("sixth letter of string:", sixth_letr)
# Reverse Indexing
last_str = str1[-1]
print("Last letter of a string:", last_str)

# slicing of string

slc1 = str1[0:4]
print("Printing from 1st to 4th character in sequence", slc1)

slc2 = str1[0:5]
print("Printing from 1st to 5th character in sequence", slc2)


slc3 = str1[1:2]
print("Printing from 2nd  character in sequence", slc3)

slc4 = str1[0:1]
print("Printing from 1st  character in sequence", slc4)



# reversing of string

rev_slc = str1[::-1]
print("Printing reverse order of string", rev_slc)

rev_slc1 = str1[1::]
print("Printing 1st character to nth character", rev_slc1)

string = "Hello world"
length = len(string)
print("length of a string:", length)
ind_of_space = string[5]
print("Printing space in string:", ind_of_space)