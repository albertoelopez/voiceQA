import os

from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from langchain_groq import ChatGroq

search_tool = SerperDevTool()

# Load environment variables from .env file
load_dotenv()

default_llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=os.getenv('GROQ_API_KEY')
)

class ConversationAnalysisAgents():
    def conversation_evaluator(self):
        return Agent(
            role='Conversation Evaluator',
            goal="""Evaluate the quality of the conversation between a 
            chatbot and a human based on given criteria.""",
            backstory="""You are an expert in customer service analysis. 
            You are responsible for evaluating and providing insights on 
            the quality of interactions between chatbots and customers.""",
            verbose=False,
            llm=default_llm, # <----- passing our llm reference here
        )
    # TODO: Could be deleted as well
    def human_agent(self):
        return Agent(
            role='Human speaking on phone',
            goal='Find and summarize the latest AI news',
            backstory="""You're a researcher at a large company.
            You're responsible for analyzing data and providing insights
            to the business.""",
            verbose=False,
            llm=default_llm, 
        )
    # TODO: could be deleted
    def chatbot_agent(self):
        return Agent(
            role='Phone chatbot',
            goal='Find and summarize the latest AI news',
            backstory="""You're a researcher at a large company.
            You're responsible for analyzing data and providing insights
            to the business.""",
            verbose=False,
            llm=default_llm, 
        )
    # WE NEED CONTEXT OF BOTH due to the row data not separated
    def chatbot_human_agent(self):
        return Agent(
            role='Facilitate a phone conversation between a chatbot and a person',
            goal='Determine the effectiveness of the conversation and provide insights for improving chatbot interactions at an insurance company',
            backstory="""You're a researcher at a large insurance company. "
            "You're responsible for analyzing data and providing insights "
            "to the business.""",
            verbose=False,
            llm=default_llm, 
        )
        



# writer_agent = Agent(
#   llm=llm, # <----- passing our llm reference here
#   role='Researcher',
#   goal='Find and summarize the latest AI news',
#   backstory="""You're a researcher at a large company.
#   You're responsible for analyzing data and providing insights
#   to the business.""",
#   verbose=True
# )


# chatbot = Task(
#     description='Find and summarize the latest AI news',
#     expected_output='A bullet list summary of the top 5 most important AI news',
#     async_execution=True,
#     agent=research_agent,
#     tools=[search_tool]
# )

# human = Task(
#     description='Find and summarize the latest AI Ops news',
#     expected_output='A bullet list summary of the top 5 most important AI Ops news',
#     async_execution=True,
#     agent=research_agent,
#     tools=[search_tool]
# )

# write_blog_task = Task(
#     description="Write a full blog post about the importance of AI and its latest news",
#     expected_output='Full blog post that is 4 paragraphs long',
#     agent=writer_agent,
#     context=[chatbot, human]
# )

# crew = Crew(
#     agents=[research_agent, writer_agent],
#     tasks=[chatbot, human, write_blog_task],
#     verbose=2
# )

# result = crew.kickoff()

# print(result)