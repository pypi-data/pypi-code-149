from dataclasses import dataclass

from cerbeyra.src.dto import CerbeyraIndex


@dataclass
class UbiqumIndex(CerbeyraIndex):
    @classmethod
    def build_from_index(cls, ci: CerbeyraIndex):
        return cls(index=ci.index, risk_level=ci.risk_level, explain=ci.explain)
