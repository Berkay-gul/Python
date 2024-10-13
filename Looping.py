""""
v1
time = int(input("Daha kaç kere söylemem gerek ? "))
print("Odani temizle! \n" * time, end="")

v2
time = int(input("Daha kaç kere söylemem gerek ? "))
for x in range(time):
    print("Odani Temizle.")
#----------------------------------------------------------------------------------
for x in range(1,21):
    if x == 4 or x == 13:
        print(f"{x} :Is UNLUCKY")
    elif x%2 == 0:
        print(f"{x} :Is even")
    else:
        
        print(f"{x} :Is odd")
"""
for x in range(1,21):
    if x == 4 or x == 13:
        state = "Unlucky"
    elif x%2 == 0:
        state = "Even"
    else:
        state="Odd"
    print(f"{x} is {state}")   
