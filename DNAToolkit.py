
from structures import *

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False 
    return tmpseq


def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "G":0, "T":0, "C":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1

    return tmpFreqDict


def transcription(seq):
    return seq.replace("T","U")


def reverse_complement(seq):
    return ''.join([DNA_reverse_Complement[nuc] for nuc in seq])


