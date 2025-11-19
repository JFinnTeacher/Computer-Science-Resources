# 💻 Challenge Worksheet  
## Project: Math Quiz Tournament  

---

### Project Brief  
You will design a **Math Quiz Tournament** in Python.  

- The **user chooses** how many questions to try.  
- For each question:  
  - A math question is shown.  
  - The user must keep guessing until they are correct.  
  - If the user types **0**, that question ends immediately.  
- At the end of the quiz, the program should show how many questions were answered correctly.  

---

### Starter Scaffold Code (fill in the blanks)  

```python
print("Welcome to the Math Quiz Tournament")

# Step 1: Ask how many questions
rounds = int(input("How many questions would you like to try? "))

score = 0

# Step 2: For loop to go through each question
for i in range(rounds):
    print("Question number " + str(i+1))
    
    # TODO: Write a maths question here (e.g. 3 + 4)
    # TODO: Set the correct_answer variable

    answer = -1
    
    # Step 3: While loop for repeated guesses
    while answer != correct_answer:
        answer = int(input("Your answer (or 0 to quit): "))
        
        # Step 4: Decisions with if / elif / else
        if answer == correct_answer:
            print("Correct!")
            score = score + 1
        elif answer == 0:
            print("Exiting this question")
            break
        else:
            print("Try again")

# Step 5: Summary
print("Tournament over")
print("Total questions: " + str(rounds))
print("Correct answers: " + str(score))
```

---

### ✅ Success Criteria  
- Uses a **for loop** to run multiple questions.  
- Uses a **while loop** so the user repeats until correct.  
- Uses **if / elif / else** to handle correct, incorrect, and quit.  
- Prints a **summary** of results at the end.  

---

### Reflection Questions  
1. What part of the program uses a **for loop**, and why?  
2. Why do we need a **while loop** for each question?  
3. How does the **if / elif / else** give meaningful feedback?  
4. If the user types `0` but there was no `elif answer == 0`, what would happen?  

---

## ✅ Marking Rubric (24 Marks)

| Criteria           | Excellent (4)                          | Good (3)                   | Satisfactory (2)           | Needs Improvement (1) |
| ------------------ | -------------------------------------- | -------------------------- | -------------------------- | --------------------- |
| **For Loop**       | Correctly controls number of questions | Mostly correct             | Attempted but flawed       | Absent                |
| **While Loop**     | Fully repeats until answer is correct  | Works with small issues    | Attempted but partly wrong | Missing               |
| **If/Elif/Else**   | Clear feedback for all cases           | Most cases handled         | Basic or limited feedback  | Very limited/none     |
| **Summary Output** | Complete and accurate                  | Includes most details      | Partially shown            | Missing               |
| **Code Clarity**   | Clear, indented, easy to follow        | Mostly clear readable code | Understandable but messy   | Very messy/unreadable |
| **Reflection**     | Complete thoughtful answers            | Mostly correct answers     | Partial answers given      | Little/no effort      |

**Total: /24**

---

### ⚡ Extensions  
- Add extra questions (subtraction, multiplication).  
- Count how many **attempts** it takes per question.  
- Give extra points for correct **on the first try**.