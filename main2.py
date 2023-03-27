from collections import deque

def rhythm(people_amount: int, rhytm_syllables: int):

    group = [i for i in range(0, people_amount)]
    i = 0
    k = rhytm_syllables
    while len(group) != 1:
        i = (k - 1 + i) % len(group)
        # print(i, "pop index")
        popped = group[i]
        group.pop(i)
        # print(group, "group and popped ->", popped)
    return group[0]

print(rhythm(5, 16))
print(rhythm(4, 9))
print(rhythm(10, 4))