import unittest
from packages.core import Agent, Engine, Orchestrator, Task
from services.orchestrator import OrchestratorService

class TestPipeline(unittest.TestCase):
    def test_end_to_end(self):
        engine = Engine(orchestrator=Orchestrator(id='default'))
        agent = Agent(id='test-agent')
        engine.register_agent(agent=agent)
        task = Task(id='test-task', agent_id=agent.id)
        engine.assign_task(task=task)
        orchestrator_service = OrchestratorService(engine=engine)
        orchestrator_service.start()
        self.assertIsNotNone(engine.orchestrator)

if __name__ == '__main__':
    unittest.main()