from pydantic import BaseModel,Field
from typing import Annotated,Dict,List

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description='The predicted insurance premium category',
        example='High'
    )
    confidence: float = Field(
        ...,
        description="Model's confidence score for the predicted class",
        example=0.8272
    )
    class_probabilities : Dict[str,float] = Field(
        ...,
        description='Probability distribution across all possible classes',
        example = {"Low":0.02,"Medium":0.34,"High":0.64}
    )