from Stack_ import*

def donusum(String):
    if String[:2]== "0b":
        print "Binary to Decimal"
        cevir(String[2:],2)
    elif String[:2]== "0x":
        print "Hexadecimal to Decimal"
        cevir(String[2:],16)
    elif String[:1]== "0":
        print "Octal to Decimal"
        cevir(String[1:],8)
    elif String[0] != "0":
        print "Decimal\n ",String
        
def cevir(StR,base):
    s=Stack()
    syc=0
    sonuc=0
    digits = "0123456789ABCDEF"

    for i in StR[0:]:
        s.push(i)
        
    while not s.isEmpty():
        BI=digits.index(s.pop())
        sonuc+=int(BI)*base**syc
        syc+=1
        
    print sonuc

        
