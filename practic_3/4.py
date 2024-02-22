# Task_4_Ekin_Viacheslaw

x, y, n = map(int, input().split())
k = (y * n) % 100
r = x * n + (y * n) // 100

print(f"{r} руб. {k} коп.")