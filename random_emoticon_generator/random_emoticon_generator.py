import random

eye_list = [":", ";", "=", "8"]
nose_list = ["-","o"]
mouth_list = [")", "(", "D", "*", "p", ">"]

eyes = random.choice(eye_list)
nose = random.choice(nose_list)
mouth = random.choice(mouth_list)

print(f"{eyes}{nose}{mouth}")