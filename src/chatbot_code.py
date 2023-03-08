import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import warnings
import numpy as np
import tensorflow
from keras.models import load_model
import random
warnings.filterwarnings('ignore')

nltk.download("popular")

# Cargar el archivo intents.json
words = pickle.load(open("model/words.pkl", "rb"))
classes = pickle.load(open("model/classes.pkl", "rb"))
model = load_model("model/chatbot_model.h5")
data_file = open('Json/intents.json', encoding='utf-8').read() # lee el fichero de json
intents = json.loads(data_file) # carga el fichero de json

def clean_up_sentence(sentence):

  sentence_words = nltk.word_tokenize(sentence)
  sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]

  return sentence_words

def sentences(sentence, words, show_details=True):

  sentence_words = clean_up_sentence(sentence)

  bag = [0]*len(words) 

  for s in sentence_words:  
      for i,w in enumerate(words):
          if w == s: 
              bag[i] = 1
              if show_details:
                  print ("encontrado en la bolsas de palabras: %s" % w)
  return(np.array(bag))

def predict_class(sentence, model):

  p = sentences(sentence, words,show_details=False)
  res = model.predict(np.array([p]))[0]
  ERROR_THRESHOLD = 0.25

  results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
  results.sort(key=lambda x: x[1], reverse=True)

  return_list = []

  for r in results:
      return_list.append({"intent": classes[r[0]], "probability": str(r[1])})

  return return_list

def getResponse(ints, intents_json):

  tag = ints[0]['intent']
  list_of_intents = intents_json['intents']
  for i in list_of_intents:
      if(i['tag']== tag):
          result = random.choice(i['responses'])
          break
  return result

def chatbot_response(text): 
  ints = predict_class(text, model)
  res = getResponse(ints, intents)
  return res
