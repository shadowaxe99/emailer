class ContactManager:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, email, company=None, last_interaction=None):
        if name in self.contacts:
            print(f'Contact {name} already exists.')
        else:
            self.contacts[name] = {'email': email, 'company': company, 'last_interaction': last_interaction}

    def update_contact(self, name, email=None, company=None, last_interaction=None):
        if name in self.contacts:
            if email:
                self.contacts[name]['email'] = email
            if company:
                self.contacts[name]['company'] = company
            if last_interaction:
                self.contacts[name]['last_interaction'] = last_interaction
        else:
            print(f'Contact {name} does not exist.')

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print(f'Contact {name} does not exist.')

    def get_contact(self, name):
        return self.contacts.get(name)

    def search_contact(self, name):
        return self.contacts.get(name)

    def list_contacts(self):
        return self.contacts