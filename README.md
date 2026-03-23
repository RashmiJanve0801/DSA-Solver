# DSA Solver — Multi-Agent Code Generation & Execution

The question that started this: can two AI agents actually solve a 
coding problem end-to-end — not just write code, but run it, 
validate it against test cases, and only save it when it passes?

Turns out yes. ~70% pass rate on the first attempt. 
The rest get there after a retry loop. Not bad.

## How it works

Two agents. One job each.

**Agent 1 — Problem Solver**
Takes the problem description, reasons through the approach, 
writes a Python solution and test cases. Uses Gemini 2.5 Flash 
for the reasoning and code generation.

**Agent 2 — Code Executor**
Receives the solution, runs it inside an isolated Docker container 
(nothing executes on your host machine), checks test results.

If tests fail → sends failure details back to Agent 1 → it fixes and retries.
If tests pass → solution gets written to a file in `/solutions`.

AutoGen's `RoundRobinGroupChat` coordinates the turn-taking between agents.
Clean separation of concerns — the solver doesn't execute, 
the executor doesn't write code.


## Tech Stack

| Layer | Technologies |
|---|---|
| Agent Orchestration | Microsoft AutoGen (RoundRobinGroupChat) |
| LLM | Google Gemini 2.5 Flash |
| Code Execution | Docker (sandboxed containers) |
| Frontend | Streamlit, CLI (argparse) |
| Infra | Docker |

