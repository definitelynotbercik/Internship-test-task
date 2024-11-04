import sys
import random


def main():
    """
    Main function that acts as a pseudo-random number generator responding to specific commands.

    This program listens for commands via standard input and responds as follows:

    - "Hi": Responds with "Hi".
    - "GetRandom": Responds with a random integer between 1 and 100.
    - "Shutdown": Terminates the program gracefully.

    If an unrecognized command is received, it is ignored, allowing the program to continue
    processing further commands.
    """

    while True:
        command = input().strip()

        if command == 'Hi':
            print('Hi')

        elif command == 'GetRandom':
            print(random.randint(1, 100))

        elif command == 'Shutdown':
            break


if __name__ == '__main__':
    main()
