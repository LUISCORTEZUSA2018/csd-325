# ---------------------------------------------------
# Luis Cortez
# Assignment 1.3 - On the Wall + Flowchart
# CSD-325 Advanced Python
# ---------------------------------------------------


def countdown(bottles):

    while bottles > 0:

        if bottles == 1:
            print(f"\n{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        else:
            print(f"\n{bottles} bottles of beer on the wall, {bottles} bottles of beer.")

        bottles -= 1

        print(
            f"Take one down and pass it around, "
            f"{bottles} bottle(s) of beer on the wall."
        )


def main():

    bottles = int(input("Enter number of bottles of beer on the wall: "))

    countdown(bottles)

    print("\nTime to buy more bottles of beer.")


main()