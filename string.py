# # How to Print duplicate characters from String
#
# # def duplicate(str):
# #     dict = {}
# #     str1 = ""
# #
# #     for i in range(len(str)):
# #         if str[i] in dict:
# #             dict[str[i]] += 1
# #         else:
# #             dict[str[i]] = 1
# #     print(dict)
# #
# #     for i in dict:
# #         if dict[i] > 1:
# #             str1 += i
# #     print(str1)
#
# # duplicate("ankita katoch")
#
# # How to remove duplicate characters from String
#
# # def remove_dup(str):
# #     dict = {}
# #     str1 = ""
# #
# #     for i in range(len(str)):
# #         if str[i] in dict:
# #             dict[str[i]] += 1
# #         else:
# #             dict[str[i]] = 1
# #
# #     print(dict)
# #
# #     for i in dict:
# #         if dict[i] == 1:
# #             str1 += i
# #     print(str1)
# #
# # remove_dup("ankita katoch")
#
# # How to reverse String
#
# # def reverse(str):
# #     str1 = str[::-1]
# #     print(str1)
# # reverse("ankitakatoch")
#
# # 4. How to remove characters from the first String which are present in the second String?
#
# # def remove_char(str1, str2):
# #     dict1 = {}
# #     dict2 = {}
# #     str3 = ""
# #
# #     for i in range(len(str1)):
# #         if str1[i] in dict1:
# #             dict1[str1[i]] += 1
# #         else:
# #             dict1[str1[i]] = 1
# #
# #     for i in range(len(str2)):
# #         if str2[i] in dict2:
# #             dict2[str2[i]] += 1
# #         else:
# #             dict2[str2[i]] = 1
# #     print(dict1)
# #     print(dict2)
# #
# #     for i in dict1:
# #         if i not in dict2:
# #             str3 += i
# #
# #     print(str3)
# #
# # remove_char("ankita", "anuj")
#
# # 5) How to check if a String contains only digits
#
# # def string_digit(str):
# #     str1 = "1234567890"
# #
# #     for i in range(len(str)):
# #         if str[i] not in str1:
# #             print("no digit", str[i])
# #         else:
# #             print("result: digit", str[i])
# # string_digit("1b2345a7")
#
# # 2) How to check if two Strings are anagrams of each other?
#
# # def anagram(str1,str2):
# #     dict1 = {}
# #     dict2 = {}
# #
# #     for i in range(len(str1)):
# #         if str1[i] in dict1:
# #             dict1[str1[i]] += 1
# #         else:
# #             dict1[str1[i]] = 1
# #     for i in range(len(str2)):
# #         if str2[i] in dict2:
# #             dict2[str2[i]] += 1
# #         else:
# #             dict2[str2[i]] = 1
# #     print(dict1)
# #     print(dict2)
# #
# #     if dict1 == dict2:
# #         print("anagram")
# #     else:
# #         print("not")
# #
# # anagram("ankita", "atikna")
#
#
# # How to program to print first non repeated character from String?
#
# # def nonrepeat(str):
# #     dict = {}
# #
# #     for i in range(len(str)):
# #         if str[i] in dict:
# #             dict[str[i]] += 1
# #         else:
# #             dict[str[i]] = 1
# #
# #     print(dict)
# #
# #     for i in dict:
# #         if dict[i] == 1:
# #             break
# #     print(i)
# # nonrepeat("ankitakatoch")
#
# # How to count a number of vowels and consonants in a String?
#
# # def vowelconstant(str):
# #     str1 = "aeiou"
# #     vowel = 0
# #     constant = 0
# #
# #     for i in range(len(str)):
# #         if str[i] in str1:
# #             vowel += 1
# #         else:
# #             constant += 1
# #     print("vowels are = ", vowel)
# #     print("constants are =" , constant )
# #
# # vowelconstant("ankitakatoch")
#
# # How to count the occurrence of a given character in String?
#
# # def occurance(str):
# #     count = 0
# #     alpha = input("enter the character to count: ")
# #     for i in range(len(str)):
# #         if alpha in str[i]:
# #             count += 1
# #     print("character count = ", count)
# #
# # occurance("ankitakatoch")
#
# # How to find all permutations of String?
#
# # ini_str = "abc"
# # result = []
# # def permute(data, i, length):
# #     if i == length:
# #         result.append(''.join(data))
# #     else:
# #         for j in range(i, length):
# #             # swap
# #             data[i], data[j] = data[j], data[i]
# #             permute(data, i + 1, length)
# #             data[i], data[j] = data[j], data[i]
# #
# #
# # permute(list(ini_str), 0, len(ini_str))
# # print("Resultant permutations", str(result))
#
# # reverse an integer
# # def integer_reverse(str):
# #     if str[0] == "-":
# #         str1 = "-"+str[:0:-1]
# #         print(str1)
# #     else:
# #         str1 = str[::-1]
# #         print(str1)
# # integer_reverse("12345")
#
# # prime numbers
# # def prime(num):
# #     prime_numbers = []
# #     for j in range(num):
# #         if j > 1:
# #             for i in range(2, j):
# #                 if j % i == 0:
# #                     break
# #         else:
# #             prime_numbers.append(j)
# #     return prime_numbers
# # prime(17)
#
# # compare two lists (use sets)
# # sentence1 = {2,4,6,8,0}
# # sentence2 = [1,3,5,8,9]
# # def matched(sentence1,sentence2):
# #     set1 = set(sentence1)
# #     set2 = set(sentence2)
# #     print(set1)
# #     print(set2)
# #     set3 = set1 - set2
# #     print(set3)
# # matched(sentence1,sentence2)
#
# # replace None by previous digit
# # array = [1,None,2,3,None,None,5,None]
# # def solution(array):
# #     res = []
# #     valid = 0
# #
# #     for i in array:
# #         if i is not None:
# #             res.append(i)
# #             valid = i
# #         else:
# #             res.append(valid)
# #
# #     print(res)
# # solution(array)
#
# # all zeroes in the end
# # array1 = [0,1,0,3,12]
# # array2 = [1,7,0,0,8,0,10,12,0,4]
# # def solution(array1):
# #
# #     for i in array1:
# #         if i is 0:
# #             array1.remove(i)
# #             array1.append(i)
# #
# #     print(array1)
# # solution(array1)
#
# # palindrome
# # def solution(str):
# #     for i in range(len(str)):
# #         t = str[:i] + str[i+1:]
# #         if t == t[::-1]:
# #             return True
# #
# # print(solution("radhar"))
#
# # first unique character
# # def solution(str):
# #     dict = {}
# #     for i in range(len(str)):
# #         if str[i] in dict:
# #             dict[str[i]] += 1
# #         else:
# #             dict[str[i]] = 1
# #     print(dict)
# #
# #     for i in dict:
# #         if dict[i] == 1:
# #             return i
# #
# # print(solution("allphabet"))
#
# # sum of two strings
# # num1 = '364'
# # num2 = '1836'
# # def solution(num1,num2):
# #     return int(num1) + int(num2)
# # print(solution(num1,num2))
#
# # index of two numbers adding up to target
# # def twoSum(nums, target):
# #     dict = {}
# #     for i in range(len(nums)):
# #         if target - nums[i] not in dict:
# #             dict[nums[i]] = i
# #         else:
# #             return dict[target-nums[i]], i
# #
# # nums = [3, 2, 4]
# # target = 6
# # print(twoSum(nums, target))
#
# '''
# Given a list of integers, representing duration of songs in seconds, output the possible number of unique pairs of songs
# such that sum of their durations is a multiple of a whole minute, 60 secs, 120 secs, so on.
# Example - for input [30,20,150,40], output is 2.
# Here, Possible pairs are [30,150] and [20,40]
#
# [25, 15, 20, 15] = 0
# [37, 48] = 0
# '''
#
# # list = [30,20,150,40]
# #
# # def solution(list):
# #     target = [60,180]
# #     count = 0
# #     for i in range(len(list)):
# #         for j in range(i+1, len(list)):
# #             if list[i] + list[j] % 60 == 0:
# #                 count += 1
# #     return count
# # print(solution(list))
# #
# #
# #
# # def pair_with_target_sum(songs, k):
# #     n = len(songs)
# #     count = 0
# #     for i in range(0, n):
# #         for j in range(i + 1, n):
# #             if songs[i] + songs[j] == k:
# #                 count += 1
# #     return count
# # print(pair_with_target_sum([10, 50, 90, 30], 60))
# # print(pair_with_target_sum([30, 20, 150, 100, 40], 60))
#
#
# # # How to return the highest occurred character in a String?
# # str = "my nameisankitacdvvcsvsvf"
# # def solution(str):
# #     dict = {}
# #     max = dict[0]
# #
# #     for i in range(len(str)):
# #         if str[i] in dict:
# #             dict[str[i]] += 1
# #         else:
# #             dict[str[i]] = 1
# #
# #     print(dict)
# #
# #
# #     for i in range(1,len(dict)):
# #         if dict[i] > max:
# #             max = dict[i]
# #     return max
# #
# # print(solution(str))
#
# # sorting
# # def solution(list):
# #     # temp = 0
# #
# #     for i in range(len(list)):
# #         for j in range(len(list)):
# #             if list[i] > list[j]:
# #                 temp = list[i]
# #                 list[i] = list[j]
# #                 list[j] = temp
# #     return list
# # print(solution([2,4,7,9,0,12,3]))
#
# # balanced paranthesis
#
# # open_list = ["[", "{", "(", "<"]
# # close_list = ["]", "}", ")", ">"]
# # str = "{{[]{()}}"
# # def solution(str):
# #     stack = []
# #
# #     for i in range(len(str)):
# #         if i in open_list:
# #             stack.append(i)
# #         elif i in close_list:
# #             pos = close_list.index(i)
# #             if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
# #                 stack.pop()
# #             else:
# #                 return "unbalanced"
# #     if len(stack) == 0:
# #         return "unbalanced"
# #     else:
# #         return "unbalanced"
# #
# # print(solution(str))
#
# #reverse an integer
# # def reverse(x):
# #     x_char = str(x)
# #     if x_char[0] is "-":
# #         y = "-" + x_char[:0:-1]
# #     else:
# #         y = x_char[::-1]
# #     print(y)
# # reverse(-321)
#
#
# # def palindrome(x):
# #     str1 = str(x)
# #     if str1 == str1[::-1]:
# #         return True
# #     else:
# #         return False
# # print(palindrome(123121))
#
# # Find the date of the month on which the stock was highest.
# # In this case, the result is 2.
# # date = [30 ,4, 8, 6, 25, 13]
# # stock = [150, 210.5, 268, 200.34, 187, 112]
# # def solution(stock, date):
# #     max = 0
# #     for i in range(len(stock)):
# #         if stock[i] > max:
# #             max = stock[i]
# #     return date[(stock.index(max))]
# # print(solution(stock,date))
#
# # Sort an array of strings so all anagrams are next to each other
# # input = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
# # #Result: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']
# #
# # def solution(input):
# #     index1 = []
# #     words = []
# #
# #     for i in input:
# #         index1 = input.index()
# #     print(index1)
# #     words = input
# #     # print (index1)
# #
# # solution(input)
#
#
#
#
#
# Find the Minimum length Unsorted Subarray, sorting which makes
# the complete array sorted
# Given an unsorted array arr[0..n-1] of size n,
# find the minimum length subarray arr[s..e] such that
# sorting this subarray makes the whole array sorted.
# Examples:
# 1) If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60],
# your program should be able to find that the subarray lies between
# the indexes 3 and 8
#
# arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
#
# fibbonachi

