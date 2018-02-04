import sys,math,string


#calculate lowest number of entries per entered slots to avoid collision probability entered 
slots,tolerance,entries = int(sys.argv[1]),float(sys.argv[2]),0
tplStr = "For $slots slots, up to $entries entries can be tolerated before the probability for collision reaches $toleranceStr%"

def minEntries():
    for entries in range(0,slots):
        probability = 1 - ( math.factorial(slots) / (math.factorial(slots-entries) * (slots**entries)) )
        print(entries,probability)
        if probability >= tolerance:
            print(string.Template(tplStr).substitute(slots=slots,entries=entries,toleranceStr=str(int(tolerance*100))))
            break

minEntries()

