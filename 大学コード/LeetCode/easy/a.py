class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        temp = [0] * len(x_str)
        temp_str = ""
        for i in range(len(x_str)):
            temp[i] = x_str[len(x_str)-i-1]
        for i in range(len(temp)):
            temp_str += temp[i]  
        if temp_str == x_str:
            print(temp)
            return True
        else:
            return False
