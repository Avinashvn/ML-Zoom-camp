# score_lead.py (Corrected Version)

# We no longer need pandas for the prediction part!
# from model_loader import load_model
from model_loader import load_model

def get_prediction(model, record: dict) -> float:
    """
    Scores a single record using the provided model.
    The model's first step (DictVectorizer) expects a list of dicts.
    """
    # The model expects a list of dictionaries as input, not a DataFrame.
    # We simply wrap our single record dictionary in a list.
    input_data = [record]
    
    # Use predict_proba to get the probability of conversion (class 1)
    probability = model.predict_proba(input_data)[0, 1]
    
    return probability

def main():
    """
    Main execution function.
    """
    # The record to be scored
    client_record = {
        "lead_source": "paid_ads",
        "number_of_courses_viewed": 2,
        "annual_income": 79276.0
    }
    
    # 1. Use the imported function to load the model
    model = load_model()

    # 2. Check if the model was loaded successfully before proceeding
    if model is None:
        print("Exiting due to model loading failure.")
        return

    # 3. Use the loaded model to score the record with the corrected input format
    conversion_probability = get_prediction(model, client_record)
    
    # 4. Display the final result
    print("\n--- Scoring Result ---")
    print(f"Input record: {client_record}")
    print(f"Predicted probability of conversion: {conversion_probability:.4f}")
    
    decision_threshold = 0.5
    decision = "Convert" if conversion_probability >= decision_threshold else "Don't Convert"
    print(f"Decision (at {decision_threshold} threshold): {decision}")
    print("----------------------")


if __name__ == "__main__":
    main()