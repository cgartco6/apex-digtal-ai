from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def create_webdev_crew():
    agent = Agent(
        role="Full-Stack Developer",
        goal="Build production ready web and mobile applications",
        backstory="Expert full-stack developer using modern technologies.",
        verbose=True,
        llm=llm
    )
    task = Task(
        description="Generate complete full-stack web and mobile app code.",
        expected_output="Production ready codebase",
        agent=agent
    )
    return Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=1)
