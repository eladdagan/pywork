import json
import os

# מחלקה ליצירת הדמות של השחקן
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.items = []
        self.experience = 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def add_item(self, item):
        self.items.append(item)

    def add_experience(self, points):
        self.experience += points

    def __str__(self):
        return f"{self.name}: {self.health} HP, {self.experience} XP, Items: {', '.join(self.items)}"

# פונקציה לשמירה של נתוני השחקן לקובץ JSON
def save_player(player):
    with open('player_data.json', 'w') as file:
        json.dump(player.__dict__, file)

# פונקציה לטעינת נתוני השחקן מקובץ JSON
def load_player():
    if os.path.exists('player_data.json'):
        with open('player_data.json', 'r') as file:
            data = json.load(file)
            player = Player(data['name'])
            player.health = data['health']
            player.items = data['items']
            player.experience = data['experience']
            return player
    else:
        return None

# פונקציה להצגת אפשרויות
def show_choices():
    print("\nבחר אחת מהאפשרויות:")
    print("1. המשך למסע")
    print("2. צפה בפרופיל שלך")
    print("3. שמור ויצא")
    print("4. טען משחק ישן")

# פונקציה למסע המשחק
def adventure_game():
    print("ברוך הבא למשחק הרפתקאות!")
    player_name = input("הכנס את שמך השחקן: ")
    player = load_player()

    if player is None:
        print(f"שלום {player_name}, יצרת דמות חדשה!")
        player = Player(player_name)
    else:
        print(f"שלום {player_name}, נתונים ישנים נמצאו ונטענו!")

    while True:
        show_choices()
        choice = input("בחר אפשרות: ")

        if choice == '1':
            print("\nאתה יוצא למסע חדש!")
            player.add_experience(10)
            print(f"נוספו לך 10 נקודות ניסיון! ניסיון נוכחי: {player.experience}")
        elif choice == '2':
            print(f"\nפרופיל שלך:\n{player}")
        elif choice == '3':
            print("\nשומר את המשחק... תודה ששיחקת!")
            save_player(player)
            break
        elif choice == '4':
            print("\nמנסה לטעון משחק ישן...")
            player = load_player()
            if player is not None:
                print(f"המשחק טוען את הנתונים הישנים שלך:\n{player}")
            else:
                print("לא נמצאו נתונים ישנים!")
        else:
            print("אפשרות לא תקינה, נסה שוב.")

# הרצת המשחק
adventure_game()
