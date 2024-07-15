class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def get_formula_dict(string):
            ptr = 0
            n = len(string)
            d = collections.defaultdict(int)

            while ptr < n:
                formula_string = ''
                formula_number = ''
                new_upper = True

                while ptr < n and string[ptr].isalpha() and (new_upper or string[ptr].islower()):
                    formula_string += string[ptr]
                    ptr+= 1
                    new_upper = False

                while ptr < n and string[ptr].isnumeric():
                    formula_number += string[ptr]
                    ptr+= 1

                d[formula_string] += 1 if formula_number == '' else int(formula_number)

            return d

        def multiply_and_generate_string(d, num):
            s = ''
            for i in d.keys():
                s+= i
                s+= str(d[i] * num)

            return s

        def merge_dict(first, second):
            for i in second.keys():
                if i in first:
                    first[i] += second[i]

                else:
                    first[i] = second[i]

            return first


        nn = len(formula)
        i = 0
        tmp = ''
        stack = []
        
        while i < nn:
            if formula[i] == "(":
                stack.append(tmp)
                tmp = ''
                i += 1
            elif formula[i] == ')':
                # print(stack)
                i+= 1

                digits_after_parentheses = ''
                while i < nn and formula[i].isnumeric():
                    digits_after_parentheses += formula[i]
                    i+=1

                new_str = multiply_and_generate_string(get_formula_dict(tmp), 1 if digits_after_parentheses == '' else int(digits_after_parentheses))
                tmp = stack.pop() + new_str
                # print(new_str)
            else:
                tmp += formula[i]
                i += 1
        
        stack.append(tmp)
        final_dict = get_formula_dict(stack.pop())
        while stack:
            final_dict = merge_dict(final_dict, get_formula_dict(stack.pop()))

        final_string = ''
        for i in sorted(final_dict.keys()):
            final_string+= i
            if final_dict[i] > 1:
                final_string+= str(final_dict[i])

        return final_string
