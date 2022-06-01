# ProtonDBchecker[BROKEN] 

## The Idea
So simple question - why we don't have the option to get the notification of problems or comments about state of the steam game to proton port? I mean there is a lot of games - sure, but why we can't choose one?

Steam API is very strange one - it shows you all kinds of things like:
- [x] Info About certain ID Number coresponed to program title
- [x] ProtonDB status for certain ID Number coresponded to program title
- [x] Game info for certain ... (you get the idea)

BUT there is one thing... There is NO list of games, but list of programs... and this is big hustle to work with. Why?
So the List of programs contains  
- [X] ID's (YAY)
- [x] Program title (YAY)

Into a programs they are counting
- games
- demos
- DLC
- Non public versions of projects
- ProtonDB 
- Tests

and without categorys it's a hustle to sort it because there is 130 000 programs at the moment. To check it all i need to call the API function to check INDIVIDUAL NUMBER, to get JSON request. So first you need to get list filter it and update twice a week (at least). 

## TODO
For now ProtonDBChecker can download WHOLE library and check what is game and what is not and collect it into seperate file.
- [x] writing to file
- [x] checking certain number
- [x] error handling
- [ ] log
- [ ] configuration file
- [ ] terminal CLI
- [ ] GUI version
