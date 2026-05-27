from __future__ import annotations

from collections.abc import Iterable


def to_filter_string(ids: Iterable[int] | None) -> str:
    """Convert a collection of integer IDs to a compact SPACE GASS filter string.

    Non-positive values are ignored. The output is sorted and deduplicated.
    Runs of 3+ consecutive values collapse to ranges (e.g. ``[3,4,5]`` → ``"3-5"``).

    Examples:
        >>> to_filter_string([1, 3, 4, 5, 6, 7, 10])
        '1,3-7,10'
        >>> to_filter_string([5, 1, 5, 3, 1])
        '1,3,5'
        >>> to_filter_string([])
        ''
    """
    if ids is None:
        return ""

    sorted_ids = sorted(set(id_ for id_ in ids if id_ > 0))
    if not sorted_ids:
        return ""

    segments: list[str] = []
    run_start = sorted_ids[0]
    run_end = sorted_ids[0]

    for id_ in sorted_ids[1:]:
        if id_ == run_end + 1:
            run_end = id_
        else:
            _append_run(segments, run_start, run_end)
            run_start = id_
            run_end = id_

    _append_run(segments, run_start, run_end)
    return ",".join(segments)


def to_id_list(filter_str: str | None) -> list[int]:
    """Parse a SPACE GASS filter string into a sorted, distinct list of positive integers.

    Ranges like ``"3-7"`` expand to all values in the inclusive range.
    Reversed ranges like ``"7-3"`` are normalised.
    Whitespace around tokens is tolerated.

    Raises:
        ValueError: If the string contains non-numeric characters, non-positive
            values, or the keyword ``"all"``.

    Examples:
        >>> to_id_list('1,3-7,10')
        [1, 3, 4, 5, 6, 7, 10]
        >>> to_id_list(' 1 , 3 - 7 ')
        [1, 3, 4, 5, 6, 7]
        >>> to_id_list('')
        []
    """
    if not filter_str or not filter_str.strip():
        return []

    result: list[int] = []

    for raw in filter_str.split(","):
        token = raw.strip()
        if not token:
            continue

        if token.lower() == "all":
            raise ValueError('The keyword "all" is not a valid ID list.')

        if "-" in token:
            dash_idx = token.index("-")
            if dash_idx == 0:
                raise ValueError(f'Invalid token in ID list: "{token}".')

            start_str = token[:dash_idx].strip()
            end_str = token[dash_idx + 1 :].strip()

            try:
                start = int(start_str)
                end = int(end_str)
            except ValueError:
                raise ValueError(f'Invalid token in ID list: "{token}".')

            lo, hi = min(start, end), max(start, end)
            result.extend(range(lo, hi + 1))
        else:
            try:
                result.append(int(token))
            except ValueError:
                raise ValueError(f'Invalid token in ID list: "{token}".')

    sorted_ids = sorted(set(result))

    for id_ in sorted_ids:
        if id_ <= 0:
            raise ValueError(f'Non-positive ID "{id_}" is not valid.')

    return sorted_ids


def _append_run(segments: list[str], start: int, end: int) -> None:
    if end - start >= 2:
        segments.append(f"{start}-{end}")
    elif end - start == 1:
        segments.append(f"{start},{end}")
    else:
        segments.append(str(start))
