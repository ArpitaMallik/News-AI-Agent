from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

# call the gemini model
llm = ChatGoogleGenerativeAI(model="",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))


# create a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking insights in technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation"
        "and eager to explore and share knowledge about the latest technological advancements."
    ),
    tools = [],
    llm=llm,
    allow_delegation=True
)

# create a writer agent with custom tools responsible in writing news blog

news_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and inform readers about technological innovations."
    ),
    tools = [],
    llm=llm,
    allow_delegation=False 
)