# https://ooyoung.tistory.com/91

T = int(input())

for _ in range(T):
    x, y = map(int,input().split())
    dt = y - x
    count = 0 
    move = 1
    move_plus = 0
    while move_plus < dt :
        count += 1
        move_plus += move
        if count % 2 == 0 :
            move += 1  
    print(count)