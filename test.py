
import sys
from messageclass import Message


def main(args=None):
    """
    The main entry point of the program.

    Args:
        args: Command-line arguments (optional).
    """
    if args is None:
        args = sys.argv[1:]

    # print(f"Script name: {sys.argv[0]}")
    # if args:
    #     print(f"Arguments received: {args}")
    # else:
    #     print("No arguments provided.")

    # Call other functions from main()
    testmessage = Message()
    testmessage.testsetup_bletchley()
    testmessage.decrypt()
    testmessage.printmessage(style="BletchleyPark")


if __name__ == "__main__":
    # This block is executed only when the file is run directly.
    # It serves as the program's entry point.
    sys.exit(main())