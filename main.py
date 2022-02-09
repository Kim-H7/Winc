# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Part 1
Scorer_1 = "Ruud Gullit"
Scorer_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = (Scorer_1) + (' ') + str(goal_0), (Scorer_2) + (' ') + str(goal_1)
Report = (Scorer_1) +' scored in the '+ str(goal_0) +'nd minute', (Scorer_2) + ' scored in the '+ str(goal_1)+ 'th minute'

#part 2
player = 'Ronald Koeman'
first_name = player.find('Ronald'), player[:6]
last_name_len = player.find('Koeman'), len(player[7:]), player[7:]
name_short = player[0] + player[7:]
chant = (player[:6] + '! ') * 2 + (player[:6] + '!')
good_chant = (2 != 3)

"""Ik kom niet door de check van wincpy heen omdat er nog ' ' om de strings heen staan in het resultaat van lijn 12. Ik heb lang gezocht
en geprobeerd maar ik kom er niet goed uit. Is daar een manier voor? In ieder geval alvast bedankt voor de feedback!"""