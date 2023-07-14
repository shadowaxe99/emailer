# Gmail API Project - Starter's Guide

This guide will help you get started with the Gmail API project. The project uses the Gmail API to fetch the latest email from a Gmail account, categorizes the email using a Naive Bayes classifier, generates a reply based on the context of the fetched email using OpenAI's GPT-3 model, and finally creates a new draft email with the auto-generated reply and saves it to the drafts folder of the Gmail account.

## Prerequisites

1. **Python**: The project scripts are written in Python. Make sure you have Python installed on your machine.

2. **Python Libraries**: The project uses several Python libraries. Install them by running `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib openai` in your terminal.

3. **Gmail API credentials**: You need to have a 'credentials.json' file which contains your API credentials. You can get this file from the Google API Console. Replace 'credentials.json' with the path to your actual credentials file, and 'token.json' with the path to your token file.

4. **OpenAI API key**: You need to have an API key from OpenAI. Set your OpenAI API key as an environment variable named 'OPENAI_API_KEY'.

## Running the Project

1. Navigate to the project directory on your Desktop.

2. Run the main script by executing `python main.py` in your terminal.

That's it! The script will fetch the latest email from your Gmail account, categorize the email, generate a reply, and save the reply as a draft in your Gmail account.