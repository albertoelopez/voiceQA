from crewai import Crew
from textwrap import dedent

from stock_analysis_agents import StockAnalysisAgents
from stock_analysis_tasks import StockAnalysisTasks
from voice_analysis_agents import ConversationAnalysisAgents
from voice_analysis_tasks import  VoiceAnalysisTasks

from dotenv import load_dotenv
load_dotenv()

class FinancialCrew:
  def __init__(self, company):
    self.company = company

  def run(self):
    agents = ConversationAnalysisAgents()
    tasks = VoiceAnalysisTasks() 

    conversation_eval_agent = agents.conversation_evaluator()
    human_agent = agents.human_agent()
    chatbot_agent = agents.chatbot_agent()

    chatbot_task = tasks.chatbot_analysis_task(conversation_eval_agent, self.company)
    human_task = tasks.human_analysis_task(human_agent)
    conversation_task = tasks.conversation_context_task(chatbot_agent)

    crew = Crew(
      agents=[
        research
        conversation_eval_agent,
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
  company = input(
    dedent("""
      What is the company you want to analyze?
    """))
  
  financial_crew = FinancialCrew(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)
