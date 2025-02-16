import streamlit as st
import google.generativeai as ai

# Configure the Google Generative AI API
ai.configure(api_key="AIzaSyCvFT6tTun41MkuGSau043SSAuuHzpJZyw")  # Corrected the syntax for the API key

# System prompt for code review
sys_prompt = """You are a helpful AI Code Reviewer. 
                Users will submit their Python code for review.
                Your task is to analyze the code, identify potential bugs, 
                errors, or areas of improvement, and provide suggestions for fixes.
                Always include a fixed code snippet as part of your response.
                If the code is correct, kindly confirm that it is error-free.
                In case if the user has questions outside the code review scope, 
                politely decline and tell them to ask questions related to Python code only.
                """

# Initialize the generative model
code_review_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

# Streamlit application title
st.title("AI Code Reviewer")

# Text area for user to input their Python code
user_code = st.text_area(label="Enter your Python code for review", placeholder="def example_function():\n    print('Hello, World!')")

# Button to submit the code for review
btn_click = st.button("Review Code")

# Process the code review when the button is clicked
if btn_click:
    if user_code.strip():  # Check if the user has entered any code
        response = code_review_model.generate_content(user_code)
        st.write("### Review Feedback:")
        st.write(response.text)
    else:
        st.warning("Please enter some Python code to review.")
