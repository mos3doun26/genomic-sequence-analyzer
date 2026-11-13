from dna import DNA
from Bio import SeqIO
import argparse
import pathlib

def main():
    """
        Manage args using argparse module
        Arugments:
            positional: Fasta file
            optional: Output CSV file
            Flags:
                -s, --show: show summary of report in terminal.
                -o, --output: CSV destination file.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=pathlib.Path, help="Fasta file to analyze")
    parser.add_argument("-o", "--output", type=pathlib.Path, help="CSV destination file to export report")
    parser.add_argument("-s", "--show", action="store_true", help="show summary of report in terminal window.")

    args = parser.parse_args()
    sequences = read_fasta(args.input)

    if not args.output:
        args.show = True

    if args.output:
        export_reports(sequences, args.output)

    if args.show:
        show_report(sequences)

def read_fasta(file):
    """
        Input: fasta file
        Ouput: list of DNA sequences
    """
    return [str(record.seq) for record in SeqIO.parse(file, 'fasta')]

def export_reports(data, d_file):
    ...

def show_report(data):
    ...

def compare(list):
    ...

if __name__ == "__main__":
    main()