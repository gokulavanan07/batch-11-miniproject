import random
import colorama
from rich.console import Console
import colorama
def banner():
    console = Console()
    Star_Wars =
    """
    .______        ___      .___________.  ______  __    __         __   __  
    |   _  \      /   \     |           | /      ||  |  |  |       /_ | /_ | 
    |  |_)  |    /  ^  \    `---|  |----`|  ,----'|  |__|  |        | |  | | 
    |   _  <    /  /_\  \       |  |     |  |     |   __   |        | |  | | 
    |  |_)  |  /  _____  \      |  |     |  `----.|  |  |  |        | |  | | 
    |______/  /__/     \__\     |__|      \______||__|  |__|        |_|  |_| 
                                                                            
    """
    console.print(Star_Wars, style="bold yellow")
    console.print("Creators : \n", style="bold cyan")
    console.print("DINESH KUMAR P \nGOKULAVANAN M \nJASHWANTH T", style="bold yellow")
banner()
questions = [
    ("How do you feel after receiving a promotion at work?", "A) Thrilled", "B) Heartbroken", "C) Anxious", "D) Furious", "E) Astonished"),
    ("How do you feel when your favorite team wins the championship?", "A) Ecstatic", "B) Sorrowful", "C) Terrified", "D) Annoyed", "E) Shocked"),
    ("What is your reaction to losing a dear friend?", "A) Cheerful", "B) Despondent", "C) Scared", "D) Enraged", "E) Startled"),
    ("How do you feel after watching a scary movie alone at night?", "A) Content", "B) Mournful", "C) Frightened", "D) Irritated", "E) Amazed"),
    ("How do you react to a sudden loud noise in the middle of the night?", "A) Delighted", "B) Grieving", "C) Panicked", "D) Outraged", "E) Stunned"),
    ("What is your reaction to receiving unexpected good news?", "A) Elated", "B) Melancholy", "C) Nervous", "D) Mad", "E) Astonished"),
    ("How do you feel when someone cuts you off in traffic?", "A) Blissful", "B) Tearful", "C) Apprehensive", "D) Furious", "E) Taken aback"),
    ("How do you feel when you lose your wallet?", "A) Jubilant", "B) Dejected", "C) Worried", "D) Livid", "E) Surprised"),
    ("What is your reaction to receiving a heartfelt apology?", "A) Contented", "B) Somber", "C) Uneasy", "D) Vexed", "E) Shocked"),
    ("How do you feel when you meet an old friend unexpectedly?", "A) Overjoyed", "B) Woeful", "C) Anxious", "D) Resentful", "E) Astonished"),
    ("How do you react to seeing a spider on your bed?", "A) Delighted", "B) Crestfallen", "C) Terrified", "D) Enraged", "E) Amazed"),
    ("How do you feel when someone praises your work?", "A) Pleased", "B) Depressed", "C) Nervous", "D) Annoyed", "E) Astonished"),
    ("What is your reaction to failing an important exam?", "A) Cheerful", "B) Heartbroken", "C) Apprehensive", "D) Furious", "E) Startled"),
    ("How do you feel when you hear a strange noise at night?", "A) Thrilled", "B) Sorrowful", "C) Scared", "D) Irritated", "E) Surprised"),
    ("How do you react to a surprise birthday party?", "A) Elated", "B) Mournful", "C) Nervous", "D) Mad", "E) Shocked"),
    ("How do you feel when you are stuck in a traffic jam?", "A) Blissful", "B) Despondent", "C) Anxious", "D) Enraged", "E) Taken aback"),
    ("How do you feel after losing a pet?", "A) Jubilant", "B) Tearful", "C) Worried", "D) Livid", "E) Surprised"),
    ("What is your reaction to getting an unexpected gift?", "A) Overjoyed", "B) Dejected", "C) Uneasy", "D) Resentful", "E) Astonished"),
    ("How do you feel when someone criticizes you unfairly?", "A) Contented", "B) Somber", "C) Apprehensive", "D) Furious", "E) Shocked"),
    ("How do you feel when you make a new friend?", "A) Delighted", "B) Crestfallen", "C) Scared", "D) Annoyed", "E) Amazed"),
    ("How do you feel when you watch a romantic movie?", "A) Thrilled", "B) Sorrowful", "C) Nervous", "D) Enraged", "E) Surprised"),
    ("What is your reaction to hearing bad news?", "A) Elated", "B) Heartbroken", "C) Terrified", "D) Mad", "E) Startled"),
    ("How do you feel when you find out you are getting a raise?", "A) Blissful", "B) Mournful", "C) Apprehensive", "D) Irritated", "E) Astonished"),
    ("How do you feel when you see a beautiful sunset?", "A) Overjoyed", "B) Despondent", "C) Scared", "D) Annoyed", "E) Surprised"),
    ("How do you feel after a long, stressful day?", "A) Jubilant", "B) Tearful", "C) Nervous", "D) Enraged", "E) Amazed"),
    ("How do you feel when you receive a compliment?", "A) Pleased", "B) Dejected", "C) Worried", "D) Resentful", "E) Shocked"),
    ("How do you feel when you watch a sad movie?", "A) Cheerful", "B) Heartbroken", "C) Apprehensive", "D) Furious", "E) Astonished"),
    ("How do you feel when someone lies to you?", "A) Thrilled", "B) Sorrowful", "C) Scared", "D) Mad", "E) Surprised"),
    ("How do you feel when you find out you have a serious illness?", "A) Elated", "B) Mournful", "C) Terrified", "D) Irritated", "E) Startled"),
    ("How do you feel when you achieve a difficult goal?", "A) Blissful", "B) Despondent", "C) Anxious", "D) Enraged", "E) Astonished"),
    ("How do you feel when someone close to you moves away?", "A) Overjoyed", "B) Tearful", "C) Worried", "D) Resentful", "E) Surprised"),
    ("How do you feel when you find out a secret?", "A) Contented", "B) Dejected", "C) Uneasy", "D) Furious", "E) Amazed"),
    ("How do you feel when you are in a dangerous situation?", "A) Delighted", "B) Crestfallen", "C) Frightened", "D) Annoyed", "E) Shocked"),
    ("How do you feel when you miss an important event?", "A) Thrilled", "B) Heartbroken", "C) Apprehensive", "D) Mad", "E) Astonished"),
    ("How do you feel when you are praised in front of others?", "A) Elated", "B) Sorrowful", "C) Nervous", "D) Irritated", "E) Surprised"),
    ("How do you feel when you accidentally break something valuable?", "A) Blissful", "B) Mournful", "C) Terrified", "D) Enraged", "E) Startled"),
    ("How do you feel when you have to speak in public?", "A) Overjoyed", "B) Despondent", "C) Anxious", "D) Annoyed", "E) Astonished"),
    ("How do you feel when you are ignored by friends?", "A) Jubilant", "B) Tearful", "C) Worried", "D) Furious", "E) Surprised"),
    ("How do you feel when you are in a strange place?", "A) Contented", "B) Dejected", "C) Uneasy", "D) Resentful", "E) Amazed"),
    ("How do you feel when you find out you have been betrayed?", "A) Delighted", "B) Crestfallen", "C) Frightened", "D) Mad", "E) Shocked"),
    ("How do you feel when you find out someone has been spreading rumors about you?", "A) Thrilled", "B) Heartbroken", "C) Apprehensive", "D) Furious", "E) Astonished")
]

