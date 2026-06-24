# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
   (for example: "the hints were backwards").
  - when I guessed 70 it told me to go higher instead of lower.
    (69 was the answer)
  - when I guessed 68 it told me to go lower instead of higher (69 was the answer)
  - New game button does nothing
  - attempts left in the beginning of the game 7
  - attempts left 1 but the game exists with "Out of attempts! The secret was 42. Score: -5"

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior                                 | Console Output / Error                          |
| ----- | ----------------- | ----------------------------------------------- | ----------------------------------------------- |
| 70    | Go Lower          | Go Higher                                       | Go Higher                                       |
| 68    | Go Higher         | Go Lower                                        | Go Lower                                        |
| 43    | 1 attempt left    | "Out of attempts! The secret was 42. Score: -5" | "Out of attempts! The secret was 42. Score: -5" |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude Sonnet
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI suggested exchange of phrases for "Go Lower and Go Higher". This fixed the first bug. Created tests using AI to confirm fix. I tested the code by running it and playing the game again. The bug was fixed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  None

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  Pytest, Debuging, Runing the project
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  The test_guess_too_low test checked the behaviour when the guess is lower than the secret. The Hint was correct after fix.
- Did AI help you design or understand any tests? How?
  I asked AI to explain the tests and it was easier to understand.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns the entire script from top to bottom every time the user interacts with the app (like clicking a button or changing input). Because of this, normal variables don’t persist. However, Streamlit uses session_state to store values that need to survive across reruns, so the app can remember previous user inputs and states.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  Prompt Strategy
- What is one thing you would do differently next time you work with AI on a coding task?
  I would have more test to include all kinds of edge cases.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI is good at scaning and implementing the target changes.
