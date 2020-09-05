import os


def main():
    cwd = os.getcwd()
    print("working directory: " + cwd)
    print("Maybe some Azure, AWS, Google data pull here with some Python API.")
    # Python API Interfacing
    print("Doing R things")
    os.system("r /usr/bin/script.R")


if __name__ == "__main__":
    main()
