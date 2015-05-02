# ethan_tk
the game of Ethan, written in python using Tkinter

the rules of Ethan are as follows
- some N number of players begin with 5 points a piece
- players take turns in some arbitrary order of unwillingness rolling a two die
- if a player rolls a total of anything other than a four (1+3, 3+1, 2+2), add a chip to Ethan's pile
- if a player rolls a four, take all of the chips from Ethan's pile
- once a player is out of chips, he or she is out
- the game is over once all players are out of chips, or there is only one player remaining, and he or she just rolled the two die resulting in that player having more chips than Ethan's pile (namely, he or she rolled a 4 and got all of the chips, or he or she already had majority of the chips and rolled one more time).

Ethan eyes variant - same rules, except rolling a 2 (1+1) results in that player immediately losing all chips to Ethan. 

So what I have here is Ethan, written in Python, using built-ins like Tkinter. It was written as a Python exercise on night when I was bored. 
