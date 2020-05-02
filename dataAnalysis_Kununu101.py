import string
import csv
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize, Cistem, Counter
from nltk.corpus import stopwords
#"C:\Users\Admin\PycharmProjects\webScraperReviews\venv\Master_Data_Milestone1.csv"
review=' '
with open('Master_Data_Milestone1.csv') as kununu_file:
    csv_data_raw=csv.reader(kununu_file, delimiter='|')
    row_count=0
    for row in csv_data_raw:
        if row_count == 0:
            print(f'Column names are {", ".join(row)}')
            row_count += 1
        else:
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            row_count += 1
            review=review+row[15]
print(row_count)
#review =csv_data_raw                  #'Guter Arbeitgeber mit Problemen in der FÃ¼hrungsriege Je nach Bereich ist es eine gute AtmosphÃ¤re. Innerhalb der Teams gibt es meist eine gute Stimmung und auch privat unternimmt man gerne mal etwas gemeinsam.Leider tragen manche Vorgesetzte und HR zu einer Verschlechterung der ArbeitsatmosphÃ¤re bei.(teilweise) Beispiele dazu:- Starker Unterschied in der FÃ¼hrungsriege. Die meisten Vorgesetzten wissen wie man Mitarbeiter fÃ¼hrt und motiviert. Doch gibt es einige Beispiele In meinem Team ist der Zusammenhalt sehr gut. Wir unternehmen auch privat etwas gemeinsam.Aber das hÃ¤ngt tatsÃ¤chlich sehr von dem Bereich und dem Team abAus meiner Sicht vorhanden und gut umgesetzt. Es ist egal wer Du bist Der Altersdurchschnitt im Office ist recht jung. Bislang habe ich aber keine negativen Auswirkungen durch ein hÃ¶heres Alter mitbekommen. Umweltbewusstsein kÃ¶nnte ein wenig besser sein'

text = open('germanWordList', encoding='utf-8').read()
#print(text)

lower_case=review.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
tokenized_words = word_tokenize(cleaned_text,"german")
#print(len((tokenized_words)))

final_words=[]
removed_words=[]
stemmer = Cistem()
stemmed_words=[]
for word in tokenized_words:
    if word not in stopwords.words('german'):
        final_words.append(word)
        stemmed_words.append(stemmer.stem(word))
    else:
        removed_words.append((word))
#print("stemmed_words: " , stemmed_words)
#print ("final_words: ", final_words)
#print ((removed_words))

emotion_list=[]
stemmed_WordList=[]
count = 0
stemmed_Dict={}
with open('germanWordList', 'r') as file:
    for line in file:
        #Remove spaces, and punctuations
        #replace spaces with nothing
        clear_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()
        wordList, emotion = clear_line.split(':')
        #print("Word :" + word + " "+ "Emotion :" + emotion)
        stemmed_WordList.append(stemmer.stem(wordList))
        #print("stemmed_WordList :" + stemmed_WordList[count] + " " + "Emotion :" + emotion)
        stemmed_Dict[stemmed_WordList[count]]=emotion
        count = count + 1
print(stemmed_Dict)

# Iterating through Stemmed words which we got from Reviews
for stemmed_word in stemmed_words:
    # Iterating through the stemmed words from germanwordList file
    print(stemmed_word)
    for stemmedDictWords in stemmed_Dict:
        if(stemmed_word == stemmedDictWords):
            print('word from review is :',stemmed_word,'And its stemmed word from file is :',stemmedDictWords,'Which contains emotion: ',stemmed_Dict[stemmed_word])
            emotion_list.append(stemmed_Dict[stemmed_word])
print(emotion_list)
w = Counter(emotion_list)
print(w)