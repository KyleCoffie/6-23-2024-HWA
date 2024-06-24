
import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday ", "Tuesday ", "Wednesday ", "Thursday ", "Friday ", "Saturday ", "Sunday "]
times = ["morning", "afternoon", "evening"]
for day in days:
    for time in times:
        mood = random.choice(moods)
        print("On " + day  + time + " I was feeling " + mood)
