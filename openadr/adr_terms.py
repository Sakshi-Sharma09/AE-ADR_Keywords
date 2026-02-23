"""
OpenADR - Adverse Drug Reaction Terms
"""

ADR_TERMS = {
    "hepatotoxicity",
    "nephrotoxicity",
    "cardiotoxicity",
    "anaphylaxis",
    "angioedema",
    "thrombocytopenia",
    "leukopenia",
    "hyperglycemia",
    "hypoglycemia",
    "pancreatitis",
    "Stevens-Johnson syndrome",
    "QT prolongation"
}

def get_adr_terms():
    """Return all ADR terms"""
    return ADR_TERMS