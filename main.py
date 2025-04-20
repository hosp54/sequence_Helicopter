import argparse
import logging
from sequence_helicopter import filter_fastq

def main():
    parser = argparse.ArgumentParser(description="Filter FASTQ sequences based on GC content, length, and quality.")
    parser.add_argument("input_fastq", type=str, help="Path to the input FASTQ file.")
    parser.add_argument("output_fastq", type=str, help="Path to save the filtered FASTQ file.")
    parser.add_argument("--min_gc", type=float, default=0, help="Minimum GC content percentage.")
    parser.add_argument("--max_gc", type=float, default=100, help="Maximum GC content percentage.")
    parser.add_argument("--min_length", type=int, default=0, help="Minimum sequence length.")
    parser.add_argument("--max_length", type=int, default=2**32, help="Maximum sequence length.")
    parser.add_argument("--quality_threshold", type=float, default=0, help="Minimum average quality score.")

    args = parser.parse_args()

    logging.basicConfig(
        filename='filter_fastq_log.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    logging.info(f"Starting filtering for {args.input_fastq}")

    try:
        filter_fastq(
            input_fastq=args.input_fastq,
            output_fastq=args.output_fastq,
            gc_bounds=(args.min_gc, args.max_gc),
            length_bounds=(args.min_length, args.max_length),
            quality_threshold=args.quality_threshold,
        )
        logging.info(f"Filtering completed. Output saved to {args.output_fastq}")
    except Exception as e:
        logging.error(f"Error during filtering: {e}")
        raise

if __name__ == "__main__":
    main()