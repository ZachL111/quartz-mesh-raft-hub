# quartz-mesh-raft-hub

`quartz-mesh-raft-hub` is a compact SQL repository for distributed systems, centered on this goal: Implement an SQL distributed systems project for raft policy evaluation, using deny and allow fixtures and explainable decision traces.

## Reason For The Project

This is intentionally local and self-contained so it can be inspected without credentials, services, or seeded history.

## Quartz Mesh Raft Hub Review Notes

`baseline` and `stress` are the cases worth reading first. They show the optimistic and cautious ends of the fixture.

## What It Does

- `fixtures/domain_review.csv` adds cases for quorum health and lease drift.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/quartz-mesh-raft-walkthrough.md` walks through the case spread.
- The SQL code includes a review path for `quorum health` and `lease drift`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## How It Is Put Together

The repository has two validation layers: the original compact policy fixture and the domain review fixture. They are separate so one can change without hiding failures in the other.

The SQL checks add a separate view over the domain review fixture.

## Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Check It

The check exercises the source code and the review fixture. `baseline` is the high score at 205; `stress` is the low score at 145.

## Boundaries

The repository is intentionally scoped to local checks. I would expand it by adding adversarial fixtures before adding features.
