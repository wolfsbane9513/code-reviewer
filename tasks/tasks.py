from crewai import Task
from config.config import Config

class Tasks:
    def __init__(self, owner, repo, path):
        """
        Initialize Tasks with repository information.
        
        Args:
            owner (str): GitHub repository owner
            repo (str): Repository name
            path (str): File path to review
        """
        self.owner = owner
        self.repo = repo
        self.path = path

    def review_task(self, agent, context):
        """
        Creates a task for reviewing code.
        
        Args:
            agent: The agent responsible for code review
            context: Additional context or previous task results
        """
        return Task(
            agent=agent,
            description=f"""
                Review the given file and provide detailed feedback and reviews about the file if it doesn't follow the industry code standards
                Take the file path and file contents from contentAgent
                Make changes in file content to make it better and return the changed content as updated_code in response
                Return the below values in response
                project_name: {self.repo}
                file_path: file path
                review: review_here
                updated_code: updated content of file after making changes

                Return the output which follows the below array structure and every element must be wrapped in multi-line string
                In case of updated_code, add the full code as a multi-line string
                Only return file content which got changed in updated_code, if there are multiple changes in file content then send whole file content

                Every array should follow this format:
                [project_name,file_path,review,updated_code]

                Don't return anything except array in above format
            """,
            context=context,
            expected_output="An array of 4 elements in a format given in description"
        )

    def notion_task(self, agent, page_id, context):
        """
        Creates a task for adding review data to Notion.
        
        Args:
            agent: The agent responsible for Notion operations
            page_id: The Notion page ID where content will be added
            context: Previous task results to be added to Notion
        """
        return Task(
            agent=agent,
            description=f"""
                You are given an array of 4 elements and a page id and you will have to add this data in notion
                Here is the id of notion page
                {page_id}
                Say 'Data is added successfully into notion' in case of success else return given array.
            """,
            context=context,
            expected_output="Text saying 'Data is added successfully into notion' in case of success and 'Could not add data in notion' in case of failure"
        )

    def get_file_path_task(self, agent, filetree, user_input):
        """
        Creates a task for extracting file paths from the repository structure.
        
        Args:
            agent: The agent responsible for path extraction
            filetree: Repository folder structure
            user_input: User-specified file or folder to review
        """
        return Task(
            agent=agent,
            description=f"""
                You are given a tree structure of folder and userInput and first you have to decide whether it is a folder or file from given tree structure of a folder
                Follow this approach
                - If it's a file then return array with 1 element which contains the full path of that file in this folder structure
                - If it's a folder then return array of paths of sub files inside that folder, if there is a subfolder in given folder, then return paths for those files as well
                - If userInput is not present in given tree structure then just return empty array
                Please return FULL path of a given file in given folder tree structure
                For example if tree structure looks like this:
                - src
                  - components
                    - Login.jsx
                    - Password.jsx
                - backend
                  - api
                Then the full path of Login.jsx will be src/components/Login.jsx
                DON'T send every file content at once, send it one by one to reviewAgent
                here is the tree structure of folder:
                {filetree}
                here is user input
                {user_input}

                NOTE: ONLY RETURN ARRAY OF PATHS WITHOUT ANY EXTRA TEXT IN RESPONSE
            """,
            expected_output="""
                ONLY an array of paths
                For example:
                ['src/load/app.jsx','client/app/pages/404.js']
            """
        )

    def get_file_content_task(self, agent):
        """
        Creates a task for retrieving file content from GitHub.
        
        Args:
            agent: The agent responsible for fetching file content
        """
        return Task(
            agent=agent,
            description=f"""
                You are given a file path and you have to get the content of file and file name using github API
                here is the file path
                {self.path}
                here is owner name
                {self.owner}
                here is repo name
                {self.repo}
                Don't return anything except filename and content
            """,
            expected_output="filename and content of given file"
        )

    @staticmethod
    def validate_file_size(content):
        """
        Validates if file size is within acceptable limits.
        
        Args:
            content (str): File content to validate
        Returns:
            bool: True if file is within size limits, False otherwise
        """
        return len(content.encode('utf-8')) <= Config.MAX_FILE_SIZE

    @staticmethod
    def validate_line_count(content):
        """
        Validates if file line count is within acceptable limits.
        
        Args:
            content (str): File content to validate
        Returns:
            bool: True if file is within line limits, False otherwise
        """
        return len(content.split('\n')) <= Config.MAX_LINES