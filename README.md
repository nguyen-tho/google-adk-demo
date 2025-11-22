# About project

This is a mini project to demonstrate some features about Google Agent Development Kit (Google ADK)

# How to setup agent

- Step 1: create virtual environment by using .venv

```sh
python -m venv .venv
```

- Step 2: activate virtual environment

```sh
# Linux bash shell:
source .venv/bin/activate
# Power shell
.venv/Scripts/Activate.ps1
# CMD
.venv/Scripts/activate.bat
# github bash shell
source ./.venv/Scripts/activate
```

- Step 3: install google-adk package
```sh
pip install google-adk
#Requirement: python >=3.9 to install google-adk package
```

- Step 4: create agent by google adk
```sh
adk create <your agent name>
# you need to prepare google gemini API key and write it when you initialize your agent
# when your agent was created, you have 3 files in your agent_name folder:
# - .env: environment variables file
# - _init_.py: initialized file
# - agent.py: agent code file

#for example:
adk create common_agent # my agent
```

- Step 5: run agent
```sh
# run agent with your terminal
adk run <your agent folder>

# run agent with web UI
adk web <your upper folder of your agent(s) folder>
# when you run agent with web UI on your localhost the agent API will run on port 8000
#localhost:8000 or 127.0.0.1:8000
# on web UI we have a checklist to choose your agent please choooe your agant based on your agent_name folder
```


Reference:

- Learn more with official document: [Google ADK](https://google.github.io/adk-docs/)

