from textwrap import dedent

from crewai import Task

# Define the evaluation criteria for the conversations
evaluation_criteria = """
1. First Call Resolution (FCR): Was the issue resolved on the first interaction?
2. Average Handle Time (AHT): Was the conversation efficient?
3. Customer Satisfaction (CSAT): Was the customer satisfied with the interaction?
4. Net Promoter Score (NPS): Would the customer recommend the service?
5. Service Level: Was the response time within acceptable limits?
6. Call Abandonment Rate: Did the customer abandon the chat before resolution?
7. Transfer Rate: Was the conversation transferred to another agent or department?
8. Customer Effort Score (CES): How much effort did the customer have to put in to get their issue resolved?
"""

class VoiceAnalysisTasks():
  # Need both human and chatbot conversation since on same row
  def chatbot_human_analysis_task(self, agent, chatbot_human_conversation):
    return Task(description=dedent(f"""
        Evaluate the quality of the conversation between a chatbot and a human based on the following criteria:\n{evaluation_criteria}
      """),
      agent=agent,
      async_execution=True,
      expected_output= "A detailed evaluation report based on the criteria",
      context=[chatbot_human_conversation]
    )
  # TODO: could be deleted if we use above
  def chatbot_analysis_task(self, agent):
    return Task(description=dedent(f"""
        'Evaluate the quality of the chatbot conversation based on the following 
        criteria:
      """),
      agent=agent,
      expected_output= "A bullet list summary of the top 5 most important analytics",
    )
   # TODO: Could be deleted if we use above
  def human_analysis_task(self, agent): 
    return Task(description=dedent(f"""
        Evaluate the quality of the human conversation based on the following criteria:
      """),
      agent=agent,
      expected_output= "A bullet list summary of the top 5 most important analytics",
    )
  def conversation_context_task(self, agent, human_conversation, chatbot_conversation):
    return Task(
    description=f'Evaluate the quality of the conversation between a chatbot and a human based on the following criteria:\n{evaluation_criteria}',
    expected_output='A detailed evaluation report based on the criteria',
    agent=agent,
    context=[human_conversation, chatbot_conversation]
)
