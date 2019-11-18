import time

def test(times):
    while True:
        print(times)
        if times == 0:
            break
        times = times - 1
    time.sleep(0.2)

test(1000)
