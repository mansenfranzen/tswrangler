"""This module contains the reference implementation for the interval
identification wrangler.

An interval is defined as a range of values beginning with an opening marker
and ending with a closing marker (e.g. the interval daylight may be defined as
all events/values occurring between sunrise and sunset).

The interval identification wrangler assigns ids to values such that values
belonging to the same interval share the same interval id. For example, all
values of the first daylight interval are assigned with id 1. All values of the
second daylight interval will be assigned with id 2 and so on. Values which do
not belong to any valid interval are assigned the value 0 by definition.

Only the shortest valid interval is identified. Given multiple opening markers,
only the last is relevant and the rest is ignored. Given multiple closing
markers, only the first is relevant and the rest is ignored.

"""

from typing import Any, List, Union

import pandas as pd

COLS_TYPE = Union[str, List[str]]


def naive_iterator(df: pd.DataFrame,
                   col_markers: str,
                   cols_order: COLS_TYPE,
                   cols_groupby: COLS_TYPE,
                   marker_start: Any,
                   marker_end: Any,
                   order: List[str] = None) -> pd.Series:
    pass
