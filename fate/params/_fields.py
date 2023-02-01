import pydantic
import typing
from typing import TypeVar, Type, Any, Optional


class Parameter:
    @classmethod
    def parse(cls, obj: Any):
        return pydantic.parse_obj_as(cls, obj)

    @classmethod
    def dict(cls):
        raise NotImplementedError()


T = TypeVar("T")


def parse(type_: Type[T], obj: Any) -> T:
    if not isinstance(type_, typing._GenericAlias) and issubclass(type_, Parameter):
        return type_.parse(obj)
    else:
        return pydantic.parse_obj_as(type_, obj)


class ConstrainedInt(pydantic.ConstrainedInt, Parameter):
    ...


def conint(
    *,
    strict: bool = False,
    gt: int = None,
    ge: int = None,
    lt: int = None,
    le: int = None,
    multiple_of: int = None,
) -> Type[int]:
    namespace = dict(strict=strict, gt=gt, ge=ge, lt=lt, le=le, multiple_of=multiple_of)
    return type("ConstrainedIntValue", (ConstrainedInt,), namespace)


class ConstrainedFloat(pydantic.ConstrainedFloat, Parameter):
    ...


def confloat(
    *,
    strict: bool = False,
    gt: float = None,
    ge: float = None,
    lt: float = None,
    le: float = None,
    multiple_of: float = None,
    allow_inf_nan: Optional[bool] = None,
) -> Type[float]:
    namespace = dict(
        strict=strict,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
    )
    return type("ConstrainedFloatValue", (ConstrainedFloat,), namespace)


class StringChoice(str, Parameter):
    chooice = set()

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        yield get_string_chooice_validator(cls.chooice)


def get_string_chooice_validator(chooices):
    def string_chooice_validator(v):
        assert v in chooices, f"should be one of {chooices}"
        return v

    return string_chooice_validator


def string_choice(chooice) -> Type[str]:
    namespace = dict(
        chooice=chooice,
    )
    return type("StringChoice", (StringChoice,), namespace)
