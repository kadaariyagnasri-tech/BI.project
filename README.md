# DNA GC Content Calculator

This is a simple **Bioinformatics Python program** that calculates the **GC content percentage** of a DNA sequence.

## What is GC Content?

GC content is the percentage of **Guanine (G)** and **Cytosine (C)** bases in a DNA sequence.
It is an important concept in **bioinformatics and genetics** because it helps in analyzing DNA stability and gene structure.

Formula used:

GC Content = ((G + C) / Total Bases) × 100

The program:

1. Takes a DNA sequence as input from the user.
2. Counts the number of **G** and **C** nucleotides.
3. Calculates the total length of the DNA sequence.
4. Computes the GC content percentage.
5. Displays the result

```python
dna = input("Enter DNA sequence: ").upper()

g = dna.count("G")
c = dna.count("C")
total = len(dna)

gc_content = ((g + c) / total) * 100

print("GC Content:", gc_content, "%")
```

Example
Input:
ATGCGTAC
Output:
GC Content: 50.0 %


 Technologies Used

* Python
* Basic Bioinformatics concept (GC Content Calculator)
