"""Stubs for more_itertools.more"""

from __future__ import annotations

import sys
import types

from typing import (
    Any,
    Callable,
    Container,
    ContextManager,
    Generic,
    Hashable,
    Iterable,
    Iterator,
    Mapping,
    overload,
    Reversible,
    Sequence,
    Sized,
    Type,
    TypeVar,
    type_check_only,
)
from typing_extensions import Protocol

__all__ = [
    'AbortThread',
    'SequenceView',
    'UnequalIterablesError',
    'adjacent',
    'all_unique',
    'always_iterable',
    'always_reversible',
    'bucket',
    'callback_iter',
    'chunked',
    'chunked_even',
    'circular_shifts',
    'collapse',
    'combination_index',
    'combination_with_replacement_index',
    'consecutive_groups',
    'constrained_batches',
    'consumer',
    'count_cycle',
    'countable',
    'dft',
    'difference',
    'distinct_combinations',
    'distinct_permutations',
    'distribute',
    'divide',
    'doublestarmap',
    'duplicates_everseen',
    'duplicates_justseen',
    'classify_unique',
    'exactly_n',
    'filter_except',
    'filter_map',
    'first',
    'gray_product',
    'groupby_transform',
    'ichunked',
    'iequals',
    'idft',
    'ilen',
    'interleave',
    'interleave_evenly',
    'interleave_longest',
    'intersperse',
    'is_sorted',
    'islice_extended',
    'iterate',
    'iter_suppress',
    'join_mappings',
    'last',
    'locate',
    'longest_common_prefix',
    'lstrip',
    'make_decorator',
    'map_except',
    'map_if',
    'map_reduce',
    'mark_ends',
    'minmax',
    'nth_or_last',
    'nth_permutation',
    'nth_prime',
    'nth_product',
    'nth_combination_with_replacement',
    'numeric_range',
    'one',
    'only',
    'outer_product',
    'padded',
    'partial_product',
    'partitions',
    'peekable',
    'permutation_index',
    'powerset_of_sets',
    'product_index',
    'raise_',
    'repeat_each',
    'repeat_last',
    'replace',
    'rlocate',
    'rstrip',
    'run_length',
    'sample',
    'seekable',
    'set_partitions',
    'side_effect',
    'sliced',
    'sort_together',
    'split_after',
    'split_at',
    'split_before',
    'split_into',
    'split_when',
    'spy',
    'stagger',
    'strip',
    'strictly_n',
    'substrings',
    'substrings_indexes',
    'takewhile_inclusive',
    'time_limited',
    'unique_in_window',
    'unique_to_each',
    'unzip',
    'value_chain',
    'windowed',
    'windowed_complete',
    'with_iter',
    'zip_broadcast',
    'zip_equal',
    'zip_offset',
]

# Type and type variable definitions
_T = TypeVar('_T')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_U = TypeVar('_U')
_V = TypeVar('_V')
_W = TypeVar('_W')
_T_co = TypeVar('_T_co', covariant=True)
_GenFn = TypeVar('_GenFn', bound=Callable[..., Iterator[Any]])
_Raisable = BaseException | Type[BaseException]

# The type of isinstance's second argument (from typeshed builtins)
if sys.version_info >= (3, 10):
    _ClassInfo = type | types.UnionType | tuple[_ClassInfo, ...]
else:
    _ClassInfo = type | tuple[_ClassInfo, ...]

@type_check_only
class _SizedIterable(Protocol[_T_co], Sized, Iterable[_T_co]): ...

@type_check_only
class _SizedReversible(Protocol[_T_co], Sized, Reversible[_T_co]): ...

@type_check_only
class _SupportsSlicing(Protocol[_T_co]):
    def __getitem__(self, __k: slice) -> _T_co: ...

def chunked(
    iterable: Iterable[_T], n: int | None, strict: bool = ...
) -> Iterator[list[_T]]: ...
@overload
def first(iterable: Iterable[_T]) -> _T: ...
@overload
def first(iterable: Iterable[_T], default: _U) -> _T | _U: ...
@overload
def last(iterable: Iterable[_T]) -> _T: ...
@overload
def last(iterable: Iterable[_T], default: _U) -> _T | _U: ...
@overload
def nth_or_last(iterable: Iterable[_T], n: int) -> _T: ...
@overload
def nth_or_last(iterable: Iterable[_T], n: int, default: _U) -> _T | _U: ...

