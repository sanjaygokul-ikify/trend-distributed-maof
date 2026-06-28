import unittest
from packages.core import Agent, Engine, Orchestrator, Task, TaskStatus

class TestCore(unittest.TestCase):
    def test_agent_registration(self):
        engine = Engine(orchestrator=Orchestrator(id='default'))
        agent = Agent(id='test-agent')
        engine.register_agent(agent=agent)
        self.assertIn(agent.id, engine.agents)

    def test_task_assignment(self):
        engine = Engine(orchestrator=Orchestrator(id='default'))
        agent = Agent(id='test-agent')
        engine.register_agent(agent=agent)
        task = Task(id='test-task', agent_id=agent.id)
        engine.assign_task(task=task)
        self.assertFalse(engine.agents[agent.id].is_busy)

    def test_task_status(self):
        engine = Engine(orchestrator=Orchestrator(id='default'))
        agent = Agent(id='test-agent')
        engine.register_agent(agent=agent)
        task = Task(id='test-task', agent_id=agent.id)
        engine.assign_task(task=task)
        task_status = engine.get_task_status(task=task)
        self.assertEqual(task_status, TaskStatus.PENDING)

if __name__ == '__main__':
    unittest.main()