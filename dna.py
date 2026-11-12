from collections import Counter
class DNA:
    CODON_TABLE = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
        "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
        
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",

        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    def __init__(self, sequence):
        self.sequence = sequence.upper().strip()

        if len(self.sequence) < 3:
            raise ValueError("DNA sequence must be at least 3 nucleotides long")

    @property
    def nucleotides(self):
        return dict(Counter(self.sequence))

    def gc_content(self):
        n = self.sequence.count("G") + self.sequence.count("C")
        return round(n / len(self.sequence) * 100, 2)

    def transcript(self):
        return self.sequence.replace("T", "U")
    
    def translate(self):
        m_rna = self.transcript()
        peptide = ""

        for i in range(0, len(m_rna)-2, 3):
            codon = m_rna[i:i+3]
            try:
                aa = self.CODON_TABLE[codon]
                if aa == "*":
                    break
                peptide += aa
            except KeyError:
                raise ValueError(f"Not valid codon {codon}")
        return peptide
    
    def orfs(self):
        orfs = 0

        for i in range(0, len(self.sequence) -2, 3):
            codon = self.sequence[i:i+3]
            if codon == "ATG":
                orfs += 1
        return orfs