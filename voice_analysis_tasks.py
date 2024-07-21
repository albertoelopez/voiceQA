from textwrap import dedent

from crewai import Task


class VoiceAnalysisTasks():
  def chatbot_analysis_task(self, agent, company, chatbot_evaluation_criteria):
    return Task(description=dedent(f"""
        'Evaluate the quality of the chatbot conversation based on the following 
        criteria:
        {chatbot_evaluation_criteria}
  
    Selected company by the customer: {company}
      """),
      agent=agent
    )
    
  def human_analysis_task(self, agent, human_evaluation_criteria): 
    return Task(description=dedent(f"""
        Evaluate the quality of the human conversation based on the following criteria:
        {human_evaluation_criteria}
      """),
      agent=agent
    )
  def conversation_context_task(self, agent, human_conversation, chatbot_conversation):
    return Task(
    description='Provide sample conversation between chatbot and human for evaluation.',
    expected_output='A sample conversation for analysis',
    agent=agent,
    context=[human_conversation, chatbot_conversation]
)