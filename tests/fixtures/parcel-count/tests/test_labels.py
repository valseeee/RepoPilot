import unittest

from parcel_count.labels import count_labels


class LabelTests(unittest.TestCase):
    def test_blank_labels_are_ignored(self):
        self.assertEqual(count_labels(["A", " ", "A"]), 2)
