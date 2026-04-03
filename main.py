from app.orchestrator.router import Router
from app.orchestrator.dispatcher import Dispatcher


def run(task: str) -> None:
    router = Router()
    dispatcher = Dispatcher()

    role = router.route(task)
    result = dispatcher.dispatch(role, task)

    print(f"[{role.upper()} RESULT]")
    print(result)


if __name__ == "__main__":
    run("build an AI system")
