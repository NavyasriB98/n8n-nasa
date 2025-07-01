Project Name
nasa apod viewer using n8n

Tech Stack
Backend: n8n (workflow automation and API backend)
Frontend: Built using VS Code (python)

set up:
I have used n8n as backend the below image shows the n8n worlflow that i used to build.
webhook node--The Webhook node in n8n acts as an entry point to your backend workflow.When you deploy your workflow in n8n, it generates a production webhook URL that you can use to trigger the workflow from your frontend or other sources.
http request node-- this node used to get the data from the given url
filter node-- u can filter the what data you want to use.
respond to  webhook-- this node sends a response back to whoever called the webhook.
![image](https://github.com/user-attachments/assets/d6c9d07d-2d20-42e9-a423-03780a7a36ea)

