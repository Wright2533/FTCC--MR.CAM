num = int(input("How many classes do you wnat to enter: "))
value = "Number "
with open("test.txt","w") as outfile:
    for count in range(1,num +1):
        cl = "cis115"
        time = "11-1"
        out = cl.ljust(10) + time.ljust(10)
        outfile.write(value + str(count) + " ")
        outfile.write(out + "\n")
