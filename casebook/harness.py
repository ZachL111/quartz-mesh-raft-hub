"""Executable checks for the quartz-mesh-raft-hub casebook."""

from __future__ import annotations

from collections import Counter

from . import quartz_mesh_raft_hub_segment_00
from . import quartz_mesh_raft_hub_segment_01
from . import quartz_mesh_raft_hub_segment_02
from . import quartz_mesh_raft_hub_segment_03
from . import quartz_mesh_raft_hub_segment_04
from . import quartz_mesh_raft_hub_segment_05
from . import quartz_mesh_raft_hub_segment_06
from . import quartz_mesh_raft_hub_segment_07
from . import quartz_mesh_raft_hub_segment_08
from . import quartz_mesh_raft_hub_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from quartz_mesh_raft_hub_segment_00.iter_quartz_mesh_raft_hub_00()
    yield from quartz_mesh_raft_hub_segment_01.iter_quartz_mesh_raft_hub_01()
    yield from quartz_mesh_raft_hub_segment_02.iter_quartz_mesh_raft_hub_02()
    yield from quartz_mesh_raft_hub_segment_03.iter_quartz_mesh_raft_hub_03()
    yield from quartz_mesh_raft_hub_segment_04.iter_quartz_mesh_raft_hub_04()
    yield from quartz_mesh_raft_hub_segment_05.iter_quartz_mesh_raft_hub_05()
    yield from quartz_mesh_raft_hub_segment_06.iter_quartz_mesh_raft_hub_06()
    yield from quartz_mesh_raft_hub_segment_07.iter_quartz_mesh_raft_hub_07()
    yield from quartz_mesh_raft_hub_segment_08.iter_quartz_mesh_raft_hub_08()
    yield from quartz_mesh_raft_hub_segment_09.iter_quartz_mesh_raft_hub_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def quartz_mesh_raft_hub_summary() -> dict:
    return assert_expected()
