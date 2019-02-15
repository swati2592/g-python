import re


def main() :
    string = "Popularity by Name : 1990"
    match = re.search(r"(Popularity by Name : )(\d\d\d\d)" , string)
    if match :
        print("found" + match.group(2))


if __name__ == '__main__':
  main()