import unittest
from text_file_handling.text_file_data_extractor import TextFileDataExtractor

class TestTextFileDataExtractor(unittest.TestCase):

    def test_no_nodes(self):
        text_file_extractor = TextFileDataExtractor(r"unit_testing_data/text_file_data_extractor_data/no_nodes.txt")
        self.assertRaises(Exception(),text_file_extractor.extract_text_file_data())

if __name__ == '__main__':
    unittest.main()