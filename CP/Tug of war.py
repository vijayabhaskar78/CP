def tug_of_war(weights):
    # Sort the weights in descending order to handle larger elements first
    weights.sort(reverse=True)
    
    team1_weight = 0
    team2_weight = 0
    
    # Alternate between team1 and team2 to balance the weights
    for weight in weights:
        if team1_weight < team2_weight:
            team1_weight += weight
        else:
            team2_weight += weight
    
    # Return the smaller and larger of the two team weights
    return min(team1_weight, team2_weight), max(team1_weight, team2_weight)

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())  # Read the number of weights
    weights = [int(input()) for _ in range(n)]  # Read the weights
    team1, team2 = tug_of_war(weights)  # Find the optimal partition
    print(f"{team1} {team2}")
    if _ < t - 1: print()  # Print a blank line between test case outputs