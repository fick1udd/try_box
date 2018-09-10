# python3

# https://projecteuler.net/problem=48


# START   initial attempt  ------------------------------------------------

def rel_int_to_str(n, digs):
    """
    convert numbers in n to string digits in a list

    :param n: integer to be converted to single digit numbers in string format
    :type n: int
    :param digs: integer representing the number of digits that are relevant and therefore converted
    :type digs: int
    :return: list of digs number of single digit numbers in string format
    :rtype: list
    """

    nstr = []
    for i in range(0, digs):
        dign = n % 10
        if n > 0:
            nstr.append(str(dign))
        n //= 10

    nstr.reverse()
    return nstr


def multiply_two_numbers(n, m, dgs):
    """

    :param n: number to be multiplied with m
    :type n: integer
    :param m: number to be multiplied with n
    :type m: integer
    :param dgs: integer representing the number of digits that are relevant starting from the smallest.
    :type dgs: integer
    :return: result from multiplying n and m
    :rtype: integer
    """
    ns = rel_int_to_str(n, dgs)
    ms = rel_int_to_str(m, dgs)
    dig = dgs + 1
    res = 0
    counter = -1
    for i in range(dig - 1, -1, -1):
        if i < len(ns):
            temp4 = 0
            for j in range(dig - 1, -1, -1):
                if j < len(ms) and dig > len(ms) + counter - j:
                    temp1 = int(ns[i]) * int(ms[j])
                    temp2 = 10 ** (len(ms) + counter - j)
                    temp3 = temp1 * temp2
                    temp4 += temp3

            res += temp4
            counter += 1

    return res


def run_multiply_n_times(n, digits):
    #  returns the last digits of  n ** n
    counter = 1
    number = n
    b_trunc = number
    while counter < n:
        b_trunc = multiply_two_numbers(number, b_trunc, digits)
        counter += 1

    b_t = rel_int_to_str(b_trunc, digits)
    b_t.reverse()
    b_trunc = 0
    for i in range(len(b_t)):
        b_trunc += int(b_t[i]) * 10 ** i
    return b_trunc


def sum_of_self_powers(number, digits):
    # sums up number ** number for number in the serie 1 to number

    tot = 0
    for n in range(1, number + 1):
        temp = run_multiply_n_times(n, digits)
        tot += temp

    # returns relevant number of digits
    tot_t = rel_int_to_str(tot, digits)
    tot_t.reverse()
    tot = 0
    for i in range(len(tot_t)):
        tot += int(tot_t[i]) * 10 ** i
    return tot

# END     initial attempt  ------------------------------------------------

# solutions

a = str(sum([i**i for i in range(1,1001)]))[-10:]
b = sum(n**n for n in range(1, 1000)) % 10**10
c = sum(pow(n, n, 10**10) for n in range(1, 1000)) % 10**10

# my take on solutions

def short_self_powers(n, dgs):
    modulo = 10 ** dgs

    # list of the last dgs of all the numbers
    al = [((i ** i) % modulo) for i in range(1, n + 1)]

    # sum upp all the numbers
    a = sum(al)

    # keep only the last relevant dgs
    a = a % modulo
    return a


def self_powers_find_same(n, dgs):
    # find numbers that are being repeated
    # finds only powers of 10

    modulo = 10 ** dgs
    # list of all the numbers, containing only the last dgs
    al = [((i ** i) % modulo) for i in range(1, n + 1)]

    als = set(al)

    # dictionary with keys from the set als and values are the number of times the key appears
    s_dict = {key: al.count(key) for key in als if al.count(key) > 1}

    return s_dict


nbr = 1000
rel_digs = 10
# t = sum_of_self_powers(nbr, rel_digs)
# print(t)
t1 = short_self_powers(nbr, rel_digs)
print(t1)
repeating_numbers = self_powers_find_same(nbr, rel_digs)
for key in repeating_numbers:
    print("{}{}{}{}".format(key, " is in the list ", repeating_numbers[key], " times."))


# (answer: 9110846700)
