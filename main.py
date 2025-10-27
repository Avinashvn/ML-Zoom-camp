from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import load_model

# Initialize app and load the model once on startup
app = FastAPI()
model = load_model()

# Define the structure of the request body
class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# Define the prediction endpoint
@app.post("/predict")
def predict_conversion(lead: Lead):
    # Convert input data to a dictionary and wrap it in a list
    input_data = [lead.model_dump()]
    
    # Get the prediction
    probability = model.predict_proba(input_data)[0, 1]
    
    # Return only the essential result
    return {"conversion_probability": probability}