from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer

# crew = Crew(
#     agents = [news_researcher,news_writer],
#     tasks = [research_task,write_task],
#     process = Process.sequential,
# )

# # starting the task execution process with enhanced feedback

# result = crew.kickoff(inputs={"topic": "AI in Healthcare"})
# print(result)

def run_crew(topic: str):
    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        max_rpm=5,
    )
    return crew.kickoff(inputs={"topic": topic})