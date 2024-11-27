# Code Review Agent 🤖

An automated code review system powered by AI agents that analyzes GitHub repositories and stores reviews in Notion documents. The system uses GPT-4 to provide detailed code reviews based on industry standards.

## 🌟 Features

- **Automated Code Reviews**: AI-powered analysis of code quality and standards
- **Flexible Review Scope**: Review individual files or entire directories
- **GitHub Integration**: Seamless access to repositories (public and private)
- **Notion Documentation**: Automatic storage of reviews in organized Notion pages
- **Smart Filtering**: Automatic handling of large files (>1MB) and lengthy code (>500 lines)
- **Modular Architecture**: Well-organized, maintainable codebase
- **Configurable**: Easy to customize review criteria and settings

## 🏗 Project Structure

```
src/
├── config/
│   └── config.py          # Configuration settings and environment variables
├── agents/
│   └── agents.py          # AI agent definitions and behaviors
├── tasks/
│   └── tasks.py           # Task definitions for agents
├── tools/
│   └── tools.py           # Implementation of agent tools
├── services/
│   ├── github_service.py  # GitHub API interactions
│   └── notion_service.py  # Notion API interactions
├── models/
│   └── review_crew.py     # Core review logic
└── main.py                # Application entry point
```

## 📋 Prerequisites

1. **Python Environment**: Python 3.8 or higher
2. **API Keys**:
   - OpenAI API Key (for GPT-4)
   - GitHub Personal Access Token
   - Notion API Integration Key

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/code-review-agent.git
cd code-review-agent
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_key
GITHUB_KEY=your_github_pat
NOTION_KEY=your_notion_key
```

## ⚙️ Configuration

Edit `config/config.py` to customize:
- Maximum file size limits
- Line count thresholds
- Directories to ignore
- Notion page templates
- Other review parameters

## 💻 Usage

1. Run the application:
```bash
python src/main.py
```

2. Enter requested information:
   - GitHub repository URL
   - File or directory to review

3. View results in your configured Notion page

## 📝 Example Output

The review will be stored in Notion with the following structure:

- 🚀 **File Name**
  - Path to the reviewed file
- 📝 **Review**
  - Detailed code review feedback
  - Suggestions for improvements
  - Best practices recommendations
- 💡 **Updated Code**
  - Improved version of the code with suggested changes

## 🔧 Development

### Adding New Features

1. **New Agents**: Add new agent classes in `agents/agents.py`
2. **Custom Tools**: Implement new tools in `tools/tools.py`
3. **Additional Tasks**: Define new tasks in `tasks/tasks.py`

### Running Tests

```bash
python -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

Common issues and solutions:

1. **API Rate Limits**:
   - Use authenticated requests
   - Implement rate limiting in your code

2. **Large Repositories**:
   - Adjust file size limits in config
   - Use selective directory scanning

3. **Notion Integration**:
   - Verify page permissions
   - Check integration token scope

## 📚 Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [GitHub API Documentation](https://docs.github.com/rest)
- [Notion API Documentation](https://developers.notion.com/)
- [CrewAI Documentation](https://crewai.readthedocs.io/)

## 📞 Support

- Create an issue in the repository
- Reach out to the maintainers
- Check the [Wiki](wiki) for detailed guides

---
Made with ❤️ by [Your Name/Organization]