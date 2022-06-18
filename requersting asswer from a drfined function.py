print("What is Your name")
Names = str(input())
print("What is Your post")
Posts = str(input())
print("What is Your level")
Levels = str(input())

def Status (Name, Post, Level):
    print("Welcome Mr " + Name)
    print("Your post is " + Post)
    print("Your Level is " + Level)

Name = Names
Post = Posts
Level = Levels

Status(Name, Post, Level)

#Normal way to use if ex explained
Status("Segun", "Driver", "10")

#Status("Input your name " + str(input()),"Input your post " + str(input()),"Input your level " + str(input()))
