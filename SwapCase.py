# Challange : sWAP cASE

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    text = s.swapcase()
    return text

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)