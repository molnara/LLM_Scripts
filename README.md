# LLM Python Scripts

Testing local LLMs using [Ollama](https://github.com/ollama/ollama) via Docker container using the [LangChain](https://python.langchain.com/) framework library and using the [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) model.

## Scripts:

### rag_webbase.py
Demonstrates RAG (Retrieval-Augmented Generation) which uses a [blog post](https://lilianweng.github.io/posts/2023-06-23-agent/) by Lilian Weng on agents as an example.

**Question:**

What are the approaches to Task Decomposition?

**Answer:**

The summary outlines three core themes related to task decomposition using an LLM-powered autonomous agent system:

1. **Task Decomposition via LLMs**: The use of large language models (LLMs) with specific instructions or prompting to break down tasks into manageable steps or subgoals, such as generating prompts for outlining processes like writing a story.

2. **Autonomous Agent Planning and Memory Utilization**: Autonomous agents employ planning mechanisms and memory to efficiently handle complex tasks by decomposing them into smaller subtasks, enabling better organization and execution of multi-step processes.

3. **Reflective Learning in Autonomous Systems**: Incorporation of reflective processes within autonomous systems allows agents to critically evaluate past actions, learn from mistakes, and refine future strategies, enhancing overall performance and outcome quality.

### Requirements

- Docker for Windows
- Windows Subsystem for Linux (WSL) if you are using a GPU
- VS Code

### Setup

- Clone repo and open folder in VS Code.
- Right click the Dockerfile in the Docker folder and Build Image...
- Run container setting a volume pointing to Scripts directory for developing/testing scripts
`docker run -d --gpus=all -v ollama:/root/.ollama -v "%userprofile%\Documents\GitHub\LLM_Scripts\Scripts":/Scripts -p 11434:11434 --name llmscripts-main llmscripts:latest`
- Pull models, these get stored in the containers volume
`docker exec -it llmscripts-main ollama pull nomic-embed-text`
`docker exec -it llmscripts-main ollama pull deepseek-r1`
- Now you can use bash to execute python scripts, located in /Scripts folder
`docker exec -it llmscripts-main bash`
`root@32daf2b4f53a:/Scripts# python3 rag_webbase.py`

### Resources
- [Build a Local RAG Application](https://python.langchain.com/v0.2/docs/tutorials/local_rag/)