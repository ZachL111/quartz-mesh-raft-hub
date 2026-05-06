# Review Journal

The repository goal stays the same: implement an SQL distributed systems project for raft policy evaluation, using deny and allow fixtures and explainable decision traces. This note explains the added review angle.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its distributed systems focus without claiming live deployment or external usage.

## Cases

- `baseline`: `quorum health`, score 205, lane `ship`
- `stress`: `lease drift`, score 145, lane `ship`
- `edge`: `replica lag`, score 154, lane `ship`
- `recovery`: `membership churn`, score 184, lane `ship`
- `stale`: `quorum health`, score 168, lane `ship`

## Note

The repository should be understandable without pretending it is larger than it is.
