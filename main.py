# Ici les imports 
import pandas as pd

def get_survived(data):
    return data[data["Survived"] == 1]

def get_dead_people(data):
    return data[data["Survived"] == 0]

def get_by_age_over(data, age):
    return data[data["Age"] >= age]

def get_peoples_name(data):
    return data[data["Name"]]

def get_people_by_genre(data, genre):
    return data[data["Sex"] == genre]

def print_new_line(str):
    print("\n" + str)    

def main():
    # C'est ici que tu dois remplir ton code
    print("Main program")
    data = pd.read_csv("./titanic.csv")

    survived = get_survived(data)
    dead = get_dead_people(data)

    #Survivants
    print_new_line("Survived")
    # print(survived[["Name"]].head(12345).to_string(index=False, header=None))
    print(survived[["Name"]].head().to_string(index=False, header=None))
    # Non-survivant
    print_new_line("Décédé")
    print(dead[["Name", "Survived"]].head())

    
# On pourra voir ça ensemble mais ne t'occupe pas de ça
if __name__ == "__main__":
    main()