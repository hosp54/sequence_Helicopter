from abc import ABC, abstractmethod
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from pathlib import Path


class BiologicalSequence(ABC):
    """
    Abstract base class for biological sequences (DNA, RNA, proteins).
    Defines the basic interface for sequence manipulation and validation.

    Methods:
        __len__: Returns the length of the sequence.
        __getitem__: Allows accessing sequence elements by index or slicing.
        __str__: Returns the sequence as a string.
        __repr__: Returns a string representation of the object.
        check_alphabet: Abstract method to check if the sequence alphabet is valid.
    """

    def __init__(self,  sequence: str):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        return self.sequence[index]

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.sequence}')"

    @abstractmethod
    def check_alphabet(self):
        pass


class NucleicAcidSequence(BiologicalSequence):
    """
    Base class for nucleic acid sequences (DNA and RNA).
    Implements methods for complement, reverse, and reverse complement operations.

    Methods:
        complement: Returns the complementary sequence.
        reverse: Returns the reversed sequence.
        reverse_complement: Returns the reverse complementary sequence.
    """
    dna_complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    rna_complement_dict = {"A": "U", "U": "A", "G": "C", "C": "G"}

    def complement(self):
        comp_dict = self.dna_complement_dict if 'T' in self.sequence else self.rna_complement_dict
        return self.__class__("".join(comp_dict.get(nt, nt) for nt in self.sequence))

    def reverse(self):
        return self.__class__(self.sequence[::-1])

    def reverse_complement(self):
        return self.complement().reverse()


class DNASequence(NucleicAcidSequence):
    """
    Class for DNA sequences.
    Inherits from NucleicAcidSequence and adds a transcription method.

    Methods:
        check_alphabet: Checks if the sequence contains only valid DNA nucleotides.
        transcribe: Transcribes DNA into RNA by replacing T with U.
    """

    def check_alphabet(self):
        return all(nt in self.dna_complement_dict for nt in self.sequence)

    def transcribe(self):
        return RNASequence(self.sequence.replace("T", "U"))


class RNASequence(NucleicAcidSequence):
    """
    Class for RNA sequences.
    Inherits from NucleicAcidSequence.

    Methods:
        check_alphabet: Checks if the sequence contains only valid RNA nucleotides.
    """

    def check_alphabet(self):
        return all(nt in self.rna_complement_dict for nt in self.sequence)


class AminoAcidSequence(BiologicalSequence):
    """
    Class for amino acid sequences (proteins).
    Inherits from BiologicalSequence and adds methods for amino acid analysis.

    Methods:
        check_alphabet: Checks if the sequence contains only valid amino acids.
        count_amino_acid: Counts the occurrences of a specific amino acid in the sequence.
    """
    valid_amino_acids = set("ACDEFGHIKLMNPQRSTVWY")

    def check_alphabet(self):
        return all(aa in self.valid_amino_acids for aa in self.sequence)

    def count_amino_acid(self, amino_acid: str):
        return self.sequence.count(amino_acid)


def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds: tuple[float, float] = (0, 100),
    length_bounds: tuple[int, int] = (0, 2**32),
    quality_threshold: float = 0,
) -> None:
    """
    Filters sequences from an input FASTQ file based on GC content, length, and quality threshold.
    Writes the filtered sequences to an output FASTQ file using Biopython.

    Args:
        input_fastq (str): Path to the input FASTQ file.
        output_fastq (str): Path to the output FASTQ file.
        gc_bounds (tuple[float, float]): Minimum and maximum GC content (default: (0, 100)).
        length_bounds (tuple[int, int]): Minimum and maximum sequence length (default: (0, 2^32)).
        quality_threshold (float): Minimum average quality score (default: 0).

    Returns:
        None
    """

    output_dir = Path(output_fastq).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_fastq, "r") as input_handle, open(output_fastq, "w") as output_handle:

        good_filtered_seqs = []

        for record in SeqIO.parse(input_handle, "fastq"):

            gc_content = gc_fraction(record.seq) * 100
            avg_quality = sum(record.letter_annotations["phred_quality"]) / len(record)
            length_seq = len(record)

            gc_status = False
            length_status = False
            quality_status = False

            if isinstance(gc_bounds, (int, float)):
                if gc_content <= gc_bounds:
                    gc_status = True
            elif isinstance(gc_bounds, tuple):
                if gc_bounds[0] <= gc_content <= gc_bounds[1]:
                    gc_status = True

            if isinstance(length_bounds, (int, float)):
                if length_seq <= length_bounds:
                    length_status = True
            elif isinstance(length_bounds, tuple):
                if length_bounds[0] <= length_seq <= length_bounds[1]:
                    length_status = True

            if avg_quality >= quality_threshold:
                quality_status = True

            if gc_status and length_status and quality_status:
                good_filtered_seqs.append(record)

        SeqIO.write(good_filtered_seqs, output_handle, "fastq")

        print(f"Sequences filtered: {len(good_filtered_seqs)}")
