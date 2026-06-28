from packages.core import Engine
from packages.core.exceptions import InvalidTaskException

class OrchestratorService:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()