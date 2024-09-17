import spacy
from transformers import pipeline

# Load spaCy model
try:
    nlp_scispacy = spacy.load("en_core_web_md")
except OSError:
    print("Error: en_core_web_md model not found. Make sure it's installed or use a different model.")
    exit(1)

# Load BioBERT model
try:
    biobert = pipeline('ner', model="dmis-lab/biobert-base-cased-v1.1")
except Exception as e:
    print(f"Error loading BioBERT model: {e}")
    print("Ensure transformers and torch are installed.")  # Indentation corrected here
    exit(1)

# Extract entities from text using spaCy
try:
    with open("output.txt", 'r') as file:
        text = file.read()

    doc = nlp_scispacy(text)
    scispacy_entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['DRUG', 'DISEASE']]
except FileNotFoundError:
    print("Error: output.txt file not found.")
    exit(1)
except Exception as e:
    print(f"Error processing text with spaCy: {e}")
    exit(1)

# Extract entities using BioBERT
try:
    biobert_entities = biobert(text)
except Exception as e:
    print(f"Error processing text with BioBERT: {e}")
    biobert_entities = []

# Compare both models' outputs
print("SciSpacy Entities:", scispacy_entities)
print("BioBERT Entities:", biobert_entities)