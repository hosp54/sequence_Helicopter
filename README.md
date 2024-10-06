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

   Accepts as input a dictionary consisting of fastq sequences of the form {'sequence name': ('sequence', 'quality string' }). Returns a dictionary of filtered sequences.

  Arguments: `seqs` (dictionary of fastq sequences), 
            `gc_bounds` (tuple of minimum and maximum GC composition values), 
            `length_bounds` (tuple of minimum and maximum sequence length) 
            `quality_threshold` (average sequence quality threshold).

- `run_dna_rna_tools` - Converts DNA or RNA sequences.
It takes a list of sequences as input and one of four commands as the last argument: transcribe, reverse, complement or reverse_complement.

Additional functions for filter_fastq (gc_and_quality_calculator)
- `calculate_gc_content` - calculates the percentage of GC content in the sequence.
- `calculate_quality` - calculates the average quality of the sequence over the string of qualities.

Additional functions for run_dna_rna_tools (dna_rna_operations)
- `transcribe` - performs transcription from DNA to RNA.
- `reverse` -  unfolds sequences.
- `complement` - returns complementary DNA or RNA sequences (if the sequence contains T and U at the same time - an error will be reported).
- `reverse_complement` - returns complementary DNA or RNA sequences and unfolds them.

  ## Contacts

  hosp54@gmail.com (Ivan)


