#!/usr/local/bin/python

import random

guesses = {"5616185650518293" : 2,
           "3847439647293047" : 1,
           "5855462940810587" : 3,
           "9742855507068353" : 3,
           "4296849643607543" : 3,
           "3174248439465858" : 1,
           "4513559094146117" : 2,
           "7890971548908067" : 3,
           "8157356344118483" : 1,
           "2615250744386899" : 2,
           "8690095851526254" : 3,
           "6375711915077050" : 1,
           "6913859173121360" : 1,
           "6442889055042768" : 2,
           "2321386104303845" : 0,
           "2326509471271448" : 2,
           "5251583379644322" : 2,
           "1748270476758276" : 3,
           "4895722652190306" : 1,
           "3041631117224635" : 3,
           "1841236454324589" : 3,
           "2659862637316867" : 2}


# How many strings will be produced in a new generation?
GENERATION_SIZE = 32

# How many will survive to produce the next generation?
FITTEST = 16

# How likely are mutations? A mutation occurs when randint(0, MUTATION_RATE)
# returns zero.
MUTATION_RATE = 5

# Initialise teh random.
rnd = random.SystemRandom()

# Remember good guesses, we'll use them when re-initialising the breeding pool.
goodSeeds = set()


# Initialise the breeding pool. Half the pool will be strings that produced
# good answers. The other half will be new random numbers. If we don't have
# many good numbers yet then create at least eight new numbers.
def init(answers):
    s = ""
    num = len(goodSeeds)
    if num < 8:
        num = 8
        
    for j in range(0, num):
        s = ""
        for i in range(0, 16):
            x = rnd.randint(0, 9)
            s += str(x)
        answers.append(s)
        
    for s in goodSeeds:
        answers.append(s)


# The score is how many of the 22 constraints are met.
def scoreAnswers(answers):
    scores = []
    for answer in answers:
        answerScore = 0
        for guess in guesses:
            matches = 0
            guessScore = guesses[guess]
            for i in range(0, len(guess)):
                if answer[i] == guess[i]:
                    matches += 1
            if matches == guessScore:
                answerScore += 1
        scores.append(answerScore)
    return scores


# Return the 16 best strings, and their scores.
def fittest(answers, scores):
    bestAnswers = [""] * FITTEST
    bestScores = [0] * FITTEST
    worstBestScore = 0
    
    i = 0
    for score in scores:
        if score > worstBestScore:
            newWorst = 99
            for j in range(0, len(bestScores)):
                if bestScores[j] == worstBestScore:
                    bestScores[j] = score
                    bestAnswers[j] = answers[i]
                if bestScores[j] < newWorst:
                    newWorst = bestScores[j]
            worstBestScore = newWorst
        i += 1
    return bestAnswers, bestScores
        

# Create the next generation. Build a string of the correct length by randomly
# picking a number from the appropriate column of one of the breeding stock.
# Occasionally mutate one of the digits to some random value.
def nextGeneration(bestAnswers):
    answers = []
    for i in range(0, GENERATION_SIZE):
        s = ""
        for i in range(0, 16):
            m = rnd.randint(0, MUTATION_RATE)
            if m == 0:
                s += str(rnd.randint(0, 9))
            else :
                x = rnd.randint(0, len(bestAnswers) - 1)
                s += bestAnswers[x][i]
        assert(len(s) == 16)
        answers.append(s)
    return answers


# If all the answers are the same we are inbred.
def answersInbred(answers):
    s = answers[0]
    inbred = True
    for answer in answers:
        if not answer == s:
            inbred = False
            break
    return inbred


# Create some initial seeds and start breeding candidate answers.
def main():

    hiScore = 0
    answers = []
    init(answers)

    # Keep going until we satisfy all the criteria.
    while hiScore < len(guesses):
        scores = scoreAnswers(answers)
        bestAnswers, bestScores = fittest(answers, scores)
        if hiScore < bestScores[0]:
            hiScore = bestScores[0]

            # On beating the high score discard the set of good seeds. This is
            # because we don't want to remember strings that are good for
            # matching low scores. Once we are close to the target we stop
            # discarding based on the assumption that 'nearly-there' strings
            # are promising. 
            if hiScore < 20:
                goodSeeds.clear()
            print
            print hiScore, bestAnswers

        # Add strings that match the high score to the good seed list.
        if hiScore == bestScores[0]:
            x = len(goodSeeds)
            goodSeeds.add(bestAnswers[0])
            if not len(goodSeeds) == x:
                print len(goodSeeds),

        # And so it continues...   
        answers = nextGeneration(bestAnswers)

        # We're inbred - better start again with some new breeding stock.
        if answersInbred(answers):
            answers = []
            init(answers)
    

main()
