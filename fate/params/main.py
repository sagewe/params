import pydantic
from fate.params import (
    learning_rate,
    conint,
    confloat,
    optimizer,
    penalty,
    strchoice,
    CipherParamType,
    PaillierCipherParam,
)
from typing import Optional
from fate.params import parse


@pydantic.validate_arguments
def lr(
    penalty: Optional[penalty()] = None,
    tol: confloat(gt=0.0) = 1e-4,
    alpha: confloat(gt=0.0) = 1.0,
    optimizer: optimizer() = "rmsprop",
    batch_strategy: strchoice({"full", "random"}) = "full",
    batch_size: Optional[int] = None,
    shuffle: bool = True,
    masked_rate: confloat(ge=0.0) = 5.0,
    learning_rate: learning_rate() = 0.01,
    max_iter: conint(gt=0) = 100,
    early_stop="diff",
    decay: float = 1.0,
    decay_sqrt: bool = True,
    encrypt_param: CipherParamType = PaillierCipherParam(),
    early_stopping_rounds: Optional[int] = None,
    metrics: Optional[strchoice({"auc", "ks"})] = None,
    use_first_metric_only: bool = False,
    floating_point_precision: Optional[int] = None,
):
    pass


if __name__ == "__main__":
    lr(tol=-1)
