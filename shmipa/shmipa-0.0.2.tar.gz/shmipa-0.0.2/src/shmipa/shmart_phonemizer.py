import appdirs
import gdown
import json
import os
from typing import List, Tuple
from dp.phonemizer import Phonemizer
from functools import reduce

default_shmart_rules = [
    ('ɛː', 'ɛr'),
    ('aː', 'ɛ'),
    ('tju', 't͡ʂiu'),
    ('uːɡ', 'u-'),
    (' kɛ', ' ːkɛ'),
]

class ShmartPhonemizer():
    def __init__(self, to_ipa_path: str = None, from_ipa_path: str = None, lang='pl') -> None:
        with open(os.path.join(os.path.dirname(__file__), 'models.json')) as models_file:
            predefined_models = json.load(models_file)
            if not to_ipa_path:
                to_ipa_path = predefined_models['autoregressive_en_to_ipa']
            if not from_ipa_path:
                from_ipa_path = predefined_models['forward_ipa_to_pl']

        self.from_ipa = self._load_model(from_ipa_path)
        self.to_ipa = self._load_model(to_ipa_path)
        self.rules = default_shmart_rules
        self.lang = lang

    def __call__(self, text: str) -> str:
        return reduce(
            lambda result, fn: fn(result),
            [
                self.get_ipa,
                self._apply_rules,
                self.revert_ipa
            ],
            text
        )

    def set_rules(self, rules: List[Tuple[str, str]]) -> None:
        self.rules = rules

    def revert_ipa(self, text: str) -> str:
        return self.from_ipa(text, self.lang)

    def get_ipa(self, text: str) -> str:
        return self.to_ipa(text, self.lang)

    def _apply_rules(self, text: str) -> str:
        for from_, to_ in self.rules:
            text = text.replace(from_, to_)
        return text

    def _load_model(self, path_or_id: str):
        if os.path.exists(path_or_id):
            return Phonemizer.from_checkpoint(path_or_id)
        else:
            cache_dir = appdirs.user_cache_dir('shmart_ipa', 'shmart')
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)
            cache_path = os.path.join(cache_dir, path_or_id)
            if not os.path.exists(cache_path):
                gdown.download(id=path_or_id, output=cache_path)
            return Phonemizer.from_checkpoint(cache_path)