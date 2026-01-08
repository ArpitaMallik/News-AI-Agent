from crewai import Agent
from crewai.llm import LLM
from tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gemini-2.5-flash"
,
    provider="google",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.5,
)

news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking insights in technologies in {topic}",
    verbose=True,
    memory=False,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation "
        "and eager to explore and share knowledge about the latest technological advancements."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True,
)

news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=False,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and inform readers."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False,
)
