import random
import time

def check_statement(predicates):
    check1 = predicates[0]
    check2 = not predicates[0]
    for i in range(len(predicates)):
        check1 = check1 or predicates[i]
        check2 = check2 and not predicates[i]
    return not check1 == check2

def check_all(i):

    count_predicates = random.randint(3,15)
    predicates = []
    for i in range(count_predicates):
        predicates.append(bool(random.randint(0,1)))
    print(f"Predicates: {predicates} -> {check_statement(predicates)}\n")

start_time = time.time()
for i in range(100):
    check_all(i)
print(f"time: {time.time() - start_time}")