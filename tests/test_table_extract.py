import unittest
from table_extract import extract_tables

class TableTests(unittest.TestCase):
    def test_extracts_and_pads_rows(self):
        html="<table><tr><th>A</th><th>B</th></tr><tr><td>x</td></tr></table>"
        self.assertEqual(extract_tables(html),[[["A","B"],["x",""]]])

    def test_ignores_text_outside_tables(self):
        self.assertEqual(extract_tables("<p>none</p>"),[])

if __name__=="__main__": unittest.main()
