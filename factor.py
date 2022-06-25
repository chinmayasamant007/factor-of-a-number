






factors = set()
M = int(input("what is your number : "))  # number whose factors we need to find
for N in range(1, M + 1):
    if M % N == 0:  # remainder is zero
        factors.add(N)
print("Factors of {} are {}".format(M, factors))


