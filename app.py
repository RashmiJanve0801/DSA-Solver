import asyncio
import streamlit as st

from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

from teams.dsa_team import get_dsa_team_docker
from config.docker_utils import start_docker_container, stop_docker_container

st.title("AlgoGenie - Our DSA Problem Solver")
st.write("Welcome to AlgoGenie, your personal DSA problem solver! Here you can ask solutions to various data structures and algorithms problems.")

task = st.text_input("Enter your DSA problem or question:", value="Write a function to add two numbers")

async def run(dsa_team, docker, task):
    try:
        await start_docker_container(docker)
        
        async for message in dsa_team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg:=f"{message.source} : {message.content}")
            elif isinstance(message, TaskResult):
                print(msg:=f"'Stop Reason:'{message.stop_reason}")
            
            yield msg

        print("Task Completed")
    except Exception as e:
        print(f"Error:{e}")
        yield f"Error: {e}"
    finally:
        await stop_docker_container(docker)

if st.button("Run"):
    st.write("Running the Task..")
   
    dsa_team, docker = get_dsa_team_docker()

    async def collect_messages():
        async for msg in run(dsa_team, docker, task):
            if isinstance(msg, str):
                if msg.startswith("user"):
                    with st.chat_message('user', avatar='👤'):
                        st.markdown(msg)
                elif msg.startswith("dsa_problem_solver"):
                    with st.chat_message('assistant', avatar='🧑‍💻'):
                        st.markdown(msg)
                elif msg.startswith("code_executor"):
                    with st.chat_message('assistant', avatar='🤖'):
                        st.markdown(msg)
            elif isinstance(msg, TaskResult):
                with st.chat_message('stopper',avatar='🚫'):
                    st.markdown(f"Task Completed: {msg.result}")

    asyncio.run(collect_messages())

