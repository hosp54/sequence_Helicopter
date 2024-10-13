
import os
import os.path

def fastq_to_dict(input_fastq: str) -> dict[str, tuple[str, str, str]]:
    """
    Converts a FASTQ file into a dictionary where each sequence is stored with its associated data.

    Arguments:
    input_fastq -- the path to the input FASTQ file (str).

    Returns:
    A dictionary where the keys are sequence names (str), and the values are tuples containing
    the sequence, quality score, and the plus string (tuple[str, str, str]).
    """
    # Create an empty dictionary to store the sequences
    seqs = {}

    # Open the input FASTQ file
    with open(input_fastq, "r") as fastq:

        # Loop to process the relevant lines and store them in the dictionary
        # We'll read all lines and save them into 4 variables
        # The number of lines must be a multiple of 4, so if a line is missing, the file has ended
        while True:
            seq_name = fastq.readline().strip()  # Read the line and immediately strip whitespace
            if not seq_name:
                break  # Exit the loop if the file has ended
            seq_str = fastq.readline().strip()
            plus_str = fastq.readline().strip()
            quality_str = fastq.readline().strip()

            # Store each iteration as an element in the dictionary
            seqs[seq_name] = (seq_str, quality_str, plus_str)
        
    return seqs


def write_fastq(good_filtered_seqs: dict[str, tuple[str, str, str]], output_fastq: str) -> None:
    """
    Writes the filtered sequences to a FASTQ file in the specified output directory.

    Arguments:
    good_filtered_seqs -- a dictionary where the keys are sequence names (str), and the values are
                          tuples containing the sequence, quality score, and the plus string (tuple[str, str, str]).
    output_fastq -- the name of the output FASTQ file (str).

    Returns:
    None
    """
    # Check if the folder exists at the specified path
    out_dir = "filtered"

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    
    # Create the path for writing the output file
    out_path = os.path.join(out_dir, output_fastq)

    with open(out_path, "w") as filtered:
        # Loop that writes each element in the dictionary
        # as a FASTQ entry using f-strings
        for seq_name, (seq_str, quality_str, plus_str) in good_filtered_seqs.items():
            filtered.write(f"{seq_name}\n{seq_str}\n{plus_str}\n{quality_str}\n")


