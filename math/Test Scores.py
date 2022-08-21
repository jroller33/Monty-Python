print("The Test Scores program:")
print("Enter 3 test scores \n")
total_score =0      #start the variable to accumulate scores
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))

average_score = round(total_score / 3)

print()
print(f"Total Score: {total_score} \n Average Score: {average_score}")
