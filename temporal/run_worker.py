"""Temporal worker bootstrap for the Sovereign AI Work Operating System.

This file intentionally registers workflow skeletons only. Activities are named in
workflow code and will be implemented behind the FastAPI brain/governor, MCP
Gateway, and Cortex receipt layer.
"""

from __future__ import annotations

import asyncio
import os

from temporalio.client import Client
from temporalio.worker import Worker

from temporal.workflows import (
    CapabilityLifecycleWorkflow,
    CapabilityRollbackWorkflow,
    GovernedAgentRunWorkflow,
    GovernedPromotionWorkflow,
    SandboxedUpgradeTestingWorkflow,
)


TEMPORAL_ADDRESS = os.getenv("TEMPORAL_ADDRESS", "localhost:7233")
TEMPORAL_NAMESPACE = os.getenv("TEMPORAL_NAMESPACE", "default")
SOVEREIGN_TASK_QUEUE = os.getenv("SOVEREIGN_TASK_QUEUE", "sovereign-governor")


async def main() -> None:
    """Connect to Temporal and register sovereign workflow definitions."""
    client = await Client.connect(TEMPORAL_ADDRESS, namespace=TEMPORAL_NAMESPACE)

    worker = Worker(
        client,
        task_queue=SOVEREIGN_TASK_QUEUE,
        workflows=[
            GovernedAgentRunWorkflow,
            CapabilityLifecycleWorkflow,
            SandboxedUpgradeTestingWorkflow,
            GovernedPromotionWorkflow,
            CapabilityRollbackWorkflow,
        ],
        activities=[],
    )

    print(
        "Sovereign Temporal worker starting: "
        f"address={TEMPORAL_ADDRESS} namespace={TEMPORAL_NAMESPACE} "
        f"task_queue={SOVEREIGN_TASK_QUEUE}"
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
