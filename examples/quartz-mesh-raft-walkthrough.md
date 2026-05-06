# Quartz Mesh Raft Hub Walkthrough

The fixture is intentionally compact, so the review starts with the cases that pull farthest apart.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | quorum health | 205 | ship |
| stress | lease drift | 145 | ship |
| edge | replica lag | 154 | ship |
| recovery | membership churn | 184 | ship |
| stale | quorum health | 168 | ship |

Start with `baseline` and `stress`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

`baseline` is the optimistic case; use it to make sure the scoring path still rewards strong signal.
