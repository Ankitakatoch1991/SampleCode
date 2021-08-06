# name = input("Give your name: ")
# age = input("Give your age: ")
# print("your name is "+ name)
# print("your age is "+ age)
# new_age = 2020 + int(100 - int(age))
# print("you will be 100 years old in " + str(new_age))


# def dup(str):
#     dict = {}
#     str1 = ""
#
#     for i in range(len(str)):
#         if str[i] in dict:
#             dict[str[i]] += 1
#         else:
#             dict[str[i]] = 1
#
#     print(dict)
#
#     for i in dict:
#         str1 += i
#     print(str1)
# dup("ankitakatoch")


# def birth():
#     dict = {'ankita': 'march-9-1991', 'anuj': 'sept-28-1987', 'random': 'march-18-2000'}
#     str = ""
#
#     for key,value in dict.items():
#         value = value.split("-")[0]
#         if value == month:
#             str += key
#     print(str)
# month = input("enter month: ")
# birth()

'''
Given a list of integers, representing duration of songs in seconds, output the possible number of unique pairs of songs
such that sum of their durations is a multiple of a whole minute, 60 secs, 120 secs, so on.
Example - for input [30,20,150,40], output is 2.
Here, Possible pairs are [30,150] and [20,40]

[25, 15, 20, 15] = 0
[37, 48] = 0
'''

#
# def numPairsDivisibleBy60(time):
#     ans = 0
#     remainder = {}
#     for i in time:
#         if i % 60 == 0 and 0 in remainder:
#             ans += remainder[0]
#         elif 60 - (i % 60) in remainder:
#             ans += remainder[60 - (i % 60)]
#         if i % 60 in remainder:
#             remainder[i % 60] += 1
#         else:
#             remainder[i % 60] = 1
#     return ans
# print(numPairsDivisibleBy60([30,20,150,100,40]))

#print duplicate/non duplicate characters from string

# def duplicate(str):
#     dict = {}
#     str1 = ""
#
#     for i in str:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#
#     print (dict)
#
#     for i in dict:
#         if dict[i] == 1:
#             str1 += i
#     print(str1)
#
# duplicate("i am a strong and confident woman")


# def palidrome(str):
#
#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str) - i - 1]:
#             return False
#     return True
# print(palidrome("malayalam"))



# def vowels(str):
#     # vowel_dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
#     vowel_list = ["a","i","e","o","u"]
#
#     for i in str:
#         if i in vowel_list:
#
#     # for i in str:
#     #     if i in vowel_dict.keys():
#     #         vowel_dict.values += 1
#     # print(vowel_dict)
#
#     # for i in vowel_dict:
#     #     if
#
# print(vowels("i am a strong and confident woman"))










