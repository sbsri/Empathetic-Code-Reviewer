#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json

# This is a placeholder function for interacting with a Generative AI model.
# In a real-world scenario, you would replace this with an actual API call (e.g., to a Google AI model, OpenAI, etc.).
def generate_response_from_ai(prompt):
    # This is a mock response that you would get from the AI.
    # The real implementation would parse the model's output based on your prompt.
    mock_responses = {
        "This is inefficient. Don't loop twice conceptually.": {
            "rephrasing": "Great start on the logic here! For better performance, especially with large user lists, we can make this more efficient by combining the checks.",
            "why": "Iterating through a list and performing checks can become slow as the list grows. By using more direct methods like list comprehensions, we can often achieve the same result with cleaner and faster code.",
            "improvement": "return [user for user in users if user.is_active and user.profile_complete]"
        },
        "Variable 'u' is a bad name.": {
            "rephrasing": "Nice work on the loop! To make your code more readable for others (and your future self), let's use a more descriptive variable name.",
            "why": "Clear variable names are crucial for code readability. Using a full word like 'user' instead of a single letter like 'u' makes the code's purpose immediately obvious without needing to read the surrounding context.",
            "improvement": "for user in users:"
        },
        "Boolean comparison '== True' is redundant.": {
            "rephrasing": "You've correctly identified the conditions you want to check. There's a small Pythonic trick that can make this a little cleaner.",
            "why": "In Python, boolean expressions are evaluated directly as `True` or `False`. Comparing a boolean variable to `True` (e.g., `is_active == True`) is redundant. The expression `is_active` already evaluates to `True` or `False` on its own.",
            "improvement": "if user.is_active and user.profile_complete:"
        }
    }
    return mock_responses.get(prompt, {})

# Our input data as specified in the mission.
input_json = {
    "code_snippet": "def get_active_users(users):\n results = []\n for u in users:\n  if u.is_active == True and u.profile_complete == True:\n   results.append(u)\n return results",
    "review_comments": [
        "This is inefficient. Don't loop twice conceptually.",
        "Variable 'u' is a bad name.",
        "Boolean comparison '== True' is redundant."
    ]
}

# Add an optional section to the end for a summary.
holistic_summary = "This is a great first draft! You've successfully implemented the core logic. The suggestions provided will help you write cleaner, more efficient, and more Pythonic code. Keep up the excellent work!"


# In[3]:


def empathetic_code_reviewer(input_data):
    # Parse the input JSON.
    code_snippet = input_data["code_snippet"]
    review_comments = input_data["review_comments"]

    # Initialize the Markdown report.
    markdown_report = "# Empathetic Code Review Report\n\n"
    markdown_report += "Below is a detailed analysis of the code snippet, rephrasing feedback to be constructive and educational.\n\n"

    # Iterate through each comment and generate the AI-enhanced feedback.
    for comment in review_comments:
        # Craft the prompt for the Generative AI. This is where the magic happens.
        # This prompt is designed to elicit the specific outputs we need.
        prompt = f"""
        Act as a patient, empathetic, and highly knowledgeable senior developer.
        You are reviewing the following Python code snippet:
        
        ```python
        {code_snippet}
        ```
        
        You have a critical review comment: "{comment}".
        
        Your task is to rewrite this comment in a positive, constructive, and educational way.
        Please provide your response in three distinct parts:
        
        1.  **Positive Rephrasing:** A gentle and encouraging version of the feedback.
        2.  **The 'Why':** A clear, concise explanation of the underlying software principle.
        3.  **Suggested Improvement:** A concrete code example demonstrating the recommended fix.
        
        Structure your response clearly so it can be easily parsed.
        """
        
        # Use a placeholder for the AI response. In a real application, you would
        # send the `prompt` to your Generative AI model and get a response.
        ai_response = generate_response_from_ai(comment)

        # Build the markdown section for this comment.
        if ai_response:
            markdown_report += "---\n"
            markdown_report += f"### Analysis of Comment: \"{comment}\"\n"
            markdown_report += f"* **Positive Rephrasing:** \"{ai_response['rephrasing']}\"\n"
            markdown_report += f"* **The 'Why':** {ai_response['why']}\n"
            markdown_report += "* **Suggested Improvement:**\n"
            markdown_report += f"```python\n{ai_response['improvement']}\n```\n"

    # Add the optional holistic summary at the end.
    markdown_report += "---\n"
    markdown_report += f"## Overall Summary\n\n{holistic_summary}"

    return markdown_report

# Run the program and print the final report.
final_report = empathetic_code_reviewer(input_json)
print(final_report)


# In[ ]:




