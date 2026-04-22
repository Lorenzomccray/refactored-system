# PROVIDER ROUTING

## Purpose
Define how the canonical core selects models and providers without hardwiring any agent role to a single vendor or service.

## Core rule
Agents request capabilities.
They do not choose providers directly.

The provider router selects the provider path according to:
- task role
- risk and policy
- privacy requirement
- cost policy
- health status
- fallback policy
- environment constraints

## Canonical routing goals
- strongest reasoning where needed
- cheapest acceptable model where possible
- local/private path for sensitive work when available
- deterministic fallback behavior
- no provider-specific logic inside planner, builder, or verifier

## Canonical routing roles

### Planner
Use the highest reasoning-capable route available for planning, decomposition, and constraint formation.

### Builder
Use the strongest execution-capable route that matches the tool and coding demands of the step.

### Verifier
Use the strongest structured-output and consistency-oriented route available.

### Research / summarization
Prefer cheaper and faster models unless the task requires deep reasoning.

### Sensitive / private
Prefer local or private provider paths when policy requires it.

## Provider decision inputs
The router must consider:
- `task_type`
- `agent_role`
- `risk_class`
- `privacy_level`
- `latency_budget`
- `cost_budget`
- `requires_tool_reasoning`
- `requires_structured_output`
- `requires_local_only`
- `provider_health`

## Fallback chain
1. retry same provider/model
2. retry with narrowed scope or reduced context
3. alternate provider with equivalent role capability
4. re-plan with downgraded capability or narrower scope
5. fail closed with diagnostic artifact

## Required router outputs
Every routing decision must emit:
- chosen provider
- chosen model
- routing reason
- fallback candidates
- privacy classification
- cost expectation class
- receipt linkage

## Hard rules
- No provider should be hardwired into planner, builder, or verifier roles.
- No provider fallback may bypass policy restrictions.
- No local-only task may silently route to a remote provider.
- No adapter gateway may become the sole owner of provider truth.
- The router must support both gateway-routed and direct adapter-routed paths when policy allows.

## Initial implementation posture
### Phase 1
- define provider capability registry
- define routing policy schema
- define health and fallback hooks

### Phase 2
- implement canonical provider router
- integrate one remote path and one local/private path
- emit routing receipts

### Phase 3
- add health-aware failover
- add cost-aware routing
- add stricter privacy and policy gating
