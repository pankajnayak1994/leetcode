#https://leetcode.com/problems/reverse-integer/submissions/
import re


class Solution(object):
    def reverse(self, x):
        """
        :type x: str
        :rtype: int
        """
        lower_bound = -2 ** 31
        upper_bound = 2 ** 31 - 1
        number = str(x).strip()
        number = number.rstrip("0")
        if len(number) > 0:
            sign = number[0]
        temp = re.search("\d+", number)
        alph_check = re.search("\d[a-z, A-Z]", number)
        if alph_check is not None:
            return 0
        if temp is None:
            return 0
        else:
            number = temp.group()
        rev_number = number[::-1]
        if sign.isdigit():
            if lower_bound <= int(rev_number) <= upper_bound:
                return str(rev_number)
            else:
                return 0
        else:
            if sign == "+":
                sign = ""
            if lower_bound <= int(sign + str(rev_number)) <= upper_bound:
                return sign + str(rev_number)
            else:
                return 0
