# SECRETS POLICY

## Purpose
Define secret classes, ownership boundaries, handling rules, and redaction requirements.

## Secret classes
1. Core secrets
2. Adapter secrets
3. Sandbox secrets
4. Ephemeral session secrets

## Core secrets
Examples:
- canonical provider routing credentials
- canonical database credentials
- approval and policy infrastructure credentials

## Adapter secrets
Examples:
- OpenClaw channel tokens
- LiteLLM provider passthrough secrets
- Browser-Use related API credentials
- n8n integration credentials

## Sandbox secrets
Examples:
- prototype-only API keys
- temporary experiment credentials

Sandbox secrets must never be reused as canonical production secrets.

## Ephemeral session secrets
Examples:
- browser cookies
- temporary auth tokens
- one-time session grants

## Hard rules
- No hardcoded secrets in source code.
- No secrets in example files except placeholders.
- No secrets written to semantic memory, receipts, artifacts, or logs.
- Adapters may not read core secrets unless explicitly allowed by policy.
- Browser/session secrets must be isolated from general adapter configs.

## Redaction rule
Before any memory write, receipt write, or artifact persistence, secret-bearing values must be redacted or excluded.
