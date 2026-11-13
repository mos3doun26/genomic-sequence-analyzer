from dna import DNA
from Bio import SeqIO

def main():
    ...

def read_fasta(file):
    """
        Input: fasta file
        Ouput: list of DNA sequences
    """
    return [str(record.seq) for record in SeqIO.parse(file, 'fasta')]

def export_reports(data):
    ...

def show_report(data):
    ...

def compare(list):
    ...

if __name__ == "__main__":
    main()