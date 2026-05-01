# Ici les imports 
import pandas as pd

def main():
    # C'est ici que tu dois remplir ton code
    print("Main program")
    data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    
    survived = data[data["Survived"] == 1]
    non_survivant = data[data["Survived"] == 0]
    print("\nSurvived")
    print("\nnon_survivant")

    data_sorted = data.sort_values(by="Name")
    print(data_sorted["Name"])


# On pourra voir ça ensemble mais ne t'occupe pas de ça
if __name__ == "__main__":
    main()