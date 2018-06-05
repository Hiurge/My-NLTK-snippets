from nltk.corpus import words

correct_spellings = words.words()

def answer_nine(entries=['cormulent', 'incendenece', 'validrate']):
    
    correct_spellings = words.words()
    f = lambda x: x[0].lower()
    final=[]
    for j in entries:
        word = j
        first_letter=np.array(list(map(f,correct_spellings)))
        indx = np.where(first_letter==word[0])
        correct_spellings = np.asarray(correct_spellings)
        dictionary = correct_spellings[indx]

        set1 = set(nltk.ngrams(word,n=3))
        s=1
        for spelling in dictionary:
            set_ex = set(nltk.ngrams(spelling,n=3))
            if nltk.distance.jaccard_distance(set1,set_ex) < s:
                s=nltk.distance.jaccard_distance(set1,set_ex)
                answer = spelling
        final.append(answer)
    return final
    
answer_nine()

def answer_ten(entries=['cormulent', 'incendenece', 'validrate']):
    
    results = []
    for entry in entries:
        candidates = [w for w in correct_spellings if w[0] == entry[0]]
        results.append(min(candidates, key=
                           lambda candidate:nltk.jaccard_distance(set(nltk.ngrams(entry, n=4)), set(nltk.ngrams(candidate, n=4)))))
    return results
    
answer_ten()

def answer_eleven(entries=['cormulent', 'incendenece', 'validrate']):
    
    correct_spellings = words.words()
    f = lambda x: x[0].lower()
    final=[]
    for j in entries:
        word = j
        first_letter=np.array(list(map(f,correct_spellings)))
        indx = np.where(first_letter==word[0])
        correct_spellings = np.asarray(correct_spellings)
        dictionary = correct_spellings[indx]
        s=10
        for spelling in dictionary:
            if nltk.distance.edit_distance(word,spelling) < s:
                s=nltk.distance.edit_distance(word,spelling)
                answer = spelling
        final.append(answer)
    return final
    
answer_eleven()





# Part 2 - Spelling Recommender
# For this part of the assignment you will create three different spelling recommenders, that each take a list of misspelled words and recommends a correctly spelled word for every word in the list.
# For every misspelled word, the recommender should find find the word in correct_spellings that has the shortest distance*, and starts with the same letter as the misspelled word, and return that word as a recommendation.
# *Each of the three different recommenders will use a different distance measure (outlined below).
# Each of the recommenders should provide recommendations for the three default words provided: ['cormulent', 'incendenece', 'validrate'].
# Question 9
# For this recommender, your function should provide recommendations for the three default words provided above using the following distance metric:
# Jaccard distance on the trigrams of the two words.
# This function should return a list of length three: ['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].
# Question 10
# For this recommender, your function should provide recommendations for the three default words provided above using the following distance metric:
# Jaccard distance on the 4-grams of the two words.
# This function should return a list of length three: ['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].
# Question 11
# For this recommender, your function should provide recommendations for the three default words provided above using the following distance metric:
# Edit distance on the two words with transpositions.
# This function should return a list of length three: ['cormulent_reccomendation', 'incendenece_reccomendation', 'validrate_reccomendation'].