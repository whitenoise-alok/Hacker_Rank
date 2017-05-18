import sys


def main(s):
    char_dict = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    bracket_stack = []
    match_bool = True

    if s!='':
        for char in s:
            if char in ['{', '[', '(']:
                bracket_stack.append(char)
            elif char in ['}', ']', ')']:
                if bracket_stack == []:
                    match_bool = False
                    break
                last_char = bracket_stack[-1]
                last_char_match = char_dict[char]

                if last_char_match == last_char:
                    bracket_stack = bracket_stack[:-1]
                else:
                    match_bool = False
                    break

        if bracket_stack ==[] and match_bool:
            print 'YES'
        else:
            print 'NO'

if __name__ == '__main__':
    t = int(raw_input().strip())
    for a0 in xrange(t):
        s = raw_input().strip()
        main(s)