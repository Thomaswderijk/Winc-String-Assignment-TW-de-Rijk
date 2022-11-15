# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

'''
String assignment
'''

#Define the variables of the scoring footballers
scorer_name_1 = 'Ruud Gullit'
scorer_name_2 = 'Marco van Basten'

#Define the variables of the minutes in which goals were scored
goal_0 = 32
goal_1 = 54

#Scorers and goal minutes stringed together
scorers = scorer_name_1 + " " + str(goal_0) + ", " + scorer_name_2 + " " + str(goal_1)

#Scoring report
report = f'{scorer_name_1} scored in the {goal_0}nd minute\n{scorer_name_2} scored in the {goal_1}th minute'

#Indexing and slicing a player name
player = 'Joop Hiele'
first_name = player[player.find('Joop'):len('Joop')]
last_name_len = len(player[player.find('Hiele'):])
name_short = player[0] + ". " + player[player.find('Hiele'):]

#Making a chant string
chant = (first_name + "! ") * (len(first_name) - 1) + first_name + "!"

#Check end of the chant string
good_chant = chant[-1] != " "