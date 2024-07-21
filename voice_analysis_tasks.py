from textwrap import dedent

from crewai import Task


class VoiceAnalysisTasks():
  # Need both human and chatbot conversation since on same row
  def chatbot_human_analysis_task(self, agent, chatbot_human_conversation):
    return Task(description=dedent(f"""
        'Evaluate the quality of the chatbot conversation based on the following 
        criteria:
      """),
      agent=agent,
      expected_output= "A bullet list summary of the top 5 most important analytics",
    context=[chatbot_human_conversation]
    )
  def chatbot_analysis_task(self, agent):
    return Task(description=dedent(f"""
        'Evaluate the quality of the chatbot conversation based on the following 
        criteria:
      """),
      agent=agent,
      expected_output= "A bullet list summary of the top 5 most important analytics",
    )
  def human_analysis_task(self, agent): 
    return Task(description=dedent(f"""
        Evaluate the quality of the human conversation based on the following criteria:
      """),
      agent=agent,
      expected_output= "A bullet list summary of the top 5 most important analytics",
    )
  def conversation_context_task(self, agent, human_conversation, chatbot_conversation):
    return Task(
    description='Provide sample conversation between chatbot and human for evaluation.',
    expected_output='A sample conversation for analysis',
    agent=agent,
    context=[human_conversation, chatbot_conversation]
)
