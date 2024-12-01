# sequence_Helicopter

A bioinformatics tool that performs basic operations on DNA and RNA sequences and filters sequences in FASTQ format files

## Installing and Running Programs

Run the following commands to start it:

  ```bash

  git clone git@github.com:hosp54/sequence_Helicopter.git

  python sequence_helicopter.py

  ```
If you encounter the error of importing additional functions, try moving the files dna_rna_operations.py and gc_and_quality_calculator.py into the same folder as sequence_helicopter.py.

System requirements: Python 3.10 and above
  
## Function description

Two main functions
 - `filter_fastq` -filters FASTQ sequences using the following parameters: percentage of GC composition, sequence length, average number of reads.
 - The parameters are set by default, but the user can enter the required parameter values.

   Accepts as input a dictionary, a FASTQ format file. Returns FASTQ file with filtered sequences.

    Arguments: `input_fastq` (path to the FASTQ file you want to run through sequence Helicopter) 
            `output_fastq` (path to save the FASTQ file with the filtering results)
            `length_bounds` (tuple of minimum and maximum sequence lengths) 
            `quality_threshold` (average sequence quality threshold).

- `run_dna_rna_tools` - Converts DNA or RNA sequences.
It takes a list of sequences as input and one of four commands as the last argument: transcribe, reverse, complement or reverse_complement.

Additional functions for filter_fastq (gc_and_quality_calculator)
- `calculate_gc_content` - calculates the percentage of GC content in the sequence.
- `calculate_quality` - calculates the average quality of the sequence over the string of qualities.

Additional functions for filter_fastq (fastq_reader)
- `fastq_to_dict` - Converts a FASTQ file into a dictionary for the filter_fastq.
- `write_fast` -  Writes filtered sequences (dictionary) to a FASTQ file.

Additional functions for run_dna_rna_tools (dna_rna_operations)
- `transcribe` - performs transcription from DNA to RNA.
- `reverse` -  unfolds sequences.
- `complement` - returns complementary DNA or RNA sequences (if the sequence contains T and U at the same time - an error will be reported).
- `reverse_complement` - returns complementary DNA or RNA sequences and unfolds them.


##  New tool in the sequence_Helicopter family - bio_files_processor

Additional functions for bio_files_processor


- `convert_multiline_fasta_to_oneline` - Converts a multi-line FASTA file into a single-line format for each sequence.
  Arguments:
    input_fasta -- the path to the input FASTA file (str).
    output_fasta -- the path to the output FASTA file (str). If not provided, a new filename
                    will be created by appending '_oneline' to the input file's name (default is None).

  
- `parse_blast_output` -  Parses a BLAST output file to extract the first (first == best) matching description for each query and
    sorts these descriptions alphabetically.

    Arguments:
    input_file -- the path to the input BLAST output file (str).
    output_file -- the path to the output file where sorted descriptions will be written (str).

  ## Contacts

  hosp54@gmail.com (Ivan)