def main():
    happiness = 0
    sadness = 0
    fear = 0
    anger = 0
    surprise = 0
    
    selected_questions = random.sample(questions, 20)
    
    for q in selected_questions:
        print(colorama.Fore.YELLOW)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(colorama.Fore.RESET)
        print(colorama.Fore.RED)
        print("\n",q[0])
        print(colorama.Fore.RESET)
        print(colorama.Fore.GREEN)
        print(q[1])
        print(q[2])
        print(q[3])
        print(q[4])
        print(q[5])
        print(colorama.Fore.RESET)
        print(colorama.Fore.BLUE)
        answer = input("Select an option (A/B/C/D/E): ").strip().upper()
        print(colorama.Fore.RESET)
        print(colorama.Fore.YELLOW)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print(colorama.Fore.RESET)
        
        if answer == "A":
            happiness += 1
        elif answer == "B":
            sadness += 1
        elif answer == "C":
            fear += 1
        elif answer == "D":
            anger += 1
        elif answer == "E":
            surprise += 1
        else:
            print(colorama.Fore.RED)
            print("Invalid option. Please select A, B, C, D, or E.")
            print(colorama.Fore.RESET)
    
    # print("\nResults:")
    # print(f"Happiness: {happiness}")
    # print(f"Sadness: {sadness}")
    # print(f"Fear: {fear}")
    # print(f"Anger: {anger}")
    # print(f"Surprise: {surprise}")
    
    max_emotion = max(happiness, sadness, fear, anger, surprise)
    print(colorama.Fore.YELLOW)
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(colorama.Fore.RESET)
    if max_emotion == happiness:
        print(colorama.Fore.GREEN)
        print("""
        You are Happy now !!:
              
            Embrace the joy you feel right now, and let it be a reminder of the beauty and goodness in life. 
            Cherish these moments and spread your positive energy to those around you.
            """)
        print(colorama.Fore.RESET)
    elif max_emotion == sadness:
        print(colorama.Fore.BLUE)
        print("""
        You are Sad now !!:
              
            Even in your darkest moments, remember that this too shall pass. Allow yourself to feel, heal, and grow. 
            Every storm brings with it the promise of a brighter, more hopeful tomorrow
            """)
        print(colorama.Fore.RESET)
    elif max_emotion == fear:
        print(colorama.Fore.RED)
        print("""
        You are in Fear now !!:
              
            Courage isn't the absence of fear, but the triumph over it. Face your fears head-on, 
            knowing that each step forward makes you stronger, braver, and more resilient than before.
            """)
        print(colorama.Fore.RESET)
    elif max_emotion == anger:
        print(colorama.Fore.RED)
        print("""
        You are in Anger now !!:
              
            Use your anger as fuel for positive change. Channel it into constructive actions and meaningful growth. 
            Remember, true strength lies in turning anger into a force for good and personal empowerment.
            """)
        print(colorama.Fore.RESET)
    else:
        print(colorama.Fore.GREEN)
        print("""
        You are Suprise now !!:
              
            Embrace the unexpected twists and turns of life with an open heart. Surprises often bring new opportunities and perspectives. 
            Trust in your ability to adapt and thrive in the face of the unknown.
            """)
        print(colorama.Fore.RESET)
    print(colorama.Fore.YELLOW)
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(colorama.Fore.RESET)
        
if __name__ == "__main__":
    main()
