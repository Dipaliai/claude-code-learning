# 🐛 Bugs to Fix

This file lists all the bugs in this project. Your job is to find and fix them!

Each bug has a **description**, **hints**, and **learning goal**. Start with Bug #1, then move to Bug #2.

---

## Bug #1: Wrong Grade Calculation 🧮

### What's the Problem?
The `calculate_average()` function in `main.py` is not calculating the average grade correctly. When you calculate the average of grades, it's giving you the wrong number.

### Where to Look
**File:** `main.py`  
**Function:** `calculate_average()`

### Hints
- 🔍 **Hint 1:** The formula for average is: (sum of all grades) ÷ (number of grades)
- 🔍 **Hint 2:** Check if the function is using the correct math operation
- 🔍 **Hint 3:** What operation should you use? Addition? Multiplication? Division?
- 🔍 **Hint 4:** Look at this line: `return total / len(grades) * 100` - Is the order correct?

### Example
```
If grades are: [80, 90, 70]
Correct average should be: 80
But the function returns: 800
```

### What You'll Learn
- How to read and understand code
- How to spot logic errors
- How to test if a function works correctly
- Basic math operations in Python

### How to Test
Run this in terminal:
```bash
python tests.py
```

If the test fails, Bug #1 is not fixed yet!

---

## Bug #2: Missing Input Validation ✅

### What's the Problem?
The `get_grades()` function in `utils.py` doesn't check if the grades are valid. It should:
- Make sure grades are between 0 and 100
- Make sure there's at least one grade
- Make sure the input is a number (not text like "abc")

Right now it just accepts ANY input, even bad ones!

### Where to Look
**File:** `utils.py`  
**Function:** `get_grades()`

### Hints
- 🔍 **Hint 1:** What should happen if someone enters a grade of 150? (That's not valid!)
- 🔍 **Hint 2:** What if someone enters 0 grades? Should that work?
- 🔍 **Hint 3:** Look for where grades are checked. Is there validation?
- 🔍 **Hint 4:** You might need to add an `if` statement to check if grades are valid

### Example
```
Bad input that should NOT be accepted:
- Grade: 150 (too high!)
- Grade: -10 (negative!)
- Grade: abc (not a number!)
- No grades at all (empty list!)
```

### What You'll Learn
- Input validation (checking if data is correct)
- Error handling (what to do when something is wrong)
- User experience (making your code friendly)

### How to Test
Run this in terminal:
```bash
python tests.py
```

If all tests pass, both bugs are fixed! ✅

---

## 🎯 Steps to Fix Bugs

1. **Read the code** - Open `main.py` and `utils.py`, understand what they do
2. **Run the tests** - Type `python tests.py` to see what fails
3. **Find the bug** - Use the hints above to locate the problem
4. **Use Claude Code** - Ask Claude Code to help fix it
5. **Test again** - Run `python tests.py` to confirm it's fixed
6. **Commit to Git** - Save your work with Git

---

## 💡 Pro Tips

✨ **Read the error messages carefully** - They tell you what's wrong!

✨ **Run `python tests.py` after EVERY fix** - This tells you if you're on the right track

✨ **Don't be afraid to ask Claude Code for help** - That's the whole point!

✨ **Test with different inputs** - Try different grades to see if it works

---

## 📝 Prompts to Use with Claude Code

### For Bug #1:
```
"I found a bug in the calculate_average() function in main.py. 
It's not calculating the average correctly. 
The formula should be: sum of all grades ÷ number of grades.
Can you find and fix the bug?"
```

### For Bug #2:
```
"The get_grades() function in utils.py doesn't validate input. 
It should check that:
1. Grades are between 0 and 100
2. There's at least one grade
3. Each input is a valid number
Can you add input validation to this function?"
```

---

## ✅ How to Know You Fixed It

After you fix each bug:
1. Run `python tests.py`
2. You should see: `✅ All tests passed!`
3. No errors = Bug fixed! 🎉

---

## 🚀 What's Next?

Once both bugs are fixed:
1. Create a new Git branch: `git checkout -b fix/bug-fixes`
2. Commit your changes: `git commit -m "Fix: calculation and validation bugs"`
3. Push to GitHub: `git push origin fix/bug-fixes`
4. Create a Pull Request on GitHub
5. Update your Asana tickets

**You've got this!** 💪
