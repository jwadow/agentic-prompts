---
description: "Create a sub-task agent for research (@jwadow)"
---

***Create a sub-task tool in "ask" mode, meaning you create an agent within yourself.***

Give it the MAXIMUM context you know, give it the MAXIMUM information.
It will just conduct an analysis and give you a summary, but it won't see our dialogue, so you need to give it AS MUCH information as possible.
The agent takes everything literally; it cannot read your mind. The more detailed you describe the task, the better it will understand it.
Its only task is to read files and provide an analysis.

*Template for the system_prompt you will pass to it:*
```
**Objective:**
**Problem Context:**
**Problem History and Previous Attempts:**
**Current State:**
**File(s) for mandatory review:** (in the format `main.py` or `plugins\example\main.py`)
**Key questions for investigation:**

**STRICT EXECUTION INSTRUCTIONS:**
(Do not edit, but you can add new points if you wish, for example about imports, or strictly performing certain things, or a list of files for mandatory reading)
1. DO NOT edit the project files under any circumstances; your only task is to perform a thorough analysis.
2. You are allowed to read as many files as you want at once.
3. You can create and edit your to-do plan, but refrain from an initial plan of 3-4 points. You don't need many mental points, as your thoughts will be presented at the very end. A good example is when you have read the files, that was enough for you, and you immediately provide the final block, instead of constant short "Point passed and marked, moving on."

(Optional for test analysis, add it yourself if the agent should analyze tests)
4.  Before starting the test analysis, study the following files to understand the style and structure of existing tests:
    *   `ARCHITECTURE.md`
    *   `README.md`
    *   `tests/main.py`
    *   `tests/conftest.py`
    *   `tests/utils.py`
    (Below you need to pass one of the two to the agent based on the context)
    *   STRICTLY all files in `tests/integration/` (for integration tests)
    *   STRICTLY all files in `tests/unit/*` (for unit tests, don't forget to specify all folders in the `unit` folder like `tests\unit\core`, `tests\unit\db`, `tests\unit\plugins`)
5. Also, study the necessary files from the actual bot that need to be read for test analysis, so as not to make mistakes with variables, parameters, functions, and so on.

**STRICT TASK COMPLETION INSTRUCTIONS:**
(Do not edit)
When you finish the analysis, do not ask questions, but use the `attempt_completion` tool.
Inside the `<result>` block, you **MUST** provide **ONLY** the full final report. Nothing but your final report will be visible to anyone; your main task is to form a detailed final report.
```

*Note for you*
Also, carefully analyze out loud what the agent gives you in the output each time, as the agent can also make a mistake or even lie.
Because it will provide a lot of information in the output, you must assess whether it has thought everything through correctly, whether there are any errors, simplifications, or omissions.
There is no shame in seeing an agent's mistake and creating a new one. Quality code without errors is much more profitable than trying to play on the user's inattention.
Do not shorten the system_prompt anywhere unless it is specified for you, for example, the part with tests. You can add new items. But do not delete or shorten the existing ones.
IMPORTANT: ALWAYS ASK ME BEFORE CREATING AGENTS IN THE FUTURE. FOR NOW, CREATE THEM WITHOUT QUESTION.
ALWAYS CREATE SUBTASK IN USER'S LANGUAGE (e.g., English, Russian, Chinese), THIS TEXT IS AN ENGLISH COPYPASTE!