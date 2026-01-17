from langchain.agents import create_agent
from Model.model import model
from Tools import LitePath, MakeFolder, Relocate
from langchain.messages import SystemMessage, HumanMessage

system_prompt = SystemMessage(content="You are an advanced file management agent.")


agent = create_agent(model, tools=[LitePath, MakeFolder, Relocate], debug=True, system_prompt=system_prompt)

def Run_Agent(query: str) -> str:
    """Runs the file management agent with the given query.

    Args:
        query (str): The user's query for file management tasks.

    Returns:
        str: The agent's response to the query.
    """
    response = agent.invoke({"messages": [HumanMessage(query)]})
    return response


# Example usage:
print(Run_Agent("manage files on my Download folder"))