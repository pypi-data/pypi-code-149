from typing import Any, Dict, List, Optional

from fuzzy_multi_dict import FuzzyMultiDict


class SpellChecker:
    """
    Simple Spell Checker is a spell checker based on prefix tree search.
    It find nearest to input word from known words (from input list).
    The algorithm finds mistakes in a word (insertions, deletions, replacements).

    """
    def __init__(
        self,
        max_mistakes_number: Optional[int] = 3,
        max_mistakes_number_part: Optional[float] = None,
    ):
        """
        :param Optional[int] max_mistakes_number: default value of maximum number
               of corrections in the query key when searching for a matching key
        :param Optional[float] max_mistakes_number_part: default value to calculate
               maximum number of corrections in the query key when searching
               for a matching dictionary key;
               calculated as round(max_mistakes_number_part * token_length)

        """
        self.__vocab = FuzzyMultiDict(
            max_mistakes_number=max_mistakes_number,
            max_mistakes_number_part=max_mistakes_number_part,
        )

    def add_words(self, words: List[str]):
        for word in set(words):

            if not isinstance(word, str):
                raise TypeError(f"Invalid word type; expect str; got {type(word)}")

            if not len(word):
                raise ValueError("Empty value")

            self.__vocab[word] = word

    def correction(
        self,
        word: str,
        max_mistakes_number: Optional[int] = None,
        max_mistakes_number_part: Optional[float] = None,
    ) -> List[Dict[str, Any]]:
        """
        :param word: word to correct
        :param int max_mistakes_number: maximum number of corrections in the word
        :param max_mistakes_number_part: value to calculate maximum number
               of corrections in the word;
               if not None - `max_mistakes_number` will be ignored;
               calculated as round(max_mistakes_number_part * word_length);

        :return List[Dict[str, Any]]: result in next format
            [
                {
                    'word': <corrected word>,
                    'corrections': <list of corrections>
                },
                ...
            ]

        """
        return [
            {"word": row["value"], "corrections": row["mistakes"]}
            for row in self.__vocab.get(
                key=word,
                max_mistakes_number=max_mistakes_number,
                max_mistakes_number_part=max_mistakes_number_part,
            )
        ]
