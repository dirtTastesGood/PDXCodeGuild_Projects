import random

def getEyes(eyes):
    return random.choice(eyes)
def getNose(noses):
    return random.choice(noses)
def getMouth(mouths):
    return random.choice(mouths)

def main():
    
    eye_list = [":", ";", "=", "8"]
    nose_list = ["-","^"]
    mouth_list = [")", "(", "D", "*", "p", ">"]

    x=0
    while x<5:
        eyes = getEyes(eye_list)
        nose = getNose(nose_list)
        mouth = getMouth(mouth_list)
        print(f"{eyes}{nose}{mouth}")
        x += 1

main()