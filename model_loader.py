# model_loader.py

import pickle

MODEL_FILE = 'pipeline_v1.bin'

def load_model(filename: str = MODEL_FILE):
    """
    Loads a pickled model from a local file.
    
    Args:
        filename (str): The path to the pickled model file.
        
    Returns:
        The unpickled model object, or None if an error occurs.
    """
    print(f"Attempting to load model from '{filename}'...")
    try:
        # Open the file in binary read mode ('rb')
        with open(filename, 'rb') as f_in:
            # Load the object from the file
            model = pickle.load(f_in)
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print(f"Error: Model file '{filename}' not found.")
        print("Please ensure the model file is in the same directory as the scripts.")
        return None
    except (pickle.UnpicklingError, EOFError) as e:
        print(f"Error loading model from '{filename}': The file may be corrupted. {e}")
        return None

# You could add a small test here to ensure the loader works on its own
if __name__ == '__main__':
    print("Testing the model loader...")
    model = load_model()
    if model:
        print("Test successful. Model object type:", type(model))