Take DNA input from user
dna = input("Enter DNA sequence: ").upper()

# Create empty RNA string
rna = ""

# Loop through each base
for base in dna:
    if base == "A":
        rna += "U"
    elif base == "T":
        rna += "A"
    elif base == "G":
        rna += "C"
    elif base == "C":
        rna += "G"
    else:
        print("Invalid DNA sequence!")
        break

# Print RNA result
print("RNA Sequence:", rna)
