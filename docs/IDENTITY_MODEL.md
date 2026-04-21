# IDENTITY MODEL

## Purpose
Define the minimal canonical identity objects used by the core. Adapters must map into this model rather than inventing parallel truth systems.

## Canonical identity objects
- user_id
- operator_id
- session_id
- agent_id
- channel_identity
- credential_scope

## Mapping rule
All adapter sessions, channels, and agent identities must map into canonical identity objects before entering the core.

## Examples
- OpenClaw session state maps into canonical session_id and channel_identity.
- Future agent endpoint identities map into agent_id plus channel_identity, not a new core ontology.

## Approval rule
Every approval decision must be attributable to a canonical operator identity.
