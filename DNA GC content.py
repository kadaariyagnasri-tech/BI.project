dna = input("Enter DNA sequence: ").upper()

g = dna.count("G")
c = dna.count("C")
total = len(dna)

gc_content = ((g + c) / total) * 100

print("GC Content:", gc_content, "%")
