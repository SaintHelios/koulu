meow = input("Syötä sukupuoli (M/N): ")
tuah = int(input("Syötä hemoglobiiniarvo (g/l): "))

if (meow == "N") and (tuah >= 117 and tuah <= 175):
    print("Hemoglobiiniarvo on normaali")
elif (meow == "N") and (tuah < 117):
    print("Hemoglobiiniarvo on alhainen")
elif (meow == "N") and (tuah > 175):
    print("Hemoglobiiniarvo on korkea")

if (meow == "M") and (tuah >= 134 and tuah <= 195): 
    print("Hemoglobiiniarvo on normaali")
elif (meow == "M") and (tuah < 134):
    print("Hemoglobiiniarvo on alhainen") 
elif (meow == "M") and (tuah > 195):
    print("Hemoglobiiniarvo on korkea") 

