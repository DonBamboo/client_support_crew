from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from client_support_crew.results import ClientCommunicationResult
from typing import List

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class ClientSupportCrew:
    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def full_stack_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["full_stack_developer"],  # type: ignore[index]
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def client_services_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["client_services_manager"],  # type: ignore[index]
            allow_delegation=False,
            verbose=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def debugging_task(self) -> Task:
        return Task(
            config=self.tasks_config["debugging_task"],  # type: ignore[index]
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
        )

    @task
    def client_communication_task(self) -> Task:
        return Task(
            config=self.tasks_config["client_communication_task"],  # type: ignore[index]
            output_json=ClientCommunicationResult,
        )

    @crew
    def crew(self) -> Crew:
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
