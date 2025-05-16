# Shopping Assistant - GitHub Copilot Agent Experiment
## Project Approach 

This is an experiment project to test the capabilities of GitHub Copilot Agent. This is to show case how software development can be done quicker and with less pain with the GitHub Copilot. Refer to [Software Engineering in the Era of AI](./docs/extras/sw_in_ai_era.md) for a glimpse on what will happen in next 5 years, starting today. 

I am trying to see how much I can get out of the **GitHub Copilot Agent mode.** I'd like to document the prompt process, **from an initial big idea, to architecture design, to scaffolding code, and then to completed code modules and eventually, an working application with testing code.** This process will take some trial and error and prompts refinement. I hope to be surprised and satisfied in the end. If this process works, we could use it for our future Projects. 

All the prompts and results will be posted to **docs/prompts** folder. 

The generated code is in the folder **src**. The **frontend** subfolder has code for the web interface built with **React**. The subfolder backend has code for the AI application constructed with Python **`FastAPI`**, `Semantic Kernel`, `PostgreSQL DB`, and `Azure AI services`.

You are welcome to work with me on this project by clone this repo and make your branch. I created **docs/project_team_discussions** where you can upload your ideas and your prompts. 

## Solution Architecture 

The initial solution architecture is illustrated below. This was the key design used to create various prompts for GitHub Copilot to complete the tasks. There are many interactions with the GitHub Copilot. ![Solution Architecture](./docs/images/architecture.png)

## Current Status (Completed Work)

This is a side project beyond my full time job. I will get back to do more on this project when I get some spare time.

#### Completed Tasks with Results Documented: 

- **Prompt Engineering (PE) 1**: [Capabilities](./docs/prompts/P1-Shopping-Assistant-Capabilities.md)
- **PE 2**: [Architecture Design](./docs/prompts/P2-Architecture-Design.md)
- **PE 2A**: [Architecture Design Discussions](./docs/prompts/P2A-Architecture-Design-Discussions.md)
- **PE Extra - Features**: [User Scenarios](./docs/prompts/User_Scenarios.md)
- **PE Extra - Security**: [Security Features](./docs/prompts/Security_Tokens.md)
- **PE 3**: [Project Folder Structure](./docs/prompts/P3-Project-Code-Structure.md)
- **PE 4**: [Scaffolding Code](./docs/prompts/P4-Scaffolding-Code.md)
- **PE Code Generation - Frontend**: [Frontend Web App Code Generated and Tested (stubbed backend)](./src/frontend)
- **Author's Task**: Create this main README.md with Initial Architecture Diagram. I still like this task. But I think this can be done by AI pretty soon. 

