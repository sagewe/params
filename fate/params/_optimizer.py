from ._fields import StringChoice
from typing import Type


class Optimizer(StringChoice):
    chooice = {}


def optimizer_param(rmsprop=True, sgd=True, adam=True, nesterov_momentum_sgd=True, adagrad=True) -> Type[str]:
    choice = dict(rmsprop=rmsprop, sgd=sgd, adam=adam, nesterov_momentum_sgd=nesterov_momentum_sgd, adagrad=adagrad)
    namespace = dict(
        chooice={k for k, v in choice.items() if v},
    )
    return type("OptimizerValue", (StringChoice,), namespace)
