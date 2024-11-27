# Approach I took: try and consider a smaller number of digits instead of 1000000 first (e.g. 4 digits)
# 4_digit_palindromes = [1001, 1111, 1221, 1331, 1441, ...., 9889, 9999]
# New list that takes the difference of each consecutive palindrome = [1111-1001, 1221-1111, 1331-1221, ...., 9999-9889]
# So the sum of the new list = (1111-1001) + (1221-1111) + (1331-1221) + .... + (9999-9889)
# = -1001 + 1111 - 1111 + 1221 - 1221 + ... - 9889 + 9999 (This technique is known as the method of finite differences)
# = 9999 - 1001
# = 8998
# Notice as we increase the of digits:
# 5 digits result = 89998, 6 digits result = 899998
# Or in general: n digits result = (10^n -1) - (10^(n-1) + 1)

n = 1000000
result = (10**n - 1) - (10**(n-1) + 1)
print(result % (10**9 + 7))
