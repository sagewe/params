from typing import Type
import enum


class Optimizer(enum.StrEnum):
    @classmethod
    def __modify_schema__(
            cls, field_schema: dict
    ):
        field_schema['description'] = "optimizer params"


def optimizer_param(rmsprop=True, sgd=True, adam=True, nesterov_momentum_sgd=True, adagrad=True) -> Type[str]:
    choice = dict(rmsprop=rmsprop, sgd=sgd, adam=adam, nesterov_momentum_sgd=nesterov_momentum_sgd, adagrad=adagrad)
    return Optimizer("OptimizerParam", {k: k for k, v in choice.items() if v})
