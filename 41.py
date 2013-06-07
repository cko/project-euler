
perm_numbers = []

def permutate (v_list, rest_list):
    for number in rest_list:
        v_list_new = list (v_list)
        rest_list_new = list(rest_list)
        v_list_new.append(number)
        rest_list_new.remove(number)
        permutate(v_list_new, rest_list_new)
    if (len(rest_list) == 0):
        permutated_number = ''.join(str(i) for i in v_list)
        #print permutated_number
        num = long(permutated_number)
        if (num % 2 != 0 and num % 3 != 0):
            global perm_numbers
            perm_numbers.append(num)

def is_prime (number):
    if number % 2 == 0:
        return False
    for i in range (3,number/2, 2):
        if (number % i == 0):
            return False
    return True


def iterate_numbers(numbers):
        new_numbers = list(numbers)
        global perm_numbers
        perm_numbers = []
        permutate([], new_numbers)
        new_perm_numbers = list(perm_numbers)     
        for n in new_perm_numbers:
            if is_prime(n):
                print n
                exit()
        for n in numbers:
            new_numbers2 = list(numbers)
            new_numbers2.remove(n)
            if len(new_numbers2) > 1:
                iterate_numbers(new_numbers2)

iterate_numbers([9,8,7,6,5,4,3,2,1])
