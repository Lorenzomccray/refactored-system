# ADAPTER BOUNDARIES

## Purpose
Define the contract between the canonical core and external adapters, workers, gateways, and services.

## Adapter rule
Adapters may depend on the core. The core must not depend on any single adapter.

## Every adapter must declare
- inbound data shape
- mapping into canonical schemas
- owned resources
- non-owned resources
- auth and secret requirements
- failure modes
- timeout and retry posture
- emitted receipts or adapter-local logs

## Required normalization rule
No raw adapter payload may cross into the core without canonical schema normalization.

## Forbidden adapter behaviors
- adapter-owned task truth
- adapter-owned approval truth
- adapter-owned memory promotion
- hidden retry loops outside the core state machine
- silent summarization that mutates canonical state

## Disableability rule
Every adapter must be disableable without collapsing the coherence of the canonical core.
