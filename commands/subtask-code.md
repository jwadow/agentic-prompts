---
description: "Create a sub-task agent for writing code (@jwadow)"
---

***Create a sub-task tool FOR EACH ITEM, meaning you create an agent within yourself.***

Give it the MAXIMUM context you know, give it the MAXIMUM information.
It will just make the edits, but it won't see our dialogue, so you need to give it AS MUCH information as possible.
The agent takes everything literally; it cannot read your mind. The more detailed you describe the task, the better it will understand it.
Its only task is to edit and describe what it has done.

*One agent - one file. Do not ask two agents to edit the same file.*
Bad example:
1) 1 agent to create a file with a class and functions inside but left with pass
2) 2 agent that adds functionality instead of pass in each function
Good example:
1) 1 agent immediately creates a file with everything necessary

*With a detailed plan, you should not ask the agent to edit 1-2 lines in a file and that's it. It is better to delegate all micro-edits to one agent.*
Bad example:
1) 1 agent adds one line to file X
2) 2 agent edits 2 lines in file Y
3) 3 agent deletes a function in file Z
Good example:
1) 1 agent, having a detailed plan, immediately edits many small changes in different files

*Template for the system_prompt you will pass to it:*
```
**Objective:**
**Problem Context:**
**File(s) for modification:** (in the format `main.py` or `plugins\example\main.py`)
**Required fix:**
**Specific implementation steps:**

**STRICT EXECUTION INSTRUCTIONS:**
(DO NOT EDIT OR CHANGE. but you can add new points if you wish, for example about imports, or strictly performing certain things, or a list of files for mandatory reading)
1. If you need to study several files at once, this is not forbidden. BUT before each edit, read the file from scratch, so the diff will be applied better. Do not forget about correct tabulation and do not allow repetitions of adjacent lines. Most diff errors are when you edit the tabulation, but did not capture the area next to it, and as a result, did not fix the tabulation of adjacent elements belonging to the same block of code.
2. If required, do not forget to write debugs in Russian, and write comments in Russian.
3. Write descriptions for created functions and comments for code blocks.
4. But do not add a comment at the end of a line of code, signaling only that you added this line. Bad example: `import time # Add import for functionality"`. Good example: `import time`.
5. Never pass arguments to a function without specifying the parameter name. Bad example: `example_func(1234)`. Good example: `example_func(delay=1234)`.

(FOR TESTS, add ALL POINTS yourself if the agent should WRITE NEW or EDIT EXISTING tests)
6.  Before you start writing a test, study the following files to understand the style and structure of existing tests:
    *   `ARCHITECTURE.md`
    *   `README.md`
    *   `tests/main.py`
    *   `tests/conftest.py`
    *   `tests/utils.py`
    (Below you need to pass one of the two to the agent based on the context, IF THIS IS CREATING OR REFACTORING AN EXISTING TEST. If it is editing 1-2 lines, then skip these 2 points)
    *   STRICTLY all files in `tests/integration/` (for integration tests)
    *   STRICTLY all files in `tests/unit/*` (for unit tests, do not forget to specify all folders in the `unit` folder like `tests\unit\core`, `tests\unit\db`, `tests\unit\plugins`)
7. Also, study the necessary files from the actual bot that need to be read to create a test, so as not to make mistakes with variables, parameters, functions, and so on.
8. DO NOT edit the project files under any circumstances; your only task is to write tests.
9. Follow the style of existing tests in the project. Add print() to output information about the test progress, as well as to compare expected and received results.
10. Each test file must be written at once, not many edits for each test.

**STRICT TASK COMPLETION INSTRUCTIONS:**
(DO NOT EDIT)
When you finish making edits, do not ask questions, but use the `attempt_completion` tool.
Inside the `<result>` block, you **MUST** provide **ONLY** the following, and in this exact order:
1.  The full `diff` of the changes made (with + and -). Do not use the `git diff` command.
2.  Detailed notes on the changes, describing what exactly was done in each changed line.
**DO NOT** add any explanations, conclusions, or greetings before or after these two points in the `<result>` block. Your task is only to make edits and report on them in the specified format. If there were no changes in any point, or no changes at all, this ALSO needs to be reported in the specified format with detailed information.
The `<result>` should not consist of 1-2 sentences. But without fanaticism, BAD EXAMPLE: when you edited 5 lines, and the detailed note is stretched to 30 lines with an explanation of each line.
3. Format: "`diff` for `file1.ext` \n {diff} \n `diff` for `file2.ext` \n {diff} \n Notes on changes: \n {as in point 2}"
```

*Note for you*
Also, carefully analyze out loud what the agent gives you in the output each time, as the agent can also make a mistake or even lie. Even a tabulation error can slip through.
Because it will provide a lot of information in the output, you must assess whether it has done everything correctly, whether there are any errors, simplifications, or omissions.
There is no shame in seeing an agent's mistake and creating a new one. Quality code without errors is much more profitable than trying to play on the user's inattention.
Do not take the agent's words about the finality of the decision on faith.
IMPORTANT: ALWAYS ASK ME BEFORE CREATING AGENTS.
ALWAYS USE MY LANGUAGE, THIS TEXT IS A COPYPASTE!