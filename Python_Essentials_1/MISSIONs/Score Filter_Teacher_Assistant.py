
def main():
    #Define the raw list of exam scores
    raw_scores = [85, -10, 59, 60, 92, -3, 74, 45, 100]

    #Initialize an empty list to collect valid passing scores
    passing_scores = []

    #Loop through each individual score in raw_scores
    for score in raw_scores:
        #Check whether the score is 60 or above
        if score >= 60:
            #Append qualifying scores to passing_scores
            passing_scores.append(score)

    #Display the filtered results
    print("Passing scores:", passing_scores)

if __name__ == "__main__":
    main()
