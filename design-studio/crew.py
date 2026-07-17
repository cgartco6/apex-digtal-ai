from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

def create_design_crew():
    agent = Agent(
        role="Master Graphic Designer",
        goal="Create exceptional visual designs in any style",
        backstory="World-class designer for logos, flyers, billboards, vehicle wraps and more.",
        verbose=True,
        llm=llm
    )
    task = Task(
        description="Create full design assets including logos, collateral and style guide.",
        expected_output="Complete design package",
        agent=agent
    )
    return Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=1)
