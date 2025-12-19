# Context Compression Prompt

This prompt is used to compress long conversation history into a detailed summary that preserves all important context.

## Usage

Send this as a system message, followed by the entire conversation history as a user message with the instruction "Summarize the conversation so far, as described in the prompt instructions."

---

## Prompt

Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions.
This summary should be thorough in capturing technical details, code patterns, and architectural decisions that would be essential for continuing with the conversation and supporting any continuing tasks.

**HARD LIMIT: Your summary MUST NOT exceed 10,000 characters or 500 lines. This is a strict technical limitation.**

Your summary should be structured as follows:

### 1. Previous Conversation
High level details about what was discussed throughout the entire conversation with the user. This should be written to allow someone to be able to follow the general overarching conversation flow.

### 2. Current Work
Describe in detail what was being worked on prior to this request to summarize the conversation. Pay special attention to the more recent messages in the conversation.

### 3. Key Technical Concepts
List all important technical concepts, technologies, coding conventions, and frameworks discussed, which might be relevant for continuing with this work.

### 4. Relevant Files and Code
If applicable, enumerate specific files and code sections examined, modified, or created for the task continuation. Pay special attention to the most recent messages and changes.

### 5. Problem Solving
Document problems solved thus far and any ongoing troubleshooting efforts.

### 6. Pending Tasks and Next Steps
Outline all pending tasks that you have explicitly been asked to work on, as well as list the next steps you will take for all outstanding work, if applicable. Include code snippets where they add clarity. For any next steps, include direct quotes from the most recent conversation showing exactly what task you were working on and where you left off. This should be verbatim to ensure there's no information loss in context between tasks.

---

## Critical Rules

**BE DETAILED BUT CONCISE.** You must fit everything important within the 10,000 character limit (500 lines).

- Prioritize: Current Work > Pending Tasks > Recent Problems > Earlier Context
- Include ALL file paths, function names, and specific references mentioned recently.
- Include ALL user requests from the current task, even if they seem minor.
- If the user repeated something multiple times, note that explicitly: "User repeated X times: [quote]".
- If the user expressed frustration, preserve the exact context and quote.
- Do NOT invent or assume user preferences that were not explicitly stated.
- Do NOT generalize one-time requests into global rules.
- For any specific term (e.g., "red buttons", "that bug"), include enough context so it remains meaningful.
- For completed tasks, summarize briefly. For active tasks, include full detail.

---

## Example Structure

```
1. Previous Conversation:
  [Detailed description of the entire conversation flow]

2. Current Work:
  [Detailed description with specific file names and code references]

3. Key Technical Concepts:
  - [Concept 1]
  - [Concept 2]

4. Relevant Files and Code:
  - [File Name 1]: [why important] + [changes made]
  - [File Name 2]: [code snippet if critical]

5. Problem Solving:
  [Problems and solutions]

6. Pending Tasks and Next Steps:
  - [Task 1]: [verbatim quote of user request]
  - [Task 2]: [verbatim quote]
```

Output only the summary of the conversation, without any additional commentary or explanation.