import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


def create_sample_data():
    """Sample product review database"""
    data = {
        'text': [
            # Positive product reviews (15)
            "This smartphone exceeded all my expectations, amazing battery life!",
            "The image quality on this TV is crystal clear, worth every penny",
            "Perfect fit! These headphones are incredibly comfortable for long sessions",
            "The laptop's processing speed is impressive, handles all my tasks smoothly",
            "This coffee maker brews the perfect cup every single morning",
            "The wireless charger works flawlessly with all my devices",
            "Excellent build quality, this keyboard feels premium and types beautifully",
            "The camera's low-light performance is outstanding, captures great photos",
            "This fitness tracker accurately monitors all my activities",
            "The bluetooth speaker has amazing sound quality and great bass",
            "This gaming mouse has perfect precision and feels great in hand",
            "The air purifier has significantly improved our home's air quality",
            "Super fast delivery and the product works exactly as advertised",
            "The water filter removes all impurities, water tastes much better now",
            "This microwave heats evenly and has useful preset functions",

            # Negative product reviews (15)
            "The smartphone keeps freezing, terrible user experience",
            "This TV's colors are washed out, definitely not worth the price",
            "These headphones hurt my ears and the sound quality is poor",
            "Laptop runs too hot and the battery dies within 2 hours",
            "The coffee maker leaked after just two weeks of use",
            "Wireless charger is unreliable, keeps disconnecting randomly",
            "Keys started sticking on this keyboard after a month",
            "Camera focus is very slow and photos turn out blurry",
            "Fitness tracker shows inaccurate step counts, waste of money",
            "Speaker started crackling after few weeks of normal use",
            "The mouse buttons broke within first month of purchase",
            "Air purifier is too loud and doesn't seem to do anything",
            "Product arrived damaged and customer service was unhelpful",
            "Water filter started making strange noises and stopped working",
            "This microwave's buttons stopped working after two months"
        ],
        'sentiment': [
            # 15 positive sentiments
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            # 15 negative sentiments
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
    }
    return pd.DataFrame(data)


def analyze_sentiment(text, vectorizer, model):
    """Predict sentiment for new text"""
    # Transform the text into vectors
    text_vectorized = vectorizer.transform([text])
    # Predict sentiment
    prediction = model.predict(text_vectorized)
    sentiment = "Positive" if prediction[0] == 1 else "Negative"
    return sentiment


# Create and load the sample data
df = create_sample_data()
print("Sample data created!")

# Split the data into features (X) and target (y)
X = df['text']
y = df['sentiment']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nData split into training and testing sets")

# Create a vectorizer to convert text to numbers
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
print("\nText converted to numerical format")

# Create and train the model
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)
print("\nModel trained!")

# Make predictions on test data
predictions = model.predict(X_test_vectorized)

# Print accuracy and classification report
print("\nModel Accuracy:", accuracy_score(y_test, predictions))
print("\nDetailed Classification Report:")
print(classification_report(y_test, predictions))

# Requests simple sentences from user to test against
example_texts = []
while True:
    try:  # ensures a number is provided
        attempts = int(input('Number of product reviews to analyse: '))
        break
    except ValueError:
        print('Kindly enter a valid number')

for i in range(attempts):  # adds requested number of sentences into example_texts list
    text = input('Enter your product review: ')
    example_texts.append(text)

# Final output
print("\nAnalyzing product reviews:")
for text in example_texts:
    sentiment = analyze_sentiment(text, vectorizer, model)
    print(f"Review: '{text}'")
    print(f"Sentiment: {sentiment}\n")