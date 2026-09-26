# NutriMind AI: Intelligent Metabolic Diagnostics & Context-Aware Diet Planner 🥦🤖

NutriMind AI is a comprehensive, production-ready health optimization engine built with **Streamlit** and **Retrieval-Augmented Generation (RAG)**. The platform runs algorithmic metabolic assessments, builds custom daily macro blueprints, and houses an advanced domain-specific chatbot that queries an internal scientific knowledge base to eliminate AI hallucinations.

⚠️ **Medical Disclaimer:** *This software architecture is designed strictly for consumer wellness tracking and academic demonstration. It does not constitute medical software, clinical diagnostics, or official therapeutic dietary prescription.*

---

## ⚡ Core Architecture Features

### 🩺 Algorithmic Biometric Analytics
The system ingests basic human biometrics to instantaneously evaluate standard body metrics:
*   **Mass Evaluation:** Evaluates height-to-weight ratios via standard Body Mass Index (BMI).
*   **Basal Energy Computation:** Deploys the *Mifflin-St Jeor* standard to quantify baseline caloric needs at absolute rest.
*   **Active Energy Scaling:** Applies precise physical exertion coefficient multipliers to determine total daily expenditure.
*   **Goal-Oriented Adjustments:** Calculates specific metabolic target numbers tailored to standard fitness objectives.

### 🍱 Dynamic 24-Hour Macro & Meal Architect
Generates an explicit, custom-tailored day-long dietary framework mapped across five key intervals:
*   **Phased Eating Schedule:** Breakfast, Mid-Morning Fuel, Lunch, Evening Fuel, and Dinner.
*   **Granular Metrics:** Generates exact item titles, serving portions, caloric values, and explicit protein content.
*   **Restriction Profiles:** Filters meals based on user objectives, dietary choices (e.g., Vegetarian, Vegan), and medical allergen constraints.

### 💬 Verified Knowledge Base Chatbot
An internal assistant capable of navigating nuanced inquiries regarding ingredient optimization, macro sourcing, and general body maintenance. The backend leverages local vector lookups to anchor language model responses strictly to verified research materials.

---

## 📐 Computational Matrix

### Basal Metabolic Rate (BMR)
Calculations are processed via the **Mifflin-St Jeor Mathematical Model**:
\[\text{BMR (Male)} = (10 \times \text{weight in kg}) + (6.25 \times \text{height in cm}) - (5 \times \text{age in years}) + 5\]
\[\text{BMR (Female)} = (10 \times \text{weight in kg}) + (6.25 \times \text{height in cm}) - (5 \times \text{age in years}) - 161\]

### Total Daily Energy Expenditure (TDEE)
\[\text{TDEE} = \text{BMR} \times \text{Activity Coefficient}\]

---

## 🛠️ Data Infrastructure & Pipeline Workflow

The cognitive intelligence module routes vector queries through an optimized local document retrieval pipeline:

\[\text{[Source PDF Document]} \longrightarrow \text{[Text Chunking Engine]} \longrightarrow \text{[Vector Embedding Generation]} \longrightarrow \text{[FAISS Index Storage]} \longrightarrow \text{[Semantic Search Retrieval]} \longrightarrow \text{[System Prompt Injection]} \longrightarrow \text{[Deterministic LLM Output]}\]

*   **Ingestion Strategy:** Raw literature (`nutrition.pdf`) is converted into dense semantic indexes locally.
*   **Storage Optimization:** The generated FAISS database vector arrays are maintained locally outside version control and can be generated dynamically at any time.

---

## 📂 System File Blueprint

```text
ai_health_assistant_project/
│
├── app.py                # Main Streamlit orchestration file and user portal
├── diet.py               # Algorithmic engine handling meal configuration logic
├── rag.py                # Semantic text index query interface and embedding manager
├── create_database.py    # Builds and maps the local vector repository from raw text
├── llm_test.py           # Testing utility to evaluate API response parameters
├── prompt.md             # Core system instructions defining AI behaviors
├── requirements.txt      # Master list of Python dependency packages
├── .gitignore            # Excludes environment configurations and vector indexes
│
├── data/
│   └── nutrition.pdf     # Primary source literature for chatbot grounding
│
└── vector_db/            # Generated locally (Holds binary index files like .faiss and .pkl)
```

---

## 💻 Under the Hood (Tech Stack)

*   **Application Framework:** Streamlit Core
*   **Vector Query Core:** Meta FAISS (Facebook AI Similarity Search)
*   **Language Models & Models:** Hugging Face Transformer Architectures & LLM Endpoint Integrations
*   **Language Environment:** Python 3.x
*   **Configuration Manager:** python-dotenv

---

## 🚀 Execution & Deployment

### 1. Environment Setup
Install required system components from the project directory:
```bash
pip install -r requirements.txt
```

### 2. Knowledge Index Generation
Populate the `data/` subdirectory with your target document saved as `nutrition.pdf`, then execute the indexing pipeline:
```bash
python create_database.py
```

### 3. Initialize Interface
Boot up the Streamlit interface application locally:
```bash
streamlit run app.py
```
