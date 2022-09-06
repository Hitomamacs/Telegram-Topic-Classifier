# Telegram-Topic-Classifier

## Why we are doing it?

In many telegram groups we found the necessity to classify different images in various subjects for exemple math, physics chemestry and many others so that after that we know the subject we can automatically tag people expert in that topic hence helping more people and in a more eficcient manner.

## How we are doing it

The project is composed of mainly 3 parts

1. Collect the necessary data
2. Preprocess the data and write a model that can predicts the classes
3. Write the telegram bot that automatically classifies images and then depending on the subject tags all the experts
---
I will now briefly explain all the parts.

### 1)

For the dataset we are using all the images sent in over 2 years in the telegram group [Best Group ever](https://t.me/helpmatematica) that is composed of more than 2000 images. We used telegram user Apis to fetch all of this data. We then performed OCR on all the images and extracted the text information using [Google OCR for python](https://pypi.org/project/pytesseract/). Now the hard task was to label all of the dataset for doing that we leveraged the enormous amount of people found in our [Group Network](https://t.me/gabryphysics). We wrote a simple but effective telegram bot that sends an image and then asks to press a button corresponding to the subject of that particular image. We kinda used a **mutex_lock/unlock** so that all the people recived different images and that we could minimize the number of images labeled multiple times, you can learn more by looking at the code.

### 2)
**Preprocessing:**
We exported the DB as a pickle object so we could work with it easily. First we performed some exploratory data analysis to learn more about the distribution of the dataset. We discarded 5 of the 8 classes because we didn't have enough data about them. We prepocessed the data by removing all of the punctuation and stopwords and then we tokenized the sentences.
**Model:**
We encoded the classes using label encoding anothe approach is possible using one-hot vector encoding. The sentences are transformed in numbers using the bag-of-word technic but it is also possible and maybe reccomended to use word2vec. We tried different model like NN, logistic regression, support vector machines and Naive Bayes. The best result for now is 86% of accuracy but there is margin of improvement .

### 3) 
We modify a version of [Emanuele beautiful poke bot](https://github.com/emanuelelaface/poke-bot) so that the bot perform the actions in the seguent order. When a photo is recived it extract the text using google ocr we then perform inference using the preferred model and then the bot tags all of the scientis corresponfing to that subject.

If you have any suggestion or question feel free to write me! <3
