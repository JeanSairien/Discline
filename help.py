from os import system

def print_help():
    system("clear")
    system("echo 'Available Commands: \n" \
        + "---------------------------------- \n" \
        + "/channel  - switch to channel \n" \
        + "/server   - switch server  \n" \
        + "\n" \
        + "/servers  - list available servers \n" \
        + "/channels - list available channels \n" \
        + "/users    - list servers users \n" \
        + "\n" \
        + "/nick     - change server nick name \n" \
        + "/game     - change your game status \n" \
        + "/quit     - exit cleanly \n" \
        + "\n \n" \
        + "(press q to quit this dialog) \n" \
        + "' | less")
