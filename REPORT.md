# Project Report: AI-Assisted Development

## 1. Initial Approach
* **Understanding:** 
Strategy: For the terminal implementation, I want to compare the states of the arrays before and after the if condition. If two are different, then we know that there happens to be a change inside the array. And for printing, I just need to grab the value of the items in the array, and use the print("##"*(n+1)) so that it prints a bar that is a bit more than twice the length, so it appears longer and easiler to look at. I also use the colorama library to format the colors of terminal
* **Assumptions:** 
I assumed the project to be fairly challenging due to the fact that i have never worked with this visualization before. However, it was fairly easy due to the usage of yield and more

## 2. Prompting & AI Interaction
* **Successes:** Asking the AI to test my code. It was useful in this regard since it detected the OS problem, where windows users will find error in this at the clear() function
* **Failures:** In the feedback, it does say that int(20.5) returns a float, which is not true, since it just returns 20.
* **Analysis:** The error happens because of the workload it has to receive, so it may forget things and hallucinate. It does not hinder much of my work since the error is in the area that I know

## 3. Key Learnings
* **Technical Skills:** I discover Claude - which is pretty good in coding - to generate code for me for the pygame implementation (we were allowed to use it). For the CS skills, I think I started to adopt the planning before coding habit, and also more advanced python knowledge (specifically generators)
* **AI Workflow:** I don't think much will be change, I will still try to minimize it