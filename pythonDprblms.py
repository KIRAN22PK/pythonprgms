# 1. Reverse a string without slicing
s = "hello"
rev = ""
for char in s:
    rev = char + rev
print("Reversed string:", rev)

# 2. Check if a string is a palindrome
print("Is palindrome:", s == rev)

# 3. Count vowels and consonants in a string
vowels = "aeiouAEIOU"
v_count = c_count = 0
for char in s:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1
print("Vowels:", v_count, "Consonants:", c_count)

# 4. Remove duplicates from a string
result = ""
for char in s:
    if char not in result:
        result += char
print("Without duplicates:", result)

# 5. Find the most frequent character
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
most_freq = max(freq, key=freq.get)
print("Most frequent character:", most_freq)

# 6. Convert sentence to title case manually
sentence = "hello world from python"
title_case = ""
words = sentence.split()
for word in words:
    title_case += word[0].upper() + word[1:] + " "
print("Title case:", title_case.strip())

# 7. Check if two strings are anagrams
s1 = "listen"
s2 = "silent"
print("Anagrams:", sorted(s1) == sorted(s2))

# 8. Count words without split()
sentence = "hello world from python"
count = 1 if sentence else 0
for char in sentence:
    if char == " ":
        count += 1
print("Word count:", count)

# 9. Remove all spaces
no_space = ""
for char in sentence:
    if char != " ":
        no_space += char
print("Without spaces:", no_space)

# 10. Replace all occurrences of a character
s = "banana"
s_new = ""
for char in s:
    if char == "a":
        s_new += "o"
    else:
        s_new += char
print("Replaced string:", s_new)

# 11. Find first non-repeating character
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
first_non_repeat = None
for char in s:
    if freq[char] == 1:
        first_non_repeat = char
        break
print("First non-repeating character:", first_non_repeat)

# 12. Find longest word
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)

# 13. Check if string contains only digits
s = "12345"
print("Only digits:", s.isdigit())

# 14. Reverse words in a sentence
words = sentence.split()
reversed_words = " ".join(words[::-1])
print("Reversed words:", reversed_words)

# 15. Implement atoi()
s = "1234"
num = 0
for char in s:
    num = num * 10 + (ord(char) - ord('0'))
print("String to integer:", num)

# ---------------- Numbers / Math ----------------

# 16. Check if a number is prime
n = 29
is_prime = True
if n <= 1:
    is_prime = False
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        is_prime = False
        break
print("Is prime:", is_prime)

# 17. Find all primes in a range
start, end = 10, 50
primes = []
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            primes.append(num)
print("Primes in range:", primes)

# 18. Factorial iterative & recursive
def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n-1)

print("Factorial iterative:", factorial_iter(5))
print("Factorial recursive:", factorial_rec(5))

# 19. Fibonacci series iterative & recursive
def fib_iter(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

print("Fibonacci iterative:", fib_iter(10))
print("10th Fibonacci recursive:", fib_rec(9))

# 20. Check Armstrong number
n = 153
sum_digits = sum(int(d)**3 for d in str(n))
print("Is Armstrong:", n == sum_digits)

# 21. Find LCM
a, b = 12, 18
def lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1
print("LCM:", lcm(a, b))

# 22. Reverse a number
n = 12345
rev = 0
temp = n
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reversed number:", rev)

# 23. Count digits in a number
n = 12345
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10
print("Digits count:", count)

# 24. Sum of digits
n = 12345
sum_d = 0
temp = n
while temp > 0:
    sum_d += temp % 10
    temp //= 10
print("Sum of digits:", sum_d)

# 25. Check perfect number
n = 28
sum_div = sum(i for i in range(1, n) if n % i == 0)
print("Is perfect number:", n == sum_div)

# 26. Sum of first n natural numbers
n = 10
sum_n = n*(n+1)//2
print("Sum of first n numbers:", sum_n)

# 27. Count trailing zeros in factorial
n = 100
count = 0
i = 5
while n // i > 0:
    count += n // i
    i *= 5
print("Trailing zeros in factorial:", count)

# 28. Check if number is palindrome
n = 12321
rev = 0
temp = n
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Number palindrome:", n == rev)

# 29. Check strong number
n = 145
temp = n
sum_fact = 0
def fact(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f
while temp > 0:
    digit = temp % 10
    sum_fact += fact(digit)
    temp //= 10
print("Strong number:", n == sum_fact)

# 30. nth term in Fibonacci
n = 10
a, b = 0, 1
for _ in range(n-1):
    a, b = b, a + b
print("nth Fibonacci term:", a)

# ---------------- Lists / Arrays ----------------

lst = [3, 5, 2, 9, 1, 5]

# 31. Max & Min without built-ins
max_val = lst[0]
min_val = lst[0]
for i in lst:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i
print("Max:", max_val, "Min:", min_val)

# 32. Remove duplicates from a list
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print("Without duplicates:", unique)

# 33. Second largest element
first = second = float('-inf')
for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second largest:", second)

# 34. Rotate list by n elements
n = 2
rotated = lst[n:] + lst[:n]
print("Rotated list:", rotated)

# 35. Merge two sorted lists
lst1 = [1,3,5]
lst2 = [2,4,6]
merged = []
i = j = 0
while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1
merged += lst1[i:] + lst2[j:]
print("Merged list:", merged)

# 36. Find pairs with a given sum
lst = [1,2,3,4,5]
target = 5
pairs = []
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i]+lst[j]==target:
            pairs.append((lst[i], lst[j]))
print("Pairs with sum:", pairs)

# 37. Subarray with maximum sum (Kadane's)
lst = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = cur_sum = lst[0]
for num in lst[1:]:
    cur_sum = max(num, cur_sum+num)
    max_sum = max(max_sum, cur_sum)
print("Max subarray sum:", max_sum)

# 38. Move zeros to the end
lst = [0,1,0,3,12]
non_zero = [x for x in lst if x != 0]
zeros = [0]*lst.count(0)
lst = non_zero + zeros
print("Zeros moved to end:", lst)

# 39. Find missing number in 1..n
lst = [1,2,4,5,6]
n = 6
missing = n*(n+1)//2 - sum(lst)
print("Missing number:", missing)

# 40. Check if list is palindrome
lst = [1,2,3,2,1]
print("List palindrome:", lst == lst[::-1])

# 41. Flatten nested list
nested = [1, [2, [3,4]], 5]
flat = []
def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            flatten(i)
        else:
            flat.append(i)
flatten(nested)
print("Flattened list:", flat)

# 42. Intersection of two lists
lst1 = [1,2,3]
lst2 = [2,3,4]
intersection = [i for i in lst1 if i in lst2]
print("Intersection:", intersection)

# 43. Union of two lists
union = lst1[:]
for i in lst2:
    if i not in union:
        union.append(i)
print("Union:", union)

# 44. Count frequency of each element
lst = [1,2,2,3,1,4]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
print("Frequency:", freq)

# 45. Sort a list without using sort()
lst = [5,2,9,1]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("Sorted list:", lst)
