# # In the nation of CodeWars, there lives an Elder who has lived for a long time. Some people call him the
# # Grandpatriarch, but most people just refer to him as the Elder.

# # There is a secret to his longetivity: he has a lot of young worshippers, who regularly perform a ritual to ensure # that the Elder stays immortal:

# # The worshippers line up in a magic rectangle, of dimensions m and n.
# # They channel their will to wish for the Elder. In this magic rectangle, any worshipper can donate time equal to
# # the xor of the column and the row (zero-indexed) he's on, in seconds, to the Elder.
# # However, not every ritual goes perfectly. The donation of time from the worshippers to the Elder will experience a
# # transmission loss l (in seconds). Also, if a specific worshipper cannot channel more than l seconds, the Elder
# # will not be able to receive this worshipper's donation.
# # The estimated age of the Elder is so old it's probably bigger than the total number of atoms in the universe.
# # However, the lazy programmers (who made a big news by inventing the Y2K bug and other related things) apparently
# # didn't think thoroughly enough about this, and so their simple date-time system can only record time from 0 to t-1
# # 
# # seconds. If the elder received the total amount of time (in seconds) more than the system can store, it will be
# # wrapped around so that the time would be between the range 0 to t-1.

# # Given m, n, l and t, please find the number of seconds the Elder has received, represented in the poor
# # programmer's date-time system.

# # (Note: t will never be bigger than 2^32 - 1, and in JS, 2^26 - 1.)

import cProfile
from datetime import datetime


# Solution one
def get_result_1(m:int, n:int, l:int, t:int) -> int:
    total_time = 0

    for i in range(m):
        for j in range(n):
            time = (i ^ j) - l

            if time >= 0:
                total_time += time

    return total_time % t

# Solution two
def elder_age(m:int, n:int, l:int, t:int) -> int:
    total_time = 0

    for i in range(m):
        for j in range(n):
            time = i ^ j

            if time >= l:
                total_time += time - l

    return total_time % t

# Solution tree
def elder_age(m: int, n: int, l: int, t: int) -> int:
    total_time = 0
    lookup = [0] * (m + n - 1)

    for i in range(m + n - 1):
        time = i
        if time >= l:
            lookup[i] = time - l

    for i in range(m):
        for j in range(n):
            total_time += lookup[i ^ j]

    return total_time

# elder_age(8,5,1,100)
# elder_age(8,8,0,100007)
# elder_age(25,31,0,100007)
# elder_age(5,45,3,1000007)
# elder_age(31,39,7,2345)
# elder_age(545,435,342,1000007)
# elder_age(28827050410, 35165045587, 7109602, 13719506)


if __name__ == '__main__':
    cProfile.run('get_result(8, 5, 1, 100)')
    start = datetime.now()

    res_1 = get_result(8, 5, 1, 100)
    res_2 = get_result(8, 8, 0, 100007)
    res_3 = get_result(5, 45, 3, 1000007)

    print(res_1)
    print(res_2)
    print(res_3)

    end = datetime.now()
    print('performance => ', end - start)