#!/usr/bin/env python
from googlesearch import search
print(
    "Welcome to TerminalSearch 0.1 alpha"
)


def TerminalSearch():
    query = input("What is your query? \n")

    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)
    runagain = input("Do you want to search again? (y/n) \n")
    runagain = runagain.lower()
    if runagain == "y":
        hemagnasearch()
    else:
        print("Thanks for using TerminalSearch :)")
        input("Press any key to leave")


TerminalSearch()
