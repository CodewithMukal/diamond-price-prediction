# DIAMOND PRICE PREDICTOR

I made this to get 2 credits for my course, it was fun though, will learn more stuff.


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Train the Models

Open the Jupyter notebook ```notebooks/model.ipynb``` and execute **all cells** to preprocess the dataset, train the models, and generate the serialized model files (`.pkl`).

### 6. Run the Prediction Script

```bash
python main.py
```

### 7. Enter Diamond Features

When prompted, provide the required diamond attributes such as:

- Carat
- Cut
- Color
- Clarity
- Depth
- Table
- x
- y
- z

### 8. View Predictions

The script will output the predicted diamond price using all three trained models:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
