import sys

###########
# OP CODE #
###########
op_code = {
        "add":"0000",
        "sub":"0001",
        "wra":"0010",
        "wrb":"0011",
        "wrr":"0100",
        "wrp":"0101",
        "wro":"0110",
        "jmp":"1101",
        "jon":"1110",
        "hlt":"1111",
        }

def getArg():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = None
    return str(arg)

filePath = getArg()

with open(filePath,'r') as f:
    user_code = f.readlines()

lexer = []
value = []
for l in user_code:
    l = l.split(" ")
    lexer.append(l[0])
    value.append(l[1].strip())

compiled = ""

for i,l in enumerate(lexer):
    compiled += f'{op_code[l]}{value[i]}\n'

with open(f"{filePath}.compiled",'w') as f:
    f.write(compiled)
