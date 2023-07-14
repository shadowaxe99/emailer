# Gmail API Project

This project uses the Gmail API to fetch the latest email from a Gmail account, categorizes the email using a Naive Bayes classifier, generates a reply based on the context of the fetched email using OpenAI's GPT-3 model, and finally creates a new draft email with the auto-generated reply and saves it to the drafts folder of the Gmail account.

## Scripts

The project consists of the following scripts:

- `fetch_email.py`: Fetches the latest email from the user's Gmail account.
- `categorize_email.py`: Categorizes the fetched email using a Naive Bayes classifier.
- `generate_reply.py`: Generates a reply based on the context of the fetched email using OpenAI's GPT-3 model.
- `create_draft.py`: Creates a new draft email with the auto-generated reply and saves it to the drafts folder of the Gmail account.
- `main.py`: The main script that integrates all the functionalities.

## Instructions

1. Navigate to the project directory on your Desktop.
2. Install the necessary dependencies by running `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib openai`.
3. Run the main script by executing `python main.py`.

Please note that you need to replace 'credentials.json' with the path to your actual credentials file, and 'token.json' with the path to your token file. You also need to set your OpenAI API key as an environment variable named 'OPENAI_API_KEY'.