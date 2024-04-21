input_file = open("TOANCO.inp")
output_file = open("TOANCO.out")

data = input_file.readlines()[0]
data = data.split()

tong = int(data[0])
chan = int(data[1])

ga = cho = 0
for i in range(tong):
    print(i)
    ga = i
    cho = tong - ga
    if ga*2 + cho*4 == chan:
        output_file.write(str(ga), str(cho))

# Close
input_file.close()
output_file.close()