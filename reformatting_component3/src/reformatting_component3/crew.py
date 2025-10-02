from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from reformatting_component3.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

from crewai_tools import PDFSearchTool



@CrewBase
class ReformattingComponent3():
	"""ReformattingComponent3 crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def emergency_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['emergency_manager'],
			tool=[PDFSearchTool(pdf='/Users/madeleine/reformatting_component3/nws_training_document.pdf')], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@task
	def evacuation_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['evacuation_research_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ReformattingComponent3 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
