import pandas as pd
import numpy as np
import gc
import os

labeled_reviews = pd.DataFrame(columns=["text", "label"])
# labeled_reviews = pd.read_csv("labeled_reviews3.csv")
id2label = {0: "None", 1: "Other", 2: "Incorrect size", 3: "Lack of instructions"}
# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# enter the path of the csv table down below
table_path = "reviews_with_sentiment.csv"
data_reviews = pd.read_csv(table_path)
for i in range(len(data_reviews)): 
    clear_screen()
    designer_review_translation = data_reviews["translated_text"][i]
    designer_review = data_reviews["text"][i]
    print(f"{i} / {len(data_reviews)}")
    print("Review Translation:", data_reviews["translated_text"][i])
    print("_" * 50)
    print("Original Review:", data_reviews["text"][i])
    print("—" * 50)
    # Input the label
    try:
        label_id = int(input("Enter the label ID (0: None, 1: Other, 2: Incorrect size, 3: Lack of instructions): "))
        while label_id not in id2label:
            print("Invalid label ID. Please enter a valid label ID.")
            label_id = int(input("Enter the label ID (0: None, 1: Other, 2: Incorrect size, 3: Lack of instructions): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Append to DataFrame
    new_entry = pd.DataFrame({
        "text": [data_reviews["translated_text"][i]],
        "label": [label_id]
    })
    labeled_reviews = pd.concat([labeled_reviews, new_entry], ignore_index=True)

    # Save the labeled reviews to a new CSV file
    labeled_reviews.to_csv("labeled_reviews_en.csv", index=False)
    
print("Labeling completed. Labeled data saved to 'labeled_reviews3.csv'.")