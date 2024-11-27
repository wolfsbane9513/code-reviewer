from services.github_service import GitHubService
from services.notion_service import NotionService
from models.review_crew import ReviewCrew
from agents.agents import Agents
from tasks.tasks import Tasks
import ast

def main():
    # Get user input
    github_url = input("Provide github repo URL: ")
    user_input = input("Provide file/folder name you want to review: ")
    
    # Parse GitHub URL
    split_url = github_url.split('/')
    owner, repo = split_url[3], split_url[4]
    
    # Initialize services
    github_service = GitHubService()
    notion_service = NotionService()
    
    # Get repository structure
    file_tree = github_service.get_file_tree(owner, repo)
    
    # Get file paths
    path_agent = Agents.path_agent()
    path_task = Tasks.get_file_path_task(path_agent, file_tree, user_input)
    paths = ast.literal_eval(path_task.execute())
    
    # Create Notion page
    page_id = notion_service.create_page(repo)
    
    # Review each file
    for path in paths:
        review_crew = ReviewCrew(owner, repo, page_id, path)
        review_crew.run()

if __name__ == "__main__":
    main()