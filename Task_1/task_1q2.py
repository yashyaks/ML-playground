n = int(input())
list = []
for i in range(0,N):
    ip = input().split();
    if ip[0] == "print":
        print(list)
    elif ip[0] == "insert":
        list.insert(int(ip[1]),int(ip[2]))
    elif ip[0] == "remove":
        list.remove(int(ip[1]))
    elif ip[0] == "pop":
        list.pop();
    elif ip[0] == "append":
        list.append(int(ip[1]))
    elif ip[0] == "sort":
        list.sort();
    else:
        list.reverse();