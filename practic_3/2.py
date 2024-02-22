# Task_2_Ekin_Viacheslaw

time = int(input())
hours = time // (60 * 60)
minutes = (time // 60) % 60
sec = time % 60

print(f"{hours}:{minutes}:{sec}")
