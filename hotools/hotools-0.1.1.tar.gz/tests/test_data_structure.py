import unittest

from hotools import data_structure


class DictionaryCounterTest(unittest.TestCase):
    def _make_data(self) -> data_structure.DictionaryCounter:
        """検証用のデータを生成する

        returns:
            DictionaryCounter クラスのオブジェクト
        """
        dictionary_counter = data_structure.DictionaryCounter()

        dictionary_counter.count('apple')
        dictionary_counter.count('orange')
        dictionary_counter.count('apple')
        dictionary_counter.count('orange')
        dictionary_counter.count('apple')

        return dictionary_counter

    def test_count(self):
        dictionary_counter = self._make_data()

        self.assertEqual(dictionary_counter.dictionary['apple'], 3)
        self.assertEqual(dictionary_counter.dictionary['orange'], 2)

    def test_multi_counts(self):
        dictionary_counter = data_structure.DictionaryCounter()

        dictionary_counter.count('apple', number=2)
        dictionary_counter.count('apple', number=8)
        dictionary_counter.count('orange', number=3)

        self.assertEqual(dictionary_counter.dictionary['apple'], 10)
        self.assertEqual(dictionary_counter.dictionary['orange'], 3)

    def test_get_count(self):
        dictionary_counter = self._make_data()

        self.assertEqual(dictionary_counter.get_count('apple'), 3)
        self.assertEqual(dictionary_counter.get_count('orange'), 2)
        self.assertEqual(dictionary_counter.get_count('banana'), 0)

    def test_get_total_count(self):
        dictionary_counter = self._make_data()

        self.assertEqual(dictionary_counter.get_total_count(), 5)


if __name__ == '__main__':
    unittest.main()
