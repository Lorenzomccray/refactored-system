# SOURCE CONFLICT POLICY

## Purpose

This file defines what to do when two sources disagree.

## Status date
2026-04-22

## General rule

The higher-tier source wins. See `docs/SOURCE_AUTHORITY_MATRIX.md` for the tier ordering.

## Conflict detection

A conflict exists when:
* Two files in different tiers make contradictory factual claims.
* A runtime truth file contradicts a canonical doc on current state.
* A KB page contradicts a canonical doc on policy.
* A build doc contradicts a canonical doc on contracts or schema.

## Resolution steps

1. **Identify the tier** of each conflicting source.
2. **Surface the conflict explicitly** — do not silently resolve it.
3. **Defer to the higher-tier source** for the answer.
4. **File an update** to bring the lower-tier source into alignment.
5. **Log the resolution** in `docs/EXECUTION_RECEIPTS.md` if it affected a decision.

## When tiers are equal

If two files at the same tier conflict:
* Prefer the more recently updated file.
* If recency is unclear, surface the conflict and escalate to the repository owner.

## Prohibited actions

* Do not merge conflicting claims silently.
* Do not treat chat memory as a tiebreaker.
* Do not update a higher-tier source to match a lower-tier source without explicit authorization.

## Related files

* `docs/SOURCE_AUTHORITY_MATRIX.md`
* `docs/CORE_SOURCES_INDEX.md`
* `kb/repo-rules.md`
