#Challenge : Tuple

#Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t).

n = int(input())
integers = input().split()
t = tuple(map(int, integers))
hash_tuple = hash(t)
print(hash_tuple)