def fib(n):
    if n < 0:
        print("incorret input")
    elif n == 0:
        return 0
    elif n ==1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(9))


# # ankitakatoch -- print aktktc
#
# # def alter(str):
# #     str1 = ""
# #     for i in range(0,len(str),2):
# #         str1 = str[i]
# #         print(str1)
# #
# # print(alter("ankitakatoch"))
#
# # prime numbers
#
# # def prime():
# #     for num in range(100,200):
# #         for i in range(2,num):
# #             if num % i != 0:
# #                 print(num)
# # prime()
#
# # sorting
# # def sorting(list):
# #     temp = 0
# #     for i in range(len(list)):
# #         for j in range(1, len(list)):
# #             if list[i] > list[j]:
# #                 temp = list[i]
# #                 list[j] = list[i]
# #                 list[j] = temp
# # print(sorted([3,7,1,2,6,10,5]))
#
# # def reverse(list):
# #     str = list[::-1]
# #     print(str)
# # reverse([3,5,2,6,1,7,8])
#
# # duplicate in list
# # def duplicate(list):
# #     print(set(x for x in list if list.count(x) > 1))
# # duplicate([1,2,5,3,8,5,3])
#
# # number of words in given sentence
# # def numbers(str):
# #     print(len(str.split()))
# # numbers("my name is ankita katoch")
#
