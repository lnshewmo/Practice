# printing using PRINT()
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

# printing using f string
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"You received {my_votes / total_votes * 100}% of the total votes.")

# printing dictionary using PRINT()
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,voters in counties_dict.items(): # defines variables
    print((county) + " county has " + str(voters) + " registered voters.")  

# printing dictionary using fstring
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,voters in counties_dict.items(): # defines variables
    print(f"{county} county has {voters} registered voters.")

# multiline f strings
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("How many total votes in the election"))
message_to_candidate = (
    f"You received {candidate_votes} votes. "
    f"There were {total_votes} total votes. "
    f"You received {candidate_votes/total_votes * 100}% of the total votes.") 
print(message_to_candidate)

# same code but formatting the percentage (floating point decimal)
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("How many total votes in the election"))
message_to_candidate = (
    f"You received {candidate_votes} votes. "
    f"There were {total_votes} total votes. "
    f"You received {candidate_votes/total_votes * 100:.2f}% of the total votes.") 
print(message_to_candidate)

# skill drill 3.2.11a
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,voters in counties_dict.items(): # defines variables
    print(f"{county} county has {voters} registered voters.")

# skill drill 3.2.11b
# IDK why but this wouldn't print until I changed the " in the dictionary key to ' for f-string line
# however changing the double to single quotes in the first line of the dictionary doesn't matter
voting_data = [{'county':'Arapahoe', 'registered voters': 422829},
                {"county":"Denver", "registered voters": 463353}, 
                {"county":"Jefferson", "registered voters": 432438}]
for counties_dict in voting_data:
    print(f"{counties_dict['county']} county has {counties_dict['registered voters']} registered voters.") 

