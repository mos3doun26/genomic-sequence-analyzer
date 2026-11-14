from dna import DNA
from Bio import SeqIO
import argparse
import pathlib
from tabulate import tabulate

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
    return [DNA(str(record.seq)) for record in SeqIO.parse(file, 'fasta')]

def export_reports(data, d_file):
    ...

def show_report(data):
    """
        Arg:
            data -> list of DNA objects.
        print table in terminal
    """
    headers, table = table_data(data)
    print(tabulate(table, headers, tablefmt='grid'))

    if len(data) > 10:
        print("There are other DNA sequences......")

def compare(list):
    ...

def table_data(data, eliminate=True):
    """
        Args:
            data -> list of DNA objects
            eliminate: default True -> splice the data into just 10 DNA objects
        return:
            headers, table(list of rows related to headers)
    """
    headers = ["Sequence ID", "Length", "GC %", "A", "T", "G", "C"]
    table = []
    if eliminate:
        data = data[:10]

    for i, seq in enumerate(data, start=1):
        n = seq.nucleotides
        table.append([
            f"Sequence_{i}",
            len(seq.sequence),
            seq.gc_content(),
            n['A'],
            n['T'],
            n['G'],
            n['C'],
        ])

    return headers, table

if __name__ == "__main__":
    main()