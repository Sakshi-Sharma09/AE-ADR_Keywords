# OpenADR (AE & ADR Keyword Library)

OpenADR is a simple open-source Python keyword library for:

- Adverse Events (AE)
- Adverse Drug Reactions (ADR)

Designed for pharmacovigilance research, ADR mining, and biomedical NLP projects.

---

## 📦 Installation

### Option 1: Clone from GitHub

```bash
git clone (https://github.com/Sakshi-Sharma09/AE-ADR_Keywords)
cd openadr
```

### Option 2: Download ZIP

1. Click **Code → Download ZIP**
2. Extract the folder
3. Open in VS Code or any Python IDE

---

## 📂 Project Structure

```
openadr/
│
├── ae_terms.py        # Contains AE keyword list
├── adr_terms.py       # Contains ADR keyword list
├── README.md
├── .gitignore
```

---

## 🚀 Usage

Run Python inside the project folder:

```python
from ae_terms import get_ae_terms
from adr_terms import get_adr_terms

ae_terms = get_ae_terms()
adr_terms = get_adr_terms()

print(ae_terms)
print(adr_terms)
```

---

## 🔍 Example Use Case

You can integrate this library into:

- ADR text classification models
- Social media adverse event mining
- Pharmacovigilance signal detection projects
- NLP pipelines using spaCy or scikit-learn

---

## 🎯 Current Version

0.1.0

---

## 👩‍💻 Author

Sakshi Sharma  
PGD in AI/ML Healthcare + M. Pharma (Pharaceutics)
sakshisharma090199@gmail.com
---

## 📜 License

MIT License
