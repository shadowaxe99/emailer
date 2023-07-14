import logging

from fetch_email import fetch_latest_email
from categorize_email import categorize_email
from generate_reply import generate_reply, save_draft

# Setup logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    try:
        # Fetch the latest email
        email_content = fetch_latest_email()
        
        if not email_content:
            logger.error('No email content fetched.')
            return
        
        # Categorize the email
        category = categorize_email(email_content)
        if category is None:
            logger.error('Failed to categorize the email.')
            return
        
        logger.info(f'The email was categorized as {category}')

        # Generate a different reply based on the email category
        if category == 'spam':
            reply = 'This is a spam message. No reply will be generated.'
        else:
            reply = generate_reply(email_content)

        if reply is None:
            logger.error('Failed to generate a reply.')
            return

        logger.info(f'Generated reply: {reply}')

        # Ask user if they want to save the draft
        save_draft_choice = input('Do you want to save the generated reply as a draft? (yes/no): ')
        if save_draft_choice.lower() == 'yes':
            # Save the reply as a draft
            # Note: You'll need to provide the Gmail API service instance and user_id
            # save_draft(service, user_id, reply)

    except Exception as e:
        logger.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()