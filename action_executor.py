import calendar_integration


def execute_action(intent, data):
    """Executes an action based on the intent and the data."""
    if intent == 'schedule':
        # The action for the 'schedule' intent is to create a new event in the user's Google Calendar
        calendar_integration.create_event(data)
    else:
        print(f'Unknown intent: {intent}')