import math 

# Read in the file, split into the rules and updates sections
with open('data/day5.txt') as f:
    file = f.read()
    rules, updates = file.split("\n\n")

# Turn rules object into a long list of integer pairs
rules = rules.splitlines()
rules_parsed = [list(map(int, rule.split('|'))) for rule in rules]

# Turn updates into a long list of update arrays
updates = updates.splitlines()
updates_parsed = [list(map(int, update.split(','))) for update in updates]

# Function to try every rule for each update. If both entries exist in the update, then indexes must be in the right order. 
def rule_checker(ruleset, updateset): 
    outcome_list = []
    for update in updateset:
        outcome = True
        for rule in ruleset:
            if rule[0] in update:
                if rule[1] in update:
                    if update.index(rule[0]) > update.index(rule[1]):
                        outcome = False 
            else: 
                pass 
        outcome_list.append(outcome)
    return outcome_list

# Run the function, get a list of True/False values
checked = rule_checker(rules_parsed, updates_parsed)

# For all entries which are True, get the median entry value and add it to score.
score = 0 
for i in range(len(checked)):
    if checked[i] == True:
        use = math.floor(len(updates_parsed[i])/2)
        score += updates_parsed[i][use]

print("Part 1: " + str(score))