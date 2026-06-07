# Luis Cortez
# Date: June 7, 2026
# Assignment: Module 1.3 – On the Wall + Flowchart
# Purpose: This program asks the user for the number of bottles of beer
# and displays a countdown using a function until reaching 0.

# Display the countdown song.
def countdown(bottles):

    # Continue until bottles reaches 0.
    while bottles > 0:

        # Handle singular and plural wording.
        if bottles == 1:
            print(
                f"\n1 bottle of beer on the wall, "
                f"1 bottle of beer."
            )
        else:
            print(
                f"\n{bottles} bottles of beer on the wall, "
                f"{bottles} bottle(s) of beer."
            )

        # Display next lyric.
        print(
            f"Take one down and pass it around, "
            f"{bottles - 1} bottle(s) of beer on the wall."
        )

        # Reduce bottle count.
        bottles -= 1


# Main program.
def main():

    # Ask user for input.
    bottles = int(
        input("Enter number of bottles of beer on the wall: ")
    )

    # Call countdown function.
    countdown(bottles)

    # Final message.
    print("\nTime to buy more bottles of beer.")


# Start program.
main()