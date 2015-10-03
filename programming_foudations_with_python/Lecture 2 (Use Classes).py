
# coding: utf-8

# In[2]:

# Drawing
import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    # Create a turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)  
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    
    # Create the turtle Angie - Draws a circle
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)
    
    window.exitonclick()
        
draw_art()


# In[18]:

# Send Text Message
from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACb5759855970c9efe63e670e417da294c"
auth_token  = "176583c110385a342dd15305c05a627c"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="My name is Tuan!!!",
    to="+17149305270",    # Replace with your phone number
    from_="+17146811708") # Replace with your Twilio number
print message.sid


# In[32]:

# Profanity Editor
import urllib
 
def read_text():
    quotes = open("C:/Vindico/Projects/Data/Course/Python/Udacity/Programming Foundations with Python/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")    
    
read_text()

