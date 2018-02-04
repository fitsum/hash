import sys,math


#calculate lowest number of entries per entered slots to avoid collision probability entered 
def f():
    slots,tolerance,entries = int(sys.argv[1]),float(sys.argv[2]),0

    for entries in range(0,slots):
        probability = 1 - ( math.factorial(slots) / (math.factorial(slots-entries) * (slots**entries)) )
        if probability >= tolerance:
            tolerance*= 100
            print ("For", slots, "slots, up to", entries, " entries can be tolerated before the probability for collision reaches", str(int(tolerance)).join("\00%"))
            break

f()

