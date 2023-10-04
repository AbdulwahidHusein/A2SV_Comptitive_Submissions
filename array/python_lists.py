if __name__ == '__main__':
    N = int(input())
    listt =[]
    
    for _ in range(N):
        commands = input().split()
        if len(commands) == 3:
            listt.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == 'print':
            print(listt)
        elif commands[0] == 'remove':
            listt.remove(int(commands[1]))
        elif commands[0] == 'append':
            listt.append(int(commands[1]))
        elif commands[0] == 'pop':
            listt.pop()
        elif commands[0] == 'sort':
            listt.sort()
        else:
            listt = list(reversed(listt))