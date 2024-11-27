# tools/tools.py
from langchain.tools import tool
from services.notion_services import NotionService
from services.github_services import GitHubService

class Tools:
    def __init__(self):
        self.notion_service = NotionService()
        self.github_service = GitHubService()

    @tool("Add data to notion")
    def add_to_notion(self, output, page_id):
        """Used to add data given as input in notion document."""
        return self.notion_service.append_review(
            page_id=page_id,
            file_path=output[1],
            review=output[2],
            updated_code=output[3]
        )

    @tool("get file contents from given file path")
    def get_file_contents(self, path, owner, repo):
        """Used to get the content of given file using GitHub API."""
        return self.github_service.get_file_content(owner, repo, path)
