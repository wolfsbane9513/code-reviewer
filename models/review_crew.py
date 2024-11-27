# models/review_crew.py
from crewai import Crew
from agents.agents import Agents
from tasks.tasks import Tasks

class ReviewCrew:
    def __init__(self, owner, repo, page_id, path):
        self.owner = owner
        self.repo = repo
        self.page_id = page_id
        self.path = path
        
    def run(self):
        # Initialize agents
        review_agent = Agents.review_agent()
        content_agent = Agents.content_agent()
        notion_agent = Agents.notion_agent()
        
        # Create tasks
        tasks = Tasks(self.owner, self.repo, self.path)
        content_task = tasks.get_file_content_task(content_agent)
        review_task = tasks.review_task(review_agent, [content_task])
        notion_task = tasks.notion_task(notion_agent, self.page_id, [review_task])
        
        # Create and run crew
        crew = Crew(
            agents=[content_agent, review_agent, notion_agent],
            tasks=[content_task, review_task, notion_task],
            verbose=2,
        )
        
        return crew.kickoff()