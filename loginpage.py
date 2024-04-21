
import requests
from tkinter import *

# API endpoint for authentication
API_ENDPOINT = 'https://your-api-endpoint.com/login'

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Prepare the data to be sent to the API
    data = {'username': username, 'password': password}

    # Send a POST request to the API endpoint
    response = requests.post(API_ENDPOINT, data=data)

    # Check the response from the API
    if response.status_code == 200:
        message_label.config(text='Login successful!', fg='green')
    else:
        message_label.config(text='Login failed. Please try again.', fg='red')

# Create the GUI window
window = Tk()
window.title('Login Page')

# Create username and password entry fields
username_label = Label(window, text='Username:' ,font=("Arial",12))
username_label.pack()
username_entry = Entry(window  ,font=("Arial",12))
username_entry.pack()

password_label = Label(window, text='Password:' ,font=("Arial",12))
password_label.pack()
password_entry = Entry(window, show='*' ,font=("Arial",12))
password_entry.pack()

# Create login button
login_button = Button(window, text='Login', command=login ,font=("Arial",12))
login_button.pack()

# Create message label for displaying login status
message_label = Label(window, text='', fg='black',font=("Arial",12))
message_label.pack()

# Run the GUI window
window.mainloop()
