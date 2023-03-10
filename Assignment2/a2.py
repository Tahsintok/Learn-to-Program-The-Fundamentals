def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    summ= 0
    for char in dna:
        if char == nucleotide:
            summ= summ + 1
    return summ

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """(str) -> bool

    Return True if and only if the DNA sequence,that contains no other than 'A','T','C','G'a2.py
        
    >>> is_valid_sequence("TACGG")    
    True
    >>> is_valid_sequence("tACCTA")
    FALSE
    >>> is_valid_sequence("FACCTA")
    False
    """
    word= ""
    for  char in dna:
        if char in "TACG":
            word = word+char 
    return  dna==word
            
def insert_sequence(dna1,dna2,index1):
    """ (str,str,int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.
        
    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>> insert_sequence('CCGGCCGG','AT',-3)
    'CCGGCATCGG'
    """

    dna1 = dna1[:index1]+dna2+dna1[index1:]
    return dna1
    

def get_complement(nuc):
    """ (str) -> str
     Return the nucleotide's complement
    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    """

    if  nuc == "A":
        write="T"
    elif  nuc== "T":
        write="A"
    elif  nuc== "G":
        write="C"
    elif  nuc== "C":
        write="G"
    return write
    
def get_complementary_sequence(dna1):
    """
    Return the DNA sequence that is complementary to the given DNA sequence.
    >>> get_complementary_sequence('ATGCC')
    "TACGG"
    >>> get_complementary_sequence('AAC')
    "TTG"
    """
    seq=""
    for char in dna1:
        seq= seq +get_complement(char)

    return seq
        






    
