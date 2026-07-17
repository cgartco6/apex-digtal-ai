from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)

def create_branding_crew():
    agent = Agent(
        role="Brand Strategist",
        goal="Develop complete brand identities",
        backstory="Expert in corporate branding and identity systems.",
        verbose=True,
        llm=llm
    )
    task = Task(
        description="Create full brand guidelines and identity kit.",
        expected_output="Complete brand identity package",
        agent=agent
    )
    return Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=1)
