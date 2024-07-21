from textwrap import dedent

from crewai import Crew
from dotenv import load_dotenv

from voice_analysis_agents import VoiceAnalysisAgents
from voice_analysis_tasks import VoiceAnalysisTasks

load_dotenv()

class VoiceAnalysisCrew:
  def __init__(self, company):
    self.company = company

  def run(self):
    agents = VoiceAnalysisAgents()
    tasks = VoiceAnalysisTasks()

    conversation_analyst_agent = agents.conversation_evaluator()
    human_agent = agents.human_agent()
    chatbot_agent = agents.chatbot_agent()
    
    chatbot_task = tasks.chatbot_analysis_task(conversation_analyst_agent, self.company, "")
    human_task = tasks.human_analysis_task(human_agent)
    conversation_task = tasks.conversation_context_task(chatbot_agent)

    crew = Crew(
      agents=[
        conversation_analyst_agent,
        human_agent,
        chatbot_agent
      ],
      tasks=[
        chatbot_task,
        human_task,
        conversation_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Financial Analysis Crew")
  print('-------------------------------')
  # we need to define the inputs here
  company = input(
    dedent("""
      What is the company you want to analyze?
    """))
  
  financial_crew = VoiceAnalysisCrew(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)
