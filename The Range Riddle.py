import random

days=["Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
emotions= ("happy","sad","energetic","calm") 
for day in days:
    emotion = random.choice(emotions)
    print ("On " + day + " I felt " + emotion)