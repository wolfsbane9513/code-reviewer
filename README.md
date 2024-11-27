# Code Review Agent 🤖

An automated code review system that analyzes GitHub repositories and stores reviews in Notion documents using AI-powered agents.

## Features

- Automated code review for individual files or entire directories
- Integration with GitHub API for repository access
- Automatic storage of reviews in Notion
- Smart file filtering (skips files >1MB or >500 lines)
- Customizable review criteria based on industry standards
- Support for private repositories

## Prerequisites

Before you begin, ensure you have the following API keys:

- **OpenAI API Key**: Used for GPT-4 powered code review
- **GitHub Personal Access Token**: Required for repository access (especially private repos)
- **Notion API Key**: For storing review results
  - Create an integration at Notion
  - Connect it to your target document via the share menu

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install crewai
pip install requests
pip install crewai-tools
pip install notion_client
```

3. Set up your environment variables:
```bash
export OPENAI_API_KEY='your-openai-key'
export GITHUB_KEY='your-github-pat'
export NOTION_KEY='your-notion-key'
```

## Usage

1. Run the script:
```bash
python codereviewagent.py
```

2. When prompted:
   - Enter the GitHub repository URL
   - Specify the file or folder name you want to review

The agent will:
1. Analyze the repository structure
2. Review specified files
3. Create a Notion page with detailed reviews
4. Store both the review feedback and suggested improvements

## System Architecture

The system consists of four specialized agents:

1. **Review Agent**: Senior software developer role that performs code reviews
2. **Notion Agent**: Handles documentation in Notion
3. **Content Agent**: Manages GitHub API interactions
4. **Path Agent**: Handles file path extraction and navigation

## Limitations

- Maximum file size: 1MB
- Maximum lines of code per file: 500
- Ignores certain directories by default: `public`, `images`, `media`, `assets`

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## License

[Add your license information here]

## Support

For support:
1. Open an issue in the repository
2. Provide detailed information about your problem
3. Include relevant error messages and logs
