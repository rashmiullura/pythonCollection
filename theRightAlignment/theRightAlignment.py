# idea:
# * read the whole file given by param
# * find the length of the longest line
# * add for each line enough whitespace (spaces, of course! not tabs) to make them all aligned to the right
# * weird 80 character-rules can be just satisfied if the longest line would be <= 80 chars

#------------------------

# motivation:
#  a small test-ballon during lunch-break about code-styling and if we should use, for isntance, clang-format,
#  resulted in a argument. if applying a "one rule fits the whole team" is proper and good or not. or if your
#  personal way to write code is suppressed. my argument was then, that if we have no codes-styling-agreement, i could
#  also commit my new files with proper right-alignment, or? since it is not forbidden or wanted to have left-aligned
#  style.
#
#  of course, i doubt that i would pull this of (professionalism), but the idea sparked my interest. shouldn't be too
#  hard to write a python-skript which can be used with xargs/parallel on bash on all the touched files in the last
#  git-commit.

#------------------------


# ----------------- main function -----------------
def main():
    import sys

    # get the parameters
    if len(sys.argv) == 2:
        fileToProcessPath = sys.argv[1]
    else:
        raise Exception("Not enough parameters specified: first must be fileToProcessPath.")

# ----------------- execution -----------------
if __name__ == "__main__":
    main()