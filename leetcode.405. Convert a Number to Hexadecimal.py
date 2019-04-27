# class Solution {
# public String toHex(int num) {
# String symbols = "0123456789abcdef";
# StringBuilder ret = new StringBuilder();
#
# do {
# int val = num & 0xf;
# ret.append(symbols.charAt(val));
# num >> >= 4;
# }
#
#
# while (num != 0);
# return ret.reverse().toString();
# }
# }
class Solution(object):
    def toHex(self, num):
        if num == 0: return '0'
        if num < 0: num = (1 << 32) + num # twos complement
        hex_digits = '0123456789abcdef'
        remainders = []
        result = ''
        while num:
            num, rem = divmod(num, 16)
            result += hex_digits[rem]
        return result[::-1]