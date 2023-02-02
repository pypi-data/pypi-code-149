from typing import Final
from volworld_common.api.CA import CA


# ====== A: Attribute ======
class AA(CA):
    Request: Final[str] = "req"

    Response: Final[str] = "rsp"


attList = [AA, CA]
