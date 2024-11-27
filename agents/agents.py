# agents/agents.py
from crewai import Agent
from tools.tools import Tools

class Agents:
    @staticmethod
    def review_agent():
        return Agent(
            role='Senior software developer',
            goal='Do code reviews on a given file to check if it matches industry code standards',
            backstory="You're a Senior software developer at a big company and you need to do a code review on a given file content.",
            allow_delegation=False,
            verbose=True,
        )

    @staticmethod
    def notion_agent():
        tools = Tools()
        return Agent(
            role="Notion api expert and content writer",
            goal="Add given array data into notion document using addToNotion tool",
            backstory="You're a notion api expert who can use addToNotion tool and add given data into notion document",
            allow_delegation=True,
            tools=[tools.add_to_notion],
            verbose=True,
        )

    # ... other agents
