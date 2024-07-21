import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq
search_tool = SerperDevTool()

# Load environment variables from .env file
load_dotenv()

llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=os.getenv('GROQ_API_KEY')
)

research_agent = Agent(
  role='Researcher',
  goal='Find and summarize the latest AI news',
  backstory="""You're a researcher at a large company.
  You're responsible for analyzing data and providing insights
  to the business.""",
  verbose=True,
  llm=llm, # <----- passing our llm reference here
)

writer_agent = Agent(
  llm=llm, # <----- passing our llm reference here
  role='Researcher',
  goal='Find and summarize the latest AI news',
  backstory="""You're a researcher at a large company.
  You're responsible for analyzing data and providing insights
  to the business.""",
  verbose=True
)


chatbot = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    async_execution=True,
    agent=research_agent,
    tools=[search_tool]
)

human = Task(
    description='Find and summarize the latest AI Ops news',
    expected_output='A bullet list summary of the top 5 most important AI Ops news',
    async_execution=True,
    agent=research_agent,
    tools=[search_tool]
)

write_blog_task = Task(
    description="Write a full blog post about the importance of AI and its latest news",
    expected_output='Full blog post that is 4 paragraphs long',
    agent=writer_agent,
    context=[chatbot, human]
)

crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[chatbot, human, write_blog_task],
    verbose=2
)

result = crew.kickoff()

print(result)