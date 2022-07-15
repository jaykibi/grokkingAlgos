import time

def countdown(i):
    print(i)
    if i <= 0:
        return 
    else: 
        time.sleep(0.25)
        countdown(i-1)


countdown(int(input("enter countdown start: ")))