class peekable(Generic[_T], Iterator[_T]):
    def __init__(self, iterable: Iterable[_T]) -> None: ...
    def __iter__(self) -> peekable[_T]: ...
    def __bool__(self) -> bool: ...
    @overload
    def peek(self) -> _T: ...
    @overload
    def peek(self, default: _U) -> _T | _U: ...
    def prepend(self, *items: _T) -> None: ...
    def __next__(self) -> _T: ...
    @overload
    def __getitem__(self, index: int) -> _T: ...
    @overload
    def __getitem__(self, index: slice) -> list[_T]: ...

def consumer(func: _GenFn) -> _GenFn: ...
def ilen(iterable: Iterable[_T]) -> int: ...
def iterate(func: Callable[[_T], _T], start: _T) -> Iterator[_T]: ...
def with_iter(
    context_manager: ContextManager[Iterable[_T]],
) -> Iterator[_T]: ...
def one(
    iterable: Iterable[_T],
    too_short: _Raisable | None = ...,
    too_long: _Raisable | None = ...,
) -> _T: ...
def raise_(exception: _Raisable, *args: Any) -> None: ...
def strictly_n(
    iterable: Iterable[_T],
    n: int,
    too_short: _GenFn | None = ...,
    too_long: _GenFn | None = ...,
) -> list[_T]: ...
def distinct_permutations(
    iterable: Iterable[_T], r: int | None = ...
) -> Iterator[tuple[_T, ...]]: ...
def intersperse(
    e: _U, iterable: Iterable[_T], n: int = ...
) -> Iterator[_T | _U]: ...
def unique_to_each(*iterables: Iterable[_T]) -> list[list[_T]]: ...
@overload
def windowed(
    seq: Iterable[_T], n: int, *, step: int = ...
) -> Iterator[tuple[_T | None, ...]]: ...
@overload
def windowed(
    seq: Iterable[_T], n: int, fillvalue: _U, step: int = ...
) -> Iterator[tuple[_T | _U, ...]]: ...
def substrings(iterable: Iterable[_T]) -> Iterator[tuple[_T, ...]]: ...
def substrings_indexes(
    seq: Sequence[_T], reverse: bool = ...
) -> Iterator[tuple[Sequence[_T], int, int]]: ...

class bucket(Generic[_T, _U], Container[_U]):
    def __init__(
        self,
        iterable: Iterable[_T],
        key: Callable[[_T], _U],
        validator: Callable[[_U], object] | None = ...,
    ) -> None: ...
    def __contains__(self, value: object) -> bool: ...
    def __iter__(self) -> Iterator[_U]: ...
    def __getitem__(self, value: object) -> Iterator[_T]: ...

def spy(
    iterable: Iterable[_T], n: int = ...
) -> tuple[list[_T], Iterator[_T]]: ...
def interleave(*iterables: Iterable[_T]) -> Iterator[_T]: ...
def interleave_longest(*iterables: Iterable[_T]) -> Iterator[_T]: ...
def interleave_evenly(
    iterables: list[Iterable[_T]], lengths: list[int] | None = ...
) -> Iterator[_T]: ...
def collapse(
    iterable: Iterable[Any],
    base_type: _ClassInfo | None = ...,
    levels: int | None = ...,
) -> Iterator[Any]: ...
@overload
def side_effect(
    func: Callable[[_T], object],
    iterable: Iterable[_T],
    chunk_size: None = ...,
    before: Callable[[], object] | None = ...,
    after: Callable[[], object] | None = ...,
) -> Iterator[_T]: ...
@overload
def side_effect(
    func: Callable[[list[_T]], object],
    iterable: Iterable[_T],
    chunk_size: int,
    before: Callable[[], object] | None = ...,
    after: Callable[[], object] | None = ...,
) -> Iterator[_T]: ...
def sliced(
    seq: _SupportsSlicing[_T], n: int, strict: bool = ...
) -> Iterator[_T]: ...
def split_at(
    iterable: Iterable[_T],
    pred: Callable[[_T], object],
    maxsplit: int = ...,
    keep_separator: bool = ...,
) -> Iterator[list[_T]]: ...
def split_before(
    iterable: Iterable[_T], pred: Callable[[_T], object], maxsplit: int = ...
) -> Iterator[list[_T]]: ...
def split_after(
    iterable: Iterable[_T], pred: Callable[[_T], object], maxsplit: int = ...
) -> Iterator[list[_T]]: ...
def split_when(
    iterable: Iterable[_T],
    pred: Callable[[_T, _T], object],
    maxsplit: int = ...,
) -> Iterator[list[_T]]: ...
def split_into(
    iterable: Iterable[_T], sizes: Iterable[int | None]
) -> Iterator[list[_T]]: ...
@overload
def padded(
    iterable: Iterable[_T],
    *,
    n: int | None = ...,
    next_multiple: bool = ...,
) -> Iterator[_T | None]: ...
@overload
def padded(
    iterable: Iterable[_T],
    fillvalue: _U,
    n: int | None = ...,
    next_multiple: bool = ...,
) -> Iterator[_T | _U]: ...
@overload
def repeat_last(iterable: Iterable[_T]) -> Iterator[_T]: ...
@overload
def repeat_last(iterable: Iterable[_T], default: _U) -> Iterator[_T | _U]: ...
def distribute(n: int, iterable: Iterable[_T]) -> list[Iterator[_T]]: ...
@overload
def stagger(
    iterable: Iterable[_T],
    offsets: _SizedIterable[int] = ...,
    longest: bool = ...,
) -> Iterator[tuple[_T | None, ...]]: ...
@overload
def stagger(
    iterable: Iterable[_T],
    offsets: _SizedIterable[int] = ...,
    longest: bool = ...,
    fillvalue: _U = ...,
) -> Iterator[tuple[_T | _U, ...]]: ...

