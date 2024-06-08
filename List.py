# Challenge : List

#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())
    integers = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            index = int(command[1])
            item = int(command[2])
            integers.insert(index, item)
        elif command[0] == "append":
            item = int(command[1])
            integers.append(item)
        elif command[0] == "remove":
            item = int(command[1])
            integers.remove(item)
        elif command[0] == "pop":
            if not integers:
                print("Sorry! The list is empty")
            else:
                integers.pop()
        elif command[0] == "sort":
            if integers:
                integers.sort()
        elif command[0] == "reverse":
            if integers:
                integers.reverse()
        elif command[0] == "print":
            print(integers)
                
