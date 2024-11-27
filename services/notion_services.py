# services/notion_service.py
from notion_client import Client
from config.config import Config

class NotionService:
    def __init__(self):
        self.client = Client(auth=Config.NOTION_KEY)
    
    def create_page(self, project_name):
        parent = {
            "type": "page_id",
            "page_id": Config.NOTION_PAGE_ID
        }
        properties = {
            "title": {
                "type": "title",
                "title": [{"type": "text", "text": {"content": f"Code review of {project_name}"}}]
            },
        }
        response = self.client.pages.create(parent=parent, properties=properties)
        return response['id']

    def append_review(self, page_id, file_path, review, updated_code):
        children = [
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "🚀 File Name"}}]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": file_path}}]
                }
            },
            # ... rest of the blocks
        ]
        return self.client.blocks.children.append(block_id=page_id, children=children)