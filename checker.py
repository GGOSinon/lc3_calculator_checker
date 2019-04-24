import subprocess
from time import sleep
import sys
import random

subprocess.run(["killall", "-9", "./lc3sim"])

proc = subprocess.Popen("./lc3sim calc.obj",stdin=subprocess.PIPE, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

sleep(0.5)

proc.stdin.write("finish\n")
proc.stdin.flush()
sleep(0.5)

tests = []
#tests = [("3*5", 15), ("3/5", 0), ("3%5", 3), ("3+5", 8), ("3/0", "ERROR")]

def div(N1, N2):
    res = N1//N2
    if N1%N2 == 0: return res
    if N2<0: return res+1
    return res

def mod(N1, N2):
    res = N1%N2
    if N1%N2 == 0: return res
    if N2<0: return abs(N2) - abs(res)
    return res

def gen_test(N1, N2, op):
    global tests
    if op == 0:
        tests.append(("{}+{}".format(N1, N2), N1+N2))
    if op == 1:
        tests.append(("{}-{}".format(N1, N2), N1-N2))
    if op == 2:
        tests.append(("{}*{}".format(N1, N2), N1*N2))
    if op == 3:
        if N2==0: tests.append(("{}/{}".format(N1, N2), "ERROR"))
        else: tests.append(("{}/{}".format(N1, N2), div(N1, N2)))
    if op == 4:
        if N2==0: tests.append(("{}%{}".format(N1, N2), "ERROR"))
        else: tests.append(("{}%{}".format(N1, N2), mod(N1, N2)))


for N1 in range(-16, 16):
    for N2 in range(-16, 16):
        for op in range(5):
            if N2<0 and op>=3: continue
            gen_test(N1, N2, op)
    print(N1)
print(len(tests))
sleep(0.5)

n_low, n_high = -32767, 32767
for step in range(5000):
    op = random.randrange(0, 5)
    N1 = random.randrange(n_low, n_high)
    if op == 0:
        N2 = random.randrange(max(n_low, n_low - N1), min(n_high, n_high - N1))
    if op == 1:
        N2 = random.randrange(max(n_low, N1 - n_high), min(n_high, N1 - n_low))
    if op == 2:
        if N1 > 0: N2 = random.randrange(n_low//N1 + 1, n_high//N1)
        if N1 == 0: N2 = random.randrange(n_low, n_high)
        if N1 < 0: N2 = random.randrange(n_high//N1 + 1, n_low//N1)
    if op == 3:
        N2 = random.randrange(0, n_high)
    if op == 4:
        N2 = random.randrange(0, n_high)
    gen_test(N1, N2, op)
    if step % 100 == 0:
        print(step)

random.shuffle(tests)
#print(tests)
test_str = ""
for test in tests:
    (prob, ans) = test
    test_str += (prob+"\n")
test_str += "e"

proc.stdin.write(test_str)
proc.stdin.flush()

'''
for test in tests[0:5]:
    (prob, ans) = test
    proc.stdin.write(prob+"\n")
    proc.stdin.flush()
    sleep(0.05)
'''

for _ in range(22):
    o = proc.stdout.readline()
    if o == '': break
    print(o)

step = 1
print(len(tests))
sleep(0.4)
tests = tests[0:8500]
for test in tests:
    (prob, ans) = test
    o = proc.stdout.readline()
    #print(o)
    #break
    o.replace(")", " ")
    res = o.split()[-1]
    if str(ans) == res:
        print("Case", step, ": YES " + prob + "=" + str(res))
        pass
    else:
        print("NO answer is "+str(ans))
        print(prob + "=" + str(res))
        break
    #if step % 10 == 0: print(step,"/",len(tests), "complete")
    step += 1

subprocess.run(["killall", "-9", "./lc3sim"])
'''
    res = proc.stdout.readline()
    if ans == int(res): print("YES!")
    else: print("NO " + str(ans))
    print(prob + "=" + res)
'''
