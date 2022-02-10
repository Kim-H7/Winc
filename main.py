# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Part 1
Scorer_1 = "Ruud Gullit"
Scorer_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = (Scorer_1) + (' ') + str(goal_0) + ', ' + (Scorer_2) + (' ') + str(goal_1)
report = (Scorer_1) + ' scored in the '+ str(goal_0) +'nd minute\n' + (Scorer_2) + ' scored in the ' + str(goal_1) + 'th minute'
print(report)

#part 2
player = 'Ronald Koeman'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' ') + 1:])
name_short = player[0] + ('. ') + player[player.find(' ') + 1:]
chant = (first_name + '! ') * 5 + (first_name + '!')
good_chant = (chant[:-1] != (' '))
print (good_chant)