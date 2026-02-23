"""
OpenADR - Adverse Event Terms
Free public biomedical lexicon
"""

AE_TERMS = {
    "headache",
    "nausea",
    "vomiting",
    "rash",
    "dizziness",
    "fatigue",
    "itching",
    "fever",
    "pain",
    "diarrhea",
    "constipation",
    "cough",
    "insomnia",
    "anxiety",
    "depression"
}

def get_ae_terms():
    """Return all AE terms"""
    return AE_TERMS