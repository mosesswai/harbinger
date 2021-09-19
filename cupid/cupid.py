#########################
###### Cupid Module #####
#########################

import secrets

class Cupid:

    # JSON data URL
    SOURCE_URL = secrets.message_source_url

    # Messages to be displayed
    message = None
    no_message = "No love ..."

    # Refresh counter
    refresh_count = 0
    ignore_count = 20

    ##### Initializer #####
    def __init__(self):
        pass

    ##### Updater #####
    def update(self, matrixportal):
        response = matrixportal.network.fetch(self.SOURCE_URL)
        if response.status_code == 200:
            entries = response.json()['values']
            value = entries[0][0]
        
            if value == self.message:
                self.refresh_count = self.refresh_count + 1
            else:      
                self.message = value
                self.refresh_count = 0


    ##### Refresher #####
    def refresh(self, matrixportal):
        if self.message is None or self.refresh_count > self.ignore_count:
            matrixportal.set_text(self.no_message, 0)
        else:
            matrixportal.set_text(self.message, 0)
        