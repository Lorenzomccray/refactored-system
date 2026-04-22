# /kb/glossary

## Purpose

This page defines project-specific terms and canonical definitions used across `refactored-system`.

## Core terms

### AI Brain
The central execution and orchestration core of the system. It should understand the task, load context, build a plan, authorize the next step, execute and verify, and persist what matters.

### Adapter
An external capability integration that depends on the brain without becoming the brain itself.

### Approval
A policy decision against a classified action. Not a freeform feeling or intuition.

### Approval checkpoint
A step in an execution graph that must be authorized before proceeding.

### Canonical doc
The primary source-of-truth document for a topic.

### Control Plane
The orchestration layer responsible for intake, planning coordination, authorization checks, dispatch, retries or fallbacks, completion gating, and response assembly.

### Cognition Plane
The set of reasoning roles: planner, builder, verifier, researcher, memory, and recovery.

### ExecutionGraph
The first-class executable step graph derived from a plan.

### ExecutionStep
One executable or evaluable unit in the execution graph, with risk class, verification mode, and policy-bound requirements.

### Fail closed
Stop safely with a blocked, denied, deferred, or diagnostic outcome instead of improvising unsafe continuation.

### FailureRecord
A contract capturing classified failure context, recoverability, and suggested recovery path.

### Integration Plane
The external-facing adapter layer for systems such as Supabase, Ollama, MCP, LangGraph, browser-use, and similar capabilities.

### Memory Plane
The layered memory system: working, episodic, semantic, and procedural.

### Procedural memory
Reusable workflows and known-good patterns promoted only after repeated successful, verified use.

### RunReceipt
The replayable, auditable unit that records what happened, under what authorization state, with what outputs and verification.

### Runtime truth docs
Documents describing the current actual system state. These override assumptions.

### Semantic memory
Curated, retrievable, validated knowledge rather than raw transcripts or dump storage.

### Source hierarchy
The ordered preference system for retrieving truth: KB, canonical docs, runtime truth docs, build docs, reference lessons, then external registries.

### Tool Plane
The normalized action layer for shell, browser, file, API, DB, memory, MCP, and automation tools.

### Typed contract
A structured, serializable, versioned object used across plane boundaries instead of an opaque string.

### Validation
The process of checking syntactic, semantic, and or environment truth of a claim or artifact.

### VerificationResult
A structured verifier judgment that keeps syntactic, semantic, and environment outcomes distinct.

### Working memory
Short-lived state for the active run. It is aggressively pruned and not a durable dump of conversations.

## Cross-references
- `/kb/principles`
- `/kb/architecture`
- `/kb/schemas`
- `/kb/safety`