class UnequalIterablesError(ValueError):
    def __init__(self, details: tuple[int, int, int] | None = ...) -> None: ...

# zip_equal
@overload
def zip_equal(__iter1: Iterable[_T1]) -> Iterator[tuple[_T1]]: ...
@overload
def zip_equal(
    __iter1: Iterable[_T1], __iter2: Iterable[_T2]
) -> Iterator[tuple[_T1, _T2]]: ...
@overload
def zip_equal(
    __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3]
) -> Iterator[tuple[_T1, _T2, _T3]]: ...
@overload
def zip_equal(
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    __iter3: Iterable[_T3],
    __iter4: Iterable[_T4],
) -> Iterator[tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def zip_equal(
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    __iter3: Iterable[_T3],
    __iter4: Iterable[_T4],
    __iter5: Iterable[_T5],
) -> Iterator[tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def zip_equal(
    __iter1: Iterable[Any],
    __iter2: Iterable[Any],
    __iter3: Iterable[Any],
    __iter4: Iterable[Any],
    __iter5: Iterable[Any],
    __iter6: Iterable[Any],
    *iterables: Iterable[Any],
) -> Iterator[tuple[Any, ...]]: ...

# zip_offset
@overload
def zip_offset(
    __iter1: Iterable[_T1],
    *,
    offsets: _SizedIterable[int],
    longest: bool = ...,
    fillvalue: None = None,
) -> Iterator[tuple[_T1 | None]]: ...
@overload
def zip_offset(
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    *,
    offsets: _SizedIterable[int],
    longest: bool = ...,
    fillvalue: None = None,
) -> Iterator[tuple[_T1 | None, _T2 | None]]: ...
@overload
def zip_offset(
    __iter1: Iterable[_T],
    __iter2: Iterable[_T],
    __iter3: Iterable[_T],
    *iterables: Iterable[_T],
    offsets: _SizedIterable[int],
    longest: bool = ...,
    fillvalue: None = None,
) -> Iterator[tuple[_T | None, ...]]: ...
@overload
def zip_offset(
    __iter1: Iterable[_T1],
    *,
    offsets: _SizedIterable[int],
    longest: bool = ...,
    fillvalue: _U,
) -> Iterator[tuple[_T1 | _U]]: ...
@overload
def zip_offset(
    __iter1: Iterable[_T1],
    __iter2: Iterable[_T2],
    *,
    offsets: _SizedIterable[int],
    longest: bool = ...,
    fillvalue: _U,
) -> Iterator[tuple[_T1 | _U, _T2 | _U]]: ...
@overload
def zip_offset(
    __iter1: Iterable[_T],
    __iter2: Iterable[_T],
    __iter3: Iterable[_T],
    *iterables: Iterable[_T],
    offsets: _SizedIterable[int],
    longest: bool = ...,
    fillvalue: _U,
) -> Iterator[tuple[_T | _U, ...]]: ...
def sort_together(
    iterables: Iterable[Iterable[_T]],
    key_list: Iterable[int] = ...,
    key: Callable[..., Any] | None = ...,
    reverse: bool = ...,
    strict: bool = ...,
) -> list[tuple[_T, ...]]: ...
def unzip(iterable: Iterable[Sequence[_T]]) -> tuple[Iterator[_T], ...]: ...
def divide(n: int, iterable: Iterable[_T]) -> list[Iterator[_T]]: ...
def always_iterable(
    obj: object,
    base_type: _ClassInfo | None = ...,
) -> Iterator[Any]: ...
def adjacent(
    predicate: Callable[[_T], bool],
    iterable: Iterable[_T],
    distance: int = ...,
) -> Iterator[tuple[bool, _T]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: None = None,
    valuefunc: None = None,
    reducefunc: None = None,
) -> Iterator[tuple[_T, Iterator[_T]]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: None,
    reducefunc: None,
) -> Iterator[tuple[_U, Iterator[_T]]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: None,
    valuefunc: Callable[[_T], _V],
    reducefunc: None,
) -> Iterable[tuple[_T, Iterable[_V]]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: Callable[[_T], _V],
    reducefunc: None,
) -> Iterable[tuple[_U, Iterator[_V]]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: None,
    valuefunc: None,
    reducefunc: Callable[[Iterator[_T]], _W],
) -> Iterable[tuple[_T, _W]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: None,
    reducefunc: Callable[[Iterator[_T]], _W],
) -> Iterable[tuple[_U, _W]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: None,
    valuefunc: Callable[[_T], _V],
    reducefunc: Callable[[Iterable[_V]], _W],
) -> Iterable[tuple[_T, _W]]: ...
@overload
def groupby_transform(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: Callable[[_T], _V],
    reducefunc: Callable[[Iterable[_V]], _W],
) -> Iterable[tuple[_U, _W]]: ...

class numeric_range(Generic[_T, _U], Sequence[_T], Hashable, Reversible[_T]):
    @overload
    def __init__(self, __stop: _T) -> None: ...
    @overload
    def __init__(self, __start: _T, __stop: _T) -> None: ...
    @overload
    def __init__(self, __start: _T, __stop: _T, __step: _U) -> None: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, elem: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __getitem__(self, key: int) -> _T: ...
    @overload
    def __getitem__(self, key: slice) -> numeric_range[_T, _U]: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __len__(self) -> int: ...
    def __reduce__(
        self,
    ) -> tuple[Type[numeric_range[_T, _U]], tuple[_T, _T, _U]]: ...
    def __repr__(self) -> str: ...
    def __reversed__(self) -> Iterator[_T]: ...
    def count(self, value: _T) -> int: ...
    def index(self, value: _T) -> int: ...  # type: ignore

def count_cycle(
    iterable: Iterable[_T], n: int | None = ...
) -> Iterable[tuple[int, _T]]: ...
def mark_ends(
    iterable: Iterable[_T],
) -> Iterable[tuple[bool, bool, _T]]: ...
def locate(
    iterable: Iterable[_T],
    pred: Callable[..., Any] = ...,
    window_size: int | None = ...,
) -> Iterator[int]: ...
def lstrip(
    iterable: Iterable[_T], pred: Callable[[_T], object]
) -> Iterator[_T]: ...
def rstrip(
    iterable: Iterable[_T], pred: Callable[[_T], object]
) -> Iterator[_T]: ...
def strip(
    iterable: Iterable[_T], pred: Callable[[_T], object]
) -> Iterator[_T]: ...

class islice_extended(Generic[_T], Iterator[_T]):
    def __init__(self, iterable: Iterable[_T], *args: int | None) -> None: ...
    def __iter__(self) -> islice_extended[_T]: ...
    def __next__(self) -> _T: ...
    def __getitem__(self, index: slice) -> islice_extended[_T]: ...

def always_reversible(iterable: Iterable[_T]) -> Iterator[_T]: ...
def consecutive_groups(
    iterable: Iterable[_T], ordering: Callable[[_T], int] = ...
) -> Iterator[Iterator[_T]]: ...
@overload
def difference(
    iterable: Iterable[_T],
    func: Callable[[_T, _T], _U] = ...,
    *,
    initial: None = ...,
) -> Iterator[_T | _U]: ...
@overload
def difference(
    iterable: Iterable[_T], func: Callable[[_T, _T], _U] = ..., *, initial: _U
) -> Iterator[_U]: ...

class SequenceView(Generic[_T], Sequence[_T]):
    def __init__(self, target: Sequence[_T]) -> None: ...
    @overload
    def __getitem__(self, index: int) -> _T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[_T]: ...
    def __len__(self) -> int: ...

class seekable(Generic[_T], Iterator[_T]):
    def __init__(
        self, iterable: Iterable[_T], maxlen: int | None = ...
    ) -> None: ...
    def __iter__(self) -> seekable[_T]: ...
    def __next__(self) -> _T: ...
    def __bool__(self) -> bool: ...
    @overload
    def peek(self) -> _T: ...
    @overload
    def peek(self, default: _U) -> _T | _U: ...
    def elements(self) -> SequenceView[_T]: ...
    def seek(self, index: int) -> None: ...
    def relative_seek(self, count: int) -> None: ...

class run_length:
    @staticmethod
    def encode(iterable: Iterable[_T]) -> Iterator[tuple[_T, int]]: ...
    @staticmethod
    def decode(iterable: Iterable[tuple[_T, int]]) -> Iterator[_T]: ...

def exactly_n(
    iterable: Iterable[_T], n: int, predicate: Callable[[_T], object] = ...
) -> bool: ...
def circular_shifts(
    iterable: Iterable[_T], steps: int = 1
) -> list[tuple[_T, ...]]: ...
def make_decorator(
    wrapping_func: Callable[..., _U], result_index: int = ...
) -> Callable[..., Callable[[Callable[..., Any]], Callable[..., _U]]]: ...
@overload
def map_reduce(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: None = ...,
    reducefunc: None = ...,
) -> dict[_U, list[_T]]: ...
@overload
def map_reduce(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: Callable[[_T], _V],
    reducefunc: None = ...,
) -> dict[_U, list[_V]]: ...
@overload
def map_reduce(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: None = ...,
    reducefunc: Callable[[list[_T]], _W] = ...,
) -> dict[_U, _W]: ...
@overload
def map_reduce(
    iterable: Iterable[_T],
    keyfunc: Callable[[_T], _U],
    valuefunc: Callable[[_T], _V],
    reducefunc: Callable[[list[_V]], _W],
) -> dict[_U, _W]: ...
def rlocate(
    iterable: Iterable[_T],
    pred: Callable[..., object] = ...,
    window_size: int | None = ...,
) -> Iterator[int]: ...
def replace(
    iterable: Iterable[_T],
    pred: Callable[..., object],
    substitutes: Iterable[_U],
    count: int | None = ...,
    window_size: int = ...,
) -> Iterator[_T | _U]: ...
def partitions(iterable: Iterable[_T]) -> Iterator[list[list[_T]]]: ...
def set_partitions(
    iterable: Iterable[_T],
    k: int | None = ...,
    min_size: int | None = ...,
    max_size: int | None = ...,
) -> Iterator[list[list[_T]]]: ...

class time_limited(Generic[_T], Iterator[_T]):
    def __init__(
        self, limit_seconds: float, iterable: Iterable[_T]
    ) -> None: ...
    def __iter__(self) -> islice_extended[_T]: ...
    def __next__(self) -> _T: ...

@overload
def only(
    iterable: Iterable[_T], *, too_long: _Raisable | None = ...
) -> _T | None: ...
@overload
def only(
    iterable: Iterable[_T], default: _U, too_long: _Raisable | None = ...
) -> _T | _U: ...
def ichunked(iterable: Iterable[_T], n: int) -> Iterator[Iterator[_T]]: ...
def distinct_combinations(
    iterable: Iterable[_T], r: int
) -> Iterator[tuple[_T, ...]]: ...
def filter_except(
    validator: Callable[[Any], object],
    iterable: Iterable[_T],
    *exceptions: Type[BaseException],
) -> Iterator[_T]: ...
def map_except(
    function: Callable[[Any], _U],
    iterable: Iterable[_T],
    *exceptions: Type[BaseException],
) -> Iterator[_U]: ...
def map_if(
    iterable: Iterable[Any],
    pred: Callable[[Any], bool],
    func: Callable[[Any], Any],
    func_else: Callable[[Any], Any] | None = ...,
) -> Iterator[Any]: ...
def _sample_unweighted(
    iterator: Iterator[_T], k: int, strict: bool
) -> list[_T]: ...
def _sample_counted(
    population: Iterator[_T], k: int, counts: Iterable[int], strict: bool
) -> list[_T]: ...
def _sample_weighted(
    iterator: Iterator[_T], k: int, weights: Iterator[float], strict: bool
) -> list[_T]: ...
def sample(
    iterable: Iterable[_T],
    k: int,
    weights: Iterable[float] | None = ...,
    *,
    counts: Iterable[int] | None = ...,
    strict: bool = False,
) -> list[_T]: ...
def is_sorted(
    iterable: Iterable[_T],
    key: Callable[[_T], _U] | None = ...,
    reverse: bool = False,
    strict: bool = False,
) -> bool: ...

class AbortThread(BaseException):
    pass

class callback_iter(Generic[_T], Iterator[_T]):
    def __init__(
        self,
        func: Callable[..., Any],
        callback_kwd: str = ...,
        wait_seconds: float = ...,
    ) -> None: ...
    def __enter__(self) -> callback_iter[_T]: ...
    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> bool | None: ...
    def __iter__(self) -> callback_iter[_T]: ...
    def __next__(self) -> _T: ...
    def _reader(self) -> Iterator[_T]: ...
    @property
    def done(self) -> bool: ...
    @property
    def result(self) -> Any: ...

def windowed_complete(
    iterable: Iterable[_T], n: int
) -> Iterator[tuple[tuple[_T, ...], tuple[_T, ...], tuple[_T, ...]]]: ...
def all_unique(
    iterable: Iterable[_T], key: Callable[[_T], _U] | None = ...
) -> bool: ...
def nth_product(index: int, *args: Iterable[_T]) -> tuple[_T, ...]: ...
def nth_combination_with_replacement(
    iterable: Iterable[_T], r: int, index: int
) -> tuple[_T, ...]: ...
def nth_permutation(
    iterable: Iterable[_T], r: int, index: int
) -> tuple[_T, ...]: ...
def value_chain(*args: _T | Iterable[_T]) -> Iterable[_T]: ...
def product_index(element: Iterable[_T], *args: Iterable[_T]) -> int: ...
def combination_index(
    element: Iterable[_T], iterable: Iterable[_T]
) -> int: ...
def combination_with_replacement_index(
    element: Iterable[_T], iterable: Iterable[_T]
) -> int: ...
def permutation_index(
    element: Iterable[_T], iterable: Iterable[_T]
) -> int: ...
def repeat_each(iterable: Iterable[_T], n: int = ...) -> Iterator[_T]: ...

class countable(Generic[_T], Iterator[_T]):
    def __init__(self, iterable: Iterable[_T]) -> None: ...
    def __iter__(self) -> countable[_T]: ...
    def __next__(self) -> _T: ...
    items_seen: int

def chunked_even(iterable: Iterable[_T], n: int) -> Iterator[list[_T]]: ...
@overload
def zip_broadcast(
    __obj1: _T | Iterable[_T],
    *,
    scalar_types: _ClassInfo | None = ...,
    strict: bool = ...,
) -> Iterable[tuple[_T, ...]]: ...
@overload
def zip_broadcast(
    __obj1: _T | Iterable[_T],
    __obj2: _T | Iterable[_T],
    *,
    scalar_types: _ClassInfo | None = ...,
    strict: bool = ...,
) -> Iterable[tuple[_T, ...]]: ...
@overload
def zip_broadcast(
    __obj1: _T | Iterable[_T],
    __obj2: _T | Iterable[_T],
    __obj3: _T | Iterable[_T],
    *,
    scalar_types: _ClassInfo | None = ...,
    strict: bool = ...,
) -> Iterable[tuple[_T, ...]]: ...
@overload
def zip_broadcast(
    __obj1: _T | Iterable[_T],
    __obj2: _T | Iterable[_T],
    __obj3: _T | Iterable[_T],
    __obj4: _T | Iterable[_T],
    *,
    scalar_types: _ClassInfo | None = ...,
    strict: bool = ...,
) -> Iterable[tuple[_T, ...]]: ...
@overload
def zip_broadcast(
    __obj1: _T | Iterable[_T],
    __obj2: _T | Iterable[_T],
    __obj3: _T | Iterable[_T],
    __obj4: _T | Iterable[_T],
    __obj5: _T | Iterable[_T],
    *,
    scalar_types: _ClassInfo | None = ...,
    strict: bool = ...,
) -> Iterable[tuple[_T, ...]]: ...
@overload
def zip_broadcast(
    __obj1: _T | Iterable[_T],
    __obj2: _T | Iterable[_T],
    __obj3: _T | Iterable[_T],
    __obj4: _T | Iterable[_T],
    __obj5: _T | Iterable[_T],
    __obj6: _T | Iterable[_T],
    *objects: _T | Iterable[_T],
    scalar_types: _ClassInfo | None = ...,
    strict: bool = ...,
) -> Iterable[tuple[_T, ...]]: ...
def unique_in_window(
    iterable: Iterable[_T], n: int, key: Callable[[_T], _U] | None = ...
) -> Iterator[_T]: ...
def duplicates_everseen(
    iterable: Iterable[_T], key: Callable[[_T], _U] | None = ...
) -> Iterator[_T]: ...
def duplicates_justseen(
    iterable: Iterable[_T], key: Callable[[_T], _U] | None = ...
) -> Iterator[_T]: ...
def classify_unique(
    iterable: Iterable[_T], key: Callable[[_T], _U] | None = ...
) -> Iterator[tuple[_T, bool, bool]]: ...

class _SupportsLessThan(Protocol):
    def __lt__(self, __other: Any) -> bool: ...

_SupportsLessThanT = TypeVar("_SupportsLessThanT", bound=_SupportsLessThan)

@overload
def minmax(
    iterable_or_value: Iterable[_SupportsLessThanT], *, key: None = None
) -> tuple[_SupportsLessThanT, _SupportsLessThanT]: ...
@overload
def minmax(
    iterable_or_value: Iterable[_T], *, key: Callable[[_T], _SupportsLessThan]
) -> tuple[_T, _T]: ...
@overload
def minmax(
    iterable_or_value: Iterable[_SupportsLessThanT],
    *,
    key: None = None,
    default: _U,
) -> _U | tuple[_SupportsLessThanT, _SupportsLessThanT]: ...
@overload
def minmax(
    iterable_or_value: Iterable[_T],
    *,
    key: Callable[[_T], _SupportsLessThan],
    default: _U,
) -> _U | tuple[_T, _T]: ...
@overload
def minmax(
    iterable_or_value: _SupportsLessThanT,
    __other: _SupportsLessThanT,
    *others: _SupportsLessThanT,
) -> tuple[_SupportsLessThanT, _SupportsLessThanT]: ...
@overload
def minmax(
    iterable_or_value: _T,
    __other: _T,
    *others: _T,
    key: Callable[[_T], _SupportsLessThan],
) -> tuple[_T, _T]: ...
def longest_common_prefix(
    iterables: Iterable[Iterable[_T]],
) -> Iterator[_T]: ...
def iequals(*iterables: Iterable[Any]) -> bool: ...
def constrained_batches(
    iterable: Iterable[_T],
    max_size: int,
    max_count: int | None = ...,
    get_len: Callable[[_T], object] = ...,
    strict: bool = ...,
) -> Iterator[tuple[_T]]: ...
def gray_product(*iterables: Iterable[_T]) -> Iterator[tuple[_T, ...]]: ...
def partial_product(*iterables: Iterable[_T]) -> Iterator[tuple[_T, ...]]: ...
def takewhile_inclusive(
    predicate: Callable[[_T], bool], iterable: Iterable[_T]
) -> Iterator[_T]: ...
def outer_product(
    func: Callable[[_T, _U], _V],
    xs: Iterable[_T],
    ys: Iterable[_U],
    *args: Any,
    **kwargs: Any,
) -> Iterator[tuple[_V, ...]]: ...
def iter_suppress(
    iterable: Iterable[_T],
    *exceptions: Type[BaseException],
) -> Iterator[_T]: ...
def filter_map(
    func: Callable[[_T], _V | None],
    iterable: Iterable[_T],
) -> Iterator[_V]: ...
def powerset_of_sets(iterable: Iterable[_T]) -> Iterator[set[_T]]: ...
def join_mappings(
    **field_to_map: Mapping[_T, _V]
) -> dict[_T, dict[str, _V]]: ...
def doublestarmap(
    func: Callable[..., _T],
    iterable: Iterable[Mapping[str, Any]],
) -> Iterator[_T]: ...
def dft(xarr: Sequence[complex]) -> Iterator[complex]: ...
def idft(Xarr: Sequence[complex]) -> Iterator[complex]: ...
def _nth_prime_ub(n: int) -> float: ...
def nth_prime(n: int) -> int: ...
