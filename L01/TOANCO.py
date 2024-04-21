input_file = open("TOANCO.inp")
output_file = open("TOANCO.out")

data = input_file.readlines()[0]
data.split(" ")
tong = int(data[0])
chan = int(data[1])

ga = cho = 0
for i in range(tong):
    ga = i
    cho = tong - ga
    if ga*2 + cho*4 == chan:
        print("ga",ga)
        print("cho",cho)

# Close
input_file.close()
output_file.close()