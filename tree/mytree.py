import time
import treedata as t
import importlib
import sys

sys.ps1 = "\nmytree.py--> "

#initialize
with open("treedata.py", "r+t") as tdata:
        global tree

        tree = tdata.read().split('\n') #[treename, last_watered, height, chopped_wood]

def update_tree():
    with open("treedata.py", "r+t") as tdata:
        global tree

        tdata.write('\n'.join(tree))

        print("Updated tree.")

        tdata.seek(0)
        tree = tdata.read().split('\n') #[treename, last_watered, height, chopped_wood]

        importlib.reload(t)

def water():
    #check if tree was watered in the last minute
    if (t.last_watered < time.time() - 120):
        global tree

        #update last time watered
        tree[1] = f"last_watered = {int(time.time())}"

        #tree grows 1-4 cm
        tree[2] = f"height = {t.height + int(time.time()) % 4 + 1}"

        update_tree()

        print(f"New height: {t.height}.\n\nWater again in 2 minutes.")

    else:
        remaining_seconds = int(120 - (time.time() - t.last_watered))
        remaining_minutes = remaining_seconds // 60
        remaining_seconds %= 60

        s = lambda x : "s" if x != 1 else ""
        min = lambda x : f"{remaining_minutes} minute{s(x)} and " if x != 0 else ""

        print(f"Please wait {f"{min(remaining_minutes)} {remaining_seconds} second{s(remaining_seconds)}"} to water {t.treename} again.")

def rename():
    global tree

    tree[0] = f"treename = \"{input("What would you like to name your tree?\n--> ")}\""

    update_tree()

    print(f"Renamed your tree to {t.treename}.")

def chop():
    global tree

    t.chopped_wood += int(t.height / 10)
    t.height = 0
    tree[2] = f"height = {t.height}"
    tree[3] = f"chopped_wood = {t.chopped_wood}"

    update_tree()

def chopped_wood():
    print(t.chopped_wood)

def name():
    print("Your tree's name is " + t.treename + ". What a nice name!")

def last_watered():
    print(t.last_watered)

def height():
    print("The tree " + t.treename + ":")
    print(" mmmm\nMMMMMM")
    for num in range(t.height // 10 - 1) or []:
        print("  ||")
    print(f"  ||  {t.height} cm tall")

def commands():
    print()
    print("water()" +   "\t\t" +    "rename()")
    print("name()" +    "\t\t" +    "last_watered()")
    print("height()" +  "\t" +      "chop()")
    print("chopped_wood()" + "\t" + "commands()")

[cmd, cmds] = [commands, commands]

w = water

h = height
