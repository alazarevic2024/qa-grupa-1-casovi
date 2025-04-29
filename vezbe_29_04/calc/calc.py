import lang

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def div(a,b):
    return a / b

def mul(a,b):
    return a / b

ops = {
    "+":add,
    "-":sub,
    "/":div,
    "*":mul
}

def op(a,b,op):
    return ops[op](a,b) 

def run():
    l       = input("Choose language (sr,en,de): ")
    a       = int(input(lang.langpacks[l]["a"]+": "))
    b       = int(input(lang.langpacks[l]["b"]+": "))
    oper    = input(lang.langpacks[l]["op"]+" (+,-,/,*): ")
    res     = op(a,b,oper)
    print(lang.langpacks[l]["res"],res)



run()

