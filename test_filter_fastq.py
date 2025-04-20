import unittest
from unittest.mock import patch, mock_open
from sequence_helicopter import filter_fastq
import logging

class TestFilterFastq(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    @patch("Bio.SeqIO.parse")
    def test_filter_fastq_success(self, mock_parse, mock_open):
        """
        Check that filtering sequences based on the given criteria
        results in writing the correct data to the file.
        """
        mock_parse.return_value = [
            SeqRecord(Seq("ATGCGT"), id="seq1", letter_annotations={"phred_quality": [30, 30, 30]}),
            SeqRecord(Seq("TTGCCA"), id="seq2", letter_annotations={"phred_quality": [20, 20, 20]}),
        ]

        mock_open.return_value.__enter__.return_value = mock_open.return_value

        filter_fastq(
            input_fastq="input.fastq",
            output_fastq="output.fastq",
            gc_bounds=(40, 60),
            length_bounds=(5, 10),
            quality_threshold=25
        )

        mock_open.return_value.write.assert_called()

        self.assertEqual(mock_open.return_value.write.call_count, 1)

    @patch("builtins.open", new_callable=mock_open)
    @patch("Bio.SeqIO.parse")
    def test_filter_fastq_no_valid_sequences(self, mock_parse, mock_open):
        """
        Check that if all sequences fail the filtering criteria,
        nothing is written to the output file.
        """
        mock_parse.return_value = [
            SeqRecord(Seq("ATGCGT"), id="seq1", letter_annotations={"phred_quality": [10, 10, 10]}),
            SeqRecord(Seq("TTGCCA"), id="seq2", letter_annotations={"phred_quality": [5, 5, 5]}),
        ]

        mock_open.return_value.__enter__.return_value = mock_open.return_value

        filter_fastq(
            input_fastq="input.fastq",
            output_fastq="output.fastq",
            gc_bounds=(40, 60),
            length_bounds=(5, 10),
            quality_threshold=25
        )

        mock_open.return_value.write.assert_not_called()

    @patch("builtins.open", new_callable=mock_open)
    def test_logging_error(self, mock_open):
        """
        Check that an error (e.g., file not found) is logged when it occurs.
        """
        with self.assertRaises(Exception):
            filter_fastq(
                input_fastq="invalid.fastq",
                output_fastq="output.fastq",
                gc_bounds=(40, 60),
                length_bounds=(5, 10),
                quality_threshold=25
            )

        logging.error.assert_called_with("Error occurred during filtering process:")

class TestErrors(unittest.TestCase):

    def test_invalid_gc_bounds(self):
        """
        Check that if invalid GC bounds are provided, a ValueError is raised.
        """
        with self.assertRaises(ValueError):
            filter_fastq(
                input_fastq="input.fastq",
                output_fastq="output.fastq",
                gc_bounds=(200, 300),
                length_bounds=(5, 10),
                quality_threshold=25
            )
    
    def test_invalid_length_bounds(self):
        """
        Check that if invalid length bounds are provided, a ValueError is raised.
        """
        with self.assertRaises(ValueError):
            filter_fastq(
                input_fastq="input.fastq",
                output_fastq="output.fastq",
                gc_bounds=(40, 60),
                length_bounds=(100, 10),
                quality_threshold=25
            )

class TestFileOperations(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open)
    def test_write_to_file(self, mock_open):
        """
        Check that when writing sequences to a file, the file is opened in write mode.
        """
        mock_open.return_value.__enter__.return_value = mock_open.return_value
        filter_fastq(
            input_fastq="input.fastq",
            output_fastq="output.fastq",
            gc_bounds=(40, 60),
            length_bounds=(5, 10),
            quality_threshold=25
        )

        mock_open.assert_called_with("output.fastq", "w")

    @patch("builtins.open", new_callable=mock_open)
    def test_read_from_file(self, mock_open):
        """
        Check that when reading from a file, the file is opened in read mode.
        """
        mock_open.return_value.__enter__.return_value = mock_open.return_value
        filter_fastq(
            input_fastq="input.fastq",
            output_fastq="output.fastq",
            gc_bounds=(40, 60),
            length_bounds=(5, 10),
            quality_threshold=25
        )

        mock_open.assert_called_with("input.fastq", "r")


if __name__ == "__main__":
    unittest.main()