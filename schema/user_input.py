from pydantic import BaseModel,Field,computed_field,field_validator

from typing import List,Annotated,Literal

from config.city_tier import tier_1_cities,tier_2_cities

# Pydantic Class to validate data
class Customer(BaseModel):
    age: Annotated[int, Field(...,gt=0, description='Age of the customer',examples=[65])]
    weight: Annotated[float, Field(...,gt=0, description="Weight of Customer in KGs",examples=[70])]
    height: Annotated[float, Field(...,gt=0, description='Height of customer in Metres',examples=[1.7])]
    income_lpa: Annotated[float, Field(...,gt=0,description='Income of Customer in LPA',examples=[10])]
    smoker: Annotated[bool, Field(...,description='Does the customer smoke')]
    city: Annotated[str, Field(...,description='City where customer lives',examples=['Mumbai'])]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(...,description="Occupation of Customer")]


    @field_validator('city')
    @classmethod
    def normalize_city(cls,v: str) -> str:
        return v.strip().title()
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age <45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and (self.bmi > 30):
            return "high"
        elif self.smoker and (self.bmi > 27):
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def city_tier(self) -> int:
        
        if self.city in tier_1_cities:
            return 1
        if self.city in tier_2_cities:
            return 2
        return 3