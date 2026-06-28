import logging
from typing import Dict, List
from .types import Agent, Task, Orchestrator
from .exceptions import InvalidTaskException, AgentNotFoundException

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self, orchestrator: Orchestrator):
        self.orchestrator = orchestrator
        self.agents: Dict[str, Agent] = {}
        self.tasks: List[Task] = []

    def register_agent(self, agent: Agent):
        if agent.id in self.agents:
            raise AgentAlreadyRegisteredException(f"Agent {agent.id} is already registered")
        self.agents[agent.id] = agent
        logger.info(f"Agent {agent.id} registered")

    def assign_task(self, task: Task):
        try:
            if not self.agents:
                raise NoAgentsAvailableException("No agents available to assign task to")
            agent_id = self.get_available_agent()
            self.agents[agent_id].assign_task(task)
            logger.info(f"Task {task.id} assigned to agent {agent_id}")
            self.tasks.append(task)
        except Exception as e:
            raise InvalidTaskException("Error assigning task to agent") from e

    def get_available_agent(self) -> str:
        available_agents = [agent for agent in self.agents.values() if not agent.is_busy()]
        if not available_agents:
            raise NoAgentsAvailableException("No agents available to assign task to")
        return available_agents[0].id

    def monitor_tasks(self):
        for task in self.tasks:
            try:
                task_status = self.get_task_status(task)
                if task_status == TaskStatus.COMPLETED:
                    logger.info(f"Task {task.id} completed")
                    self.tasks.remove(task)
                elif task_status == TaskStatus.FAILED:
                    logger.error(f"Task {task.id} failed")
            except Exception as e:
                raise InvalidTaskException("Error monitoring task") from e

    def get_task_status(self, task: Task) -> TaskStatus:
        try:
            agent = self.agents[task.agent_id]
            return agent.get_task_status(task)
        except Exception as e:
            raise InvalidTaskException("Error getting task status") from e

    def add_orchestrator(self, orchestrator: Orchestrator):
        self.orchestrator = orchestrator

    def start(self):
        self.monitor_tasks()

    def stop(self):
        pass

class InvalidTaskException(Exception):
    pass

class AgentAlreadyRegisteredException(InvalidTaskException):
    pass

class NoAgentsAvailableException(InvalidTaskException):
    pass

class TaskNotFoundException(InvalidTaskException):
    pass