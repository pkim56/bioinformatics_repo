from DNAToolkit import *
from utilities import colored
import random 
rndDNASeq = ''.join([random.choice(Nucleotides)
	                 for nuc in range(40)])
DNASeq = validateSeq(rndDNASeq)


print(f'\nSequence: {colored(DNASeq)}\n')
print("Sequence: %s" %DNASeq)
print("Sequence Length: %s"%len(DNASeq))
print("Nucleotide Frequency %s" %countNucFrequency(DNASeq))
print("DNA/RNA Transcription: %s" %transcription(DNASeq))

print(f"DNA String + reverse complement: \n5' {DNASeq} 3' ")
print(f"   {''.join(['|'  for c in range(len(DNASeq))])}")
print(f"3' {reverse_complement(DNASeq)} 5'\n")