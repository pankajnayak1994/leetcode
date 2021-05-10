#problem: https://leetcode.com/problems/string-to-integer-atoi/
import re

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        lower_bound = -2 ** 31
        upper_bound = 2 ** 31 - 1
        number = 0
        sign = ""
        s = s.strip()
        temp = re.search(r'\d+', s)
        if temp is None or s[0] == ".":
            return 0
        elif 0 <= temp.start() <= 1:
           number = temp.group()
        else:
            return 0
        if s[0] == "-":
            sign = "-"
        elif s[0] == "+":
            sign = ""
        if number.lstrip("0") == "":
            return 0
        else:
            number = number.lstrip("0")
        if s[0].isalpha():
            return 0
        if s[0].isdigit() or s[1].isdigit():
            if sign == "-":
                if lower_bound <= int(sign + str(number)):
                    return sign + str(number)
                else:
                    return lower_bound
            else:
                if int(sign + str(number)) >= upper_bound:
                    return upper_bound
                else:
                    return sign + str(number)
        else:
            return 0
