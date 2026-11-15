import pytest
from dna import DNA
from project import read_fasta, table_data, export_reports, show_report
import csv

# ==========================================
# Tests for DNA Class
# ==========================================

def test_dna_init_valid():
    dna = DNA("ATGCGT")
    assert dna.sequence == "ATGCGT"

def test_dna_init_invalid():
    with pytest.raises(ValueError):
        DNA("AT")  # Less than 3 nucleotides

def test_nucleotides():
    dna = DNA("AATTCG")
    assert dna.nucleotides == {"A": 2, "T": 2, "C": 1, "G": 1}

def test_gc_content():
    dna = DNA("ATGCGT")
    assert dna.gc_content() == 50.0  # 3 G/C out of 6

def test_transcript():
    dna = DNA("ATGCGT")
    assert dna.transcript() == "AUGCGU"

def test_translate():
    dna = DNA("ATGCGT")
    assert dna.translate() == "MR"

def test_translate_stop_codon():
    dna = DNA("ATGUAA")
    assert dna.translate() == "M"  # Stops at UAA

def test_translate_invalid_codon():
    dna = DNA("ATX")
    with pytest.raises(ValueError):
        dna.translate()

def test_orfs():
    dna = DNA("ATGCCCATG")
    assert dna.orfs() == 2  # Two ATG codons

# ==========================================
# Tests for project.py Functions
# ==========================================

def test_read_fasta(tmp_path):
    # Create a temporary fasta file
    fasta_file = tmp_path / "test.fasta"
    fasta_file.write_text(">seq1\nATGCGT\n>seq2\nAATTCG\n")
    
    sequences = read_fasta(fasta_file)
    
    assert len(sequences) == 2
    assert sequences[0].sequence == "ATGCGT"
    assert sequences[1].sequence == "AATTCG"

def test_table_data():
    dna_list = [DNA("ATGCGT"), DNA("AATTCG")]
    headers, table = table_data(dna_list)
    
    assert headers == ["Sequence ID", "Length", "GC %", "A", "T", "G", "C"]
    assert len(table) == 2
    # Check the first row of the table matches Sequence_1 (ATGCGT)
    assert table[0] == ["Sequence_1", 6, 50.0, 1, 2, 2, 1]

def test_export_reports(tmp_path):
    # Use temporary path for CSV output
    csv_file = tmp_path / "output.csv"
    dna_list = [DNA("ATGCGT")]
    
    export_reports(dna_list, csv_file)
    
    assert csv_file.exists()
    
    # Read the generated CSV to verify contents
    with open(csv_file, mode="r") as f:
        reader = list(csv.reader(f))
        assert reader[0] == ["Sequence ID", "Length", "GC %", "A", "T", "G", "C"]
        assert reader[1] == ["Sequence_1", "6", "50.0", "1", "2", "2", "1"]

def test_show_report(capsys):
    dna_list = [DNA("ATGCGT")]
    show_report(dna_list)
    
    # capsys captures everything printed to the terminal
    captured = capsys.readouterr()
    
    # Verify the table grid and data are in the terminal output
    assert "Sequence_1" in captured.out
    assert "Length" in captured.out
    assert "50.0" in captured.out