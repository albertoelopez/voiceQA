from textwrap import dedent
import os

from crewai import Crew
from dotenv import load_dotenv

from voice_analysis_agents import ConversationAnalysisAgents
from voice_analysis_tasks import VoiceAnalysisTasks
from tools.readCSV import read_and_display_csv

load_dotenv()

class VoiceAnalysisCrew:
  # def __init__(self, company):
  #   self.company = company

  def run(self, transcriptions):
    agents = ConversationAnalysisAgents()
    tasks = VoiceAnalysisTasks()

    conversation_analyst_agent = agents.conversation_evaluator()
    human_agent = agents.human_agent()
    chatbot_agent = agents.chatbot_agent()
    # Need this agent because we don't want to have two separate data
    # chatbot_human_agent = agents.chatbot_human_agent()
   
    # Need this agent because we don't want to have two separate data
    # chatbot_human_task = tasks.chatbot_human_analysis_task(chatbot_human_agent, "transcription here") 
    chatbot_task = tasks.chatbot_analysis_task(chatbot_agent)
    human_task = tasks.human_analysis_task(human_agent)
    conversation_task = tasks.conversation_context_task(conversation_analyst_agent, human_task, chatbot_task)
    # WE NEED THIS CASE, we don't want to separate conversation between chatbot and human
    # conversation_task = tasks.conversation_context_task(conversation_analyst_agent, chatbot_human_task)

    crew = Crew(
      agents=[
        conversation_analyst_agent,
        human_agent,
        chatbot_agent,
        #chatbot_human_agent
      ],
      tasks=[
        chatbot_task,
        human_task,
        #chatbot_human_task,
        conversation_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Financial Analysis Crew")
  print('-------------------------------')
  file_path = 'example_files/interesse_information_rows.csv'
  transcriptions = read_and_display_csv(file_path)
  qa_results = []
  for trans in transcriptions:
    voice_qa_crew = VoiceAnalysisCrew()
    result = voice_qa_crew.run(trans)
    qa_results.append(result)
  # we need to define the inputs here
  # company = input(
  #   dedent("""
  #     What is the company you want to analyze?
  #   """))
  
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(qa_results)
