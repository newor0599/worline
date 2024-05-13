import sys

###########
# OP CODE #
###########
op_code = {
        "add":"0000",
        "sub":"0001",
        "rta":"0010",
        "rtb":"0011",
        "wrr":"0100",
        "wrp":"0101",
        "wro":"0110",
        "wra":"0111",
        "wrb":"1000",
        "jmp":"1101",
        "jon":"1110",
        "hlt":"1111",
        }

def getArg():
    # if len(sys.argv) > 1:
    #     arg = sys.argv[1]
    # else:
    #     arg = None
    return sys.argv

filePath = getArg()[1]
try:
    output = getArg()[2]
except:
    output = "raw"

with open(filePath,'r') as f:
    user_code = f.readlines()

lexer = []
value = []
for l in user_code:
    if l.find("--") == -1 and l.strip() != "":
        l = l.strip().split(" ")
        lexer.append(l[0])
        value.append(l[1])

compiled = ""

for i,l in enumerate(lexer):
    raw = f'{op_code[l]}{value[i]}'
    match output:
        case "raw":
            compiled += f'{raw}\n'
        case "emu":
            compiled += f"\"{raw}\",\n"

with open(f"{filePath}.compiled",'w') as f:
    f.write(compiled)
