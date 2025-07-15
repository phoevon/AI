Creacion de agentes IA de forma sencilla con interfaz web de los agentes. Creado con Flask y python, lo creamos en entorno virtual, virtual env. 
El principio usado es el de una clase o constructor y tratamos a los agentes como objetos, de esta forma podemos crear infinitos agentes que ademas tienen conocimiento de lo hablado con otros agentes a traves del archivo json.
Se pueden añadir diferentes mejoras como que puedan interaccionar unos con otros.
Usamos Gemini pero se podria usar en local con Ollama y cualquier modelo dependiendo de nuestra GPU.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧠 Simple Creation of AI Agents with Web Interface
This project enables the easy creation of AI agents through a web-based interface.
Built using Flask and Python, it runs inside a virtual environment (virtualenv) for better isolation and dependency management.

🔧 Core Concepts
Object-Oriented Design:
Agents are treated as objects instantiated from a class or constructor. This approach allows the creation of unlimited agents, each with its own memory and state.

Shared Knowledge:
Agents can access and retain conversation history via a shared JSON file, enabling them to be aware of interactions with other agents.

🚀 Features
Simple web UI for interacting with agents

Persistent memory using JSON

Scalable agent creation

Room for future improvements, such as agent-to-agent interaction

🧩 Flexibility
By default, the system uses Gemini (via API or integration)

It can also run locally with Ollama and any compatible model, depending on your GPU capabilities
