string = input()
i, c = input().split()

x = i+1

s_new = string[:i]+c+string[x:]
print(s_new)

#using fn
def mutate_string(string, position, character):
    x = position+1
    Output = string[:position]+character+string[x:]
    return Output

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)