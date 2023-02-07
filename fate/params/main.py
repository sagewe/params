import pydantic.schema

from fate.params import (
    learning_rate_param,
    conint,
    confloat,
    optimizer_param,
    penalty_param,
    string_choice,
    CipherParamType,
    PaillierCipherParam,
    validate_arguments,
    parse,
    jsonschema
)
from typing import Dict, List, Optional, Union


@validate_arguments
def lr(
        penalty: Optional[penalty_param()] = None,
        tol: confloat(gt=0.0) = 1e-4,
        alpha: confloat(gt=0.0) = 1.0,
        optimizer: optimizer_param() = "rmsprop",
        batch_strategy: string_choice({"full", "random"}) = "full",
        batch_size: Optional[int] = None,
        shuffle: bool = True,
        masked_rate: confloat(ge=0.0) = 5.0,
        learning_rate: learning_rate_param() = 0.01,
        max_iter: conint(gt=0) = 100,
        early_stop="diff",
        decay: float = 1.0,
        decay_sqrt: bool = True,
        encrypt_param: CipherParamType = PaillierCipherParam(),
        early_stopping_rounds: Optional[int] = None,
        metrics: Optional[string_choice({"auc", "ks"})] = None,
        use_first_metric_only: bool = False,
        floating_point_precision: Optional[int] = None,
):
    pass


class A(pydantic.BaseModel):
    p: optimizer_param()


if __name__ == "__main__":
    print(parse(optimizer_param(), "sgd") == "sgd")
    print(jsonschema(conint(ge=10, lt=30)))
    print(jsonschema(Union[List[int], Dict[int, int]]))
    # lr(tol=-1)
    print(jsonschema(optimizer_param()))