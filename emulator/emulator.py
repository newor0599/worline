from time import sleep
from os import system
system("clear")
ram = [
        "01011110",
        "01000001",
        "00100000",
        "01011111",
        "00111111",
        "00001111",
        "01101111",
        "11010011",
        "11110000",
        ]
print(" ",len(ram))
if len(ram) > 16:
    print("RAM OVERLOAD")
    print("HALT")
    quit()

if len(ram) < 16:
    for i in range(16-len(ram)):
        ram.append('00000000')


ram_pointer = 0
program_counter = 0
reg_a = ""
reg_b = ""
negative = 0
carry_out = 0
clock_speed = 0.5

def data_ram(position,data):
    ram[position] = "2222" + str(data)

def binary_add(a,b):
    result = ''     
    carry = 0
    max_len = 4 
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result 
        carry = 0 if r < 2 else 1 
    if carry != 0:
        result = '1' + result
    return result

code = "0000"
while code != "1111" and program_counter != 16:
    code = ram[program_counter][:4]
    arg = ram[program_counter][4:]
    match code:
        case "0000":
            print("  ->  ",int(arg,2))
            alu_out = binary_add(reg_a,reg_b)
            if len(alu_out) > 5:
                carry_out = 1
            else:
                carry_out = 0
            data_ram(int(arg,2),alu_out[-4:])

        case "0001":
            print(f"  ->  ",int(arg,2))
            reg_b_invert = ""
            for i in reg_b:
                reg_b_invert += str(int(i)^1)
            alu_out = binary_add(reg_a,reg_b)
            if alu_out[0] == 1:
                negative = 1
            else:
                negative = 0
            data_ram(str(int(arg,2)),alu_out[-4:])

        case "0010":
            reg_a = str(ram[ram_pointer])[4:]
            print(int(str(ram[ram_pointer])[4:],2),"-> 󰬈 ")

        case "0011":
            reg_b = str(ram[ram_pointer])[4:]
            print(int(str(ram[ram_pointer])[4:],2),"-> 󰬉")

        case "0100":
            print(int(arg,2),"->  ",ram_pointer)
            data_ram(ram_pointer,arg)

        case "0101":
            print("󰕟 ",int(arg,2))
            ram_pointer = int(arg,2)

        case "0110":
            print("󰌖 ",ram[int(arg,2)][4:])

        case "1101":
            print("Write counter")
            program_counter = int(str(int(arg)-1),2)

        case "1110":
            if negative:
                print("Write counter on negative")
                counter = (int(str(int(arg)-1),2))

    sleep(clock_speed)
    program_counter += 1
print(" ")
