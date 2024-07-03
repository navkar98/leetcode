class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def chr_to_digit(chr):
            if chr == '0':
                return 0
            if chr == '1':
                return 1
            if chr == '2':
                return 2
            if chr == '3':
                return 3
            if chr == '4':
                return 4
            if chr == '5':
                return 5
            if chr == '6':
                return 6
            if chr == '7':
                return 7
            if chr == '8':
                return 8
            if chr == '9':
                return 9

        def str_to_num(string):
            num = 0
            digit_order = 1

            for i in string[::-1]:
               num += digit_order * chr_to_digit(i)
               digit_order *= 10

            return num

        return str(str_to_num(num1) * str_to_num(num2))