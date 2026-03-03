from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client

model_client = get_model_client()

def get_problem_solver_agent():
    """
    Function to get the problem solver agent.
    This agent is responsible for solving DSA problems.
    It will work with the code executor agent to execute the code.
    """

    problem_solver_agent = AssistantAgent(
            name = "dsa_problem_solver",
            description = "An agent that solves DSA problem.",
            model_client = model_client,
            system_message = """
            You are a overall problem solver agent that is an expert in solving DSA problems.
            You will be working with code executor agent to execute code.
            You will be given a task and you should.
            1. Write code to solve the task. Your code shall be only in Python.
            At the beginning of your response you have to specify your plan to solve the task.
            Then you should give the code in a code block (Python).
            You should write code in a single or one code block at a time and pass it to code executor agent to execute it.
            Make sure that we have atleast 3 test cases for the code you write.
            Once the code is executed and if the same is done successfully, you have the results.
            You should explain the code execution result.

            Once the code and explanation is done, you should ask the code executor agent to save the code in a file.
            like this:
             ```python
                code = '''
                    print("Hello World")
                    '''
                with open('solution.py', 'w') as f:
                    f.write(code)
                    print("Code saved successfully in solution.py")
            ```
            You should send the above code block to the code executor agent so that it can save the code in a file. Save it in a file and name the file as 'solution.py'. Make sure to provide the code in a code block.

            In the end once the code is executed successfully, you have to say "STOP" to stop the conversation.
            """
        )
    
    return problem_solver_agent
