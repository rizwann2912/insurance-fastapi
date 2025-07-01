import pickle,os
from typing import List,Annotated,Literal
import pandas as pd


def load_model(file_path):
    with open(file_path,'rb') as f:
        model =pickle.load(f)
    return model

model = load_model('model/model.pkl')
class_labels =model.classes_.tolist()

def predict_output(user_input:dict):
    df = pd.DataFrame(user_input)

    prediction = model.predict(df)[0]

    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    # Create mapping
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probabilities)))
    return {
        "response": {
            "predicted_category": prediction,
            "confidence": round(confidence, 4),
            "class_probabilities": class_probs
        }
    }