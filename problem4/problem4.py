'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def check_palindrome(number_as_str)->bool:
    '''function to check if input is a palindrome'''
    if len(number_as_str) == 1:
        return True
    if len(number_as_str) == 2:
        if number_as_str[0] == number_as_str[-1]:
            return True
        else:
            return False
    if number_as_str[0] == number_as_str[-1]:
        return check_palindrome(number_as_str[1:-1])
    else:
        return False

def main()-> int:
    MAX = 0
    pal = 0
    for i in range(0,1000):
        for j in range(0,1000):
            pal = i*j
            if check_palindrome(str(pal)):
                if pal > MAX:
                    MAX = pal
                    #print("found larger")
    return MAX



if __name__ == "__main__":
    print(main())