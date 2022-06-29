# UbuntuLoginAlerts
Allows a Discord webhook message to be send on login.
Please note that this was tested on Ubuntu 22.04 and may not work on other versions/operating systems.

# Creating a Discord webhook
The first thing you will need is a Discord webhook.

To create a webhook:
1. Go to a channel that you are able to manage.
2. Click on "Integrations".
3. Click on "Create Webhook". 
4. Click "Copy Webhook URL".
5. Once the webhook URL has been copied, paste it into the webhook_url variable in the login_alert.py file.

# Adding link to panel (optional)
If the server is hosted externally and the host has a online panel, copy the link to that panel and paste it into the panel_page variable in the login_alert.py file.
Doing this will allow you to access your server settings/options with ease.

# Setting up
Please make sure you are on Ubuntu 20+ as it may not work properly on other versions.
You will also need to have python3 installed (this should already come preinstalled).

1. Go to your root directory then type "cd /etc/profile.d". Files in this directory will be ran on login.
2. Type "touch login_alert.sh" to create the file that will run our python script.
3. Type "nano login_alert.sh" to open the text editor. Copy the code from login_alert.sh on this page and right click to paste it into the editor. Then, click CTRL+x and ENTER to close and save the file.
4. Type "touch login_alert.py" to create the python file.
5. Type "nano login_alert.py" and paste in the code from login_alert.py from this page. Then, click CTRL+x and ENTER to save and close the editor.

The setup should be complete and ever time someone logs in, a message will be sent through that webhook.
