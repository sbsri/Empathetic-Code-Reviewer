Hackathon Mission 1: The Empathetic Code Reviewer
Tagline: Transforming Critical Feedback into Constructive Growth.
The Premise
In software development, code reviews are the lifeblood of a healthy team. They catch
bugs, improve quality, and spread knowledge. However, they are often a source of
friction and a truly mundane task. Written feedback can feel blunt, impersonal, and at
worst, discouraging. A junior developer might feel attacked by a comment like "This is
inefficient," while the senior developer who wrote it was simply being direct. This
communication gap slows down learning and can harm team morale. Your mission is
to build an AI that acts as a bridge, translating raw critique into supportive,
educational guidance, thereby freeing developers from the negative cycle of harsh
feedback.
Your Mission
Create a program that takes a snippet of code and a list of direct, critical review
comments, and then uses Generative AI to rewrite them. The AI should act as an ideal
senior developer or a patient mentor, rephrasing the feedback to be empathetic,
constructive, and educational, ensuring the recipient understands the "why" behind
the suggestion, not just the "what."
Technical Specifications
● Input: Your program will process a JSON object with two keys: code_snippet and
review_comments.
{
"code_snippet": "def get_active_users(users):\n results = []\n for u in users:\n
if u.is_active == True and u.profile_complete == True:\n results.append(u)\n
return results",
"review_comments": [
"This is inefficient. Don't loop twice conceptually.",
"Variable 'u' is a bad name.",
"Boolean comparison '== True' is redundant."
]
}
● Required Output: Your program must produce a single, well-formatted
Markdown report. For each original comment, you must generate a section that
includes:

1. Positive Rephrasing: A gentle and encouraging version of the feedback.
2. The 'Why': A clear, concise explanation of the underlying software principle
(e.g., performance, readability, convention).
3. Suggested Improvement: A concrete code example demonstrating the
recommended fix.
Example structure for one part of the output:---
### Analysis of Comment: "This is inefficient. Don't loop twice conceptually."
* **Positive Rephrasing:** "Great start on the logic here! For better
performance, especially with large user lists, we can make this more efficient
by combining the checks."
* **The 'Why':** Iterating through a list and performing checks can become slow
as the list grows. By using more direct methods like list comprehensions, we
can often achieve the same result with cleaner and faster code.
* **Suggested Improvement:**
```python
def get_active_users(users):
return [user for user in users if user.is_active and
user.profile_complete]
```
---
Tips for Standing Out
● Contextual Awareness: Can your AI's tone change based on the severity of the
original feedback?
● Link to Resources: Can your AI provide a link to external documentation (e.g., a
relevant part of a style guide like PEP 8 for Python, or an article on algorithmic
complexity) to support its suggestion?
● Holistic Summary: Can you add a concluding paragraph that summarizes the
overall feedback in an encouraging way?
Key Skills Tested
● Nuanced Prompt Engineering
● Empathetic AI Design
● Code Comprehension and Explanation
