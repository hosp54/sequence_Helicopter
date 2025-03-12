# sequence_Helicopter

A bioinformatics tool that performs basic operations on DNA and RNA sequences and filters sequences in FASTQ format files.

---

## Installing and Running Programs

Run the following commands to start it:

```bash
git clone git@github.com:hosp54/sequence_Helicopter.git
cd sequence_Helicopter
pip install -r requirements.txt
python sequence_helicopter.py
```

**System requirements:** Python 3.10 and above.

## Function Description

### Main Functions

#### `filter_fastq`
Filters sequences in a FASTQ file based on the following parameters:
- **GC content percentage**
- **Sequence length**
- **Average read quality**

The parameters have default values, but the user can specify custom values.

**Arguments:**
- `input_fastq` (str): Path to the input FASTQ file.
- `output_fastq` (str): Path to save the filtered FASTQ file.
- `gc_bounds` (tuple[float, float]): Minimum and maximum GC content (default: `(0, 100)`).
- `length_bounds` (tuple[int, int]): Minimum and maximum sequence length (default: `(0, 2**32)`).
- `quality_threshold` (float): Average sequence quality threshold (default: `0`).

**Example:**

```python
filter_fastq(
    input_fastq="example.fastq",
    output_fastq="filtered.fastq",
    gc_bounds=(30, 70),
    length_bounds=(50, 150),
    quality_threshold=20,
)
```

---

### Classes for DNA, RNA, and Protein Sequences

The tool provides classes for working with biological sequences:
- **`DNASequence`**: Represents DNA sequences. Supports transcription to RNA.
- **`RNASequence`**: Represents RNA sequences.
- **`AminoAcidSequence`**: Represents protein sequences.

## New Tool in the sequence_Helicopter Family: `bio_files_processor`

### Additional Functions

#### `convert_multiline_fasta_to_oneline`
Converts a multi-line FASTA file into a single-line format for each sequence.

**Arguments:**
- `input_fasta` (str): Path to the input FASTA file.
- `output_fasta` (str): Path to the output FASTA file. If not provided, a new filename will be created by appending `'_oneline'` to the input file's name.

**Example:**

```python
convert_multiline_fasta_to_oneline(
    input_fasta="input.fasta",
    output_fasta="output_oneline.fasta"
)
```

#### `parse_blast_output`
Parses a BLAST output file to extract the first (best) matching description for each query and sorts these descriptions alphabetically.

**Arguments:**
- `input_file` (str): Path to the input BLAST output file.
- `output_file` (str): Path to the output file where sorted descriptions will be written.

**Example:**

```python
parse_blast_output(
    input_file="blast_output.txt",
    output_file="sorted_descriptions.txt"
)
```

---

## Contacts

For questions or feedback, contact:  
**Ivan**  
Email: [hosp54@gmail.com](mailto:hosp54@gmail.com)
