"""Kameleoon Configuration"""

from enum import Enum
from typing import Any, List, Dict, Optional
from kameleoon.configuration.variation_by_exposition import VariationByExposition
from kameleoon.targeting.models import Segment


class Rule:
    """
    Rule is used for saving rule of feature flags (v2) with rules
    """

    class Type(Enum):
        """Possible types of rules"""

        EXPERIMENTATION = "EXPERIMENTATION"
        TARGETED_DELIVERY = "TARGETED_DELIVERY"

    @staticmethod
    def from_array(array: List[Dict[str, Any]]) -> List["Rule"]:
        """Create a list of Rules from the json array"""
        return [Rule(item) for item in array]

    def __init__(self, dict_json: Dict[str, Any]):
        self.order: int = dict_json.get("order", 0)
        self.type: str = dict_json.get("type", "")
        self.exposition: float = dict_json.get("exposition", 0.0)
        self.experiment_id = dict_json.get("experiment_id", None)
        self.variation_by_exposition: List[
            VariationByExposition
        ] = VariationByExposition.from_array(dict_json.get("variationByExposition", []))
        segment = dict_json.get("segment")
        self.targeting_segment: Optional[Segment] = (
            Segment(segment) if segment else None
        )

    def get_variation_key(self, hash_double: float) -> Optional[str]:
        """Calculates the variation key for the given hash of visitor"""
        total = 0.0
        for var_by_exp in self.variation_by_exposition:
            total += var_by_exp.exposition
            if total >= hash_double:
                return var_by_exp.variation_key
        return None

    def get_variation_id_by_key(self, key: str) -> Optional[int]:
        """Find the variation id for the given variation key"""
        var_by_exp = next(
            (v for v in self.variation_by_exposition if v.variation_key == key), None
        )
        return var_by_exp.variation_id if var_by_exp else None
