from ._fields import StringChoice
from typing import Type


class Penalty(StringChoice):
    chooice = {}


def penalty(l1=True, l2=True) -> Type[str]:
    choice = {"L1": l1, "L2": l2}
    namespace = dict(
        chooice={k for k, v in choice.items() if v},
    )
    return type("PenaltyValue", (Penalty,), namespace)
