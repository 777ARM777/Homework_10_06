def starts_with(str1, str2):
    """Takes two strings and returns true if the first argument starts with the second one"""
    if len(str1) < len(str2):
        return False
    return str1[:len(str2)] == str2


def ends_with(str1, str2):
    """Takes two strings and returns true if the first argument ends with the second one."""
    if len(str1) < len(str2):
        return False
    return str1[-len(str2):] == str2


def swap_strings(str1, str2):
    """Takes two strings and swaps their values"""
    str1, str2 = str2, str1
    return str1, str2


def rotate_by(arr, number):
    """Takes a string and a character sequence as its arguments and
    returns the last character equal to none of the characters in the given character sequence"""
    return arr[-number % len(arr):] + arr[:-number % len(arr)]


def find_last_not_of(str, arr):
    """Takes a string and a character sequence as its arguments and
     returns the last character equal to none of the characters in the given character sequence"""
    is_equal = False
    index = len(str)
    while not is_equal and index >= 0:
        is_equal = True
        index -= 1
        for i in range(len(arr)):
            if str[index] == arr[i]:
                is_equal = False
                break
    return str[index]


def convert_to_int(str):
    """Takes an integer array and a number as its arguments and
     returns the array rotated by the specified number of positions"""
    num = 0
    for i in range(len(str)):
        if not (str[i] < 48 or str[i] > 57) and str[0] == '0':
            num *= 10
            num += str[i] - 48  # '0' code in ASCII
        elif str[0] == '0':
            raise ValueError('The string starts with 0')
        else:
            raise ValueError('The string contains not only digits')
    return num


s1 = "asdfasfd"
s2 = "asd"
s3 = "asdfasfedasd"
s4 = "asds"

print(starts_with(s1, s2))
print(starts_with(s1, s3))
print(starts_with(s3, s4))

print(ends_with(s1, s2))
print(ends_with(s3, s2))
print(ends_with(s3, s4))

s1, s2 = swap_strings(s1, s2)
print(s1)
print(s2)

array = [1, 2, 3, 4, 5, 6, 7]
print(rotate_by(array, 9))

char_list = ['s', 'd', 'a', 'e']
print(find_last_not_of(s3, char_list))

num = convert_to_int(b'465456')
if num:
    print(num)
