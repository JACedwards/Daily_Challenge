
# In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition.
# The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

# Given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

# Return a string of all teams sorted by the ranking system.


# Example 1:
# Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
# Output: "ACB"
# Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
# Team B was ranked second by 2 voters and was ranked third by 3 voters.
# Team C was ranked second by 3 voters and was ranked third by 2 voters.
# As most of the voters ranked C second, team C is the second team and team B is the third.

# Example 2:
# Input: votes = ["WXYZ","XYZW"]
  #place dictionaries:
  #first = {'W': 1, 'X': 1, 'Y':0, 'Z':0}
# Output: "XWYZ"
# Explanation: X is the winner due to tie-breaking rule. X has same votes as W for the first position but X has one vote as second position while W doesn't have any votes as second position. 

# Example 3:
# Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
# Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
# Explanation: Only one voter so his votes are used for the ranking.
# Constraints:
# 1 <= votes.length <= 1000
# 1 <= votes[i].length <= 26
# votes[i].length == votes[j].length for 0 <= i, j < votes.length.
# votes[i][j] is an English uppercase letter.
# All characters of votes[i] are unique.
# All the characters that occur in votes[0] also occur in votes[j] where 1 <= j < votes.length.

#Psuedo:
  # dictionaries for number of votes per group
    #looping through items in list, checking
      # first place e = s[0]:
        #A. keep count of all three group occurances
          #B. create first place dictionary when done
              #keys = team letter : value = counts
      # second place = s[1]
        #repeat A and B
      # third place = s[2]
        #repeat A and B
    
####<><><>####

#####This one works only for "ABC" example because A, B, C are hard-coded in###
  #Need to refactor to account for different letters and different lengths/numbers of groups###
  #also doesn't account for tied scores

# Input: votes = ["WXYZ","XYZW"]
#Psuedo 2:
#

#Hardcoded version works only for ABC example  
def rankChoiceVoting(votes):

  a_count = 0
  b_count = 0
  c_count = 0

  first_place = {}
  second_place = {}
  third_place = {}

  #first_place dictionary
  for vote in votes:
    if vote[0] == "A":
      a_count +=1
    elif vote[0] == "B":
      b_count +=1
    else:
      c_count +=1

  first_place['A'] = a_count
  first_place['B'] = b_count
  first_place['C'] = c_count

  a_count = 0
  b_count = 0
  c_count = 0
  
  #second_place dictionary
  for vote in votes:
    if vote[1] == "A":
      a_count +=1
    elif vote[1] == "B":
      b_count +=1
    else:
      c_count +=1

  second_place['A'] = a_count
  second_place['B'] = b_count
  second_place['C'] = c_count

  a_count = 0
  b_count = 0
  c_count = 0

  #third_place dictionary
  for vote in votes:
    if vote[2] == "A":
      a_count +=1
    elif vote[2] == "B":
      b_count +=1
    else:
      c_count +=1

  third_place['A'] = a_count
  third_place['B'] = b_count
  third_place['C'] = c_count

  print(first_place)
  print(second_place)
  print(third_place)

  srt_scores = []
  tot_scores_all = {}

  tot_score_a = (first_place.get('A') * 3) + (second_place.get('A') * 2) + (third_place.get('A') * 1)
  srt_scores.append(tot_score_a)
  tot_scores_all['A'] = tot_score_a

  tot_score_b = (first_place.get('B') * 3) + (second_place.get('B') * 2) + (third_place.get('B') * 1)
  srt_scores.append(tot_score_b)
  tot_scores_all['B'] = tot_score_b

  tot_score_c = (first_place.get('C') * 3) + (second_place.get('C') * 2) + (third_place.get('C') * 1)
  srt_scores.append(tot_score_c)
  tot_scores_all['C'] = tot_score_c
  print(tot_scores_all)

  srt_scores.sort(reverse=True)
  print(srt_scores)

  output = ''
  for s in srt_scores:
    for k, v in tot_scores_all.items():
      if s == v:
        output = f"{output}{k}"
  return output


print(rankChoiceVoting(["ABC","ACB","BAC","BCB","ACB"]))