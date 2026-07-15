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

<hr/>

| Model | MAE | RMSE | Train R² | Test R² |
|-------|------:|------:|---------:|---------:|
| **Linear Regression (LR)** | 731.98 | 1099.30 | 0.9195 | 0.9226 |
| **Decision Tree (DT)** | 2.65 | 33.60 | 0.999992 | 0.999954 |
| **Random Forest (RF)** | 3.12 | 26.72 | 0.999992 | 0.999954 |

## Model Performance Analysis

### Linear Regression (LR)
- **Mean Absolute Error (MAE):** 731.98
- **Root Mean Square Error (RMSE):** 1099.30
- **Train R² Score:** 0.9195
- **Test R² Score:** 0.9226

Linear Regression provides a good baseline model, explaining approximately **92.26%** of the variance in diamond prices. However, its relatively high MAE and RMSE indicate that it cannot fully capture the complex, nonlinear relationships present in the dataset.

### Decision Tree (DT)
- **Mean Absolute Error (MAE):** 2.65
- **Root Mean Square Error (RMSE):** 33.60
- **Train R² Score:** 0.999992
- **Test R² Score:** 0.999954

The Decision Tree model performs significantly better than Linear Regression, achieving an almost perfect R² score. Its very low prediction errors demonstrate its ability to model nonlinear relationships effectively.

### Random Forest (RF)
- **Mean Absolute Error (MAE):** 3.12
- **Root Mean Square Error (RMSE):** 26.72
- **Train R² Score:** 0.999992
- **Test R² Score:** 0.999954

Random Forest achieves the best overall performance. Although its MAE is slightly higher than that of the Decision Tree, it has the **lowest RMSE**, indicating fewer large prediction errors. Its nearly identical train and test R² scores also suggest excellent generalization on unseen data.

<hr/>

### Residual Plots

1. Linear Regression
<img width="581" height="546" alt="image" src="https://github.com/user-attachments/assets/957cf40d-ac7b-4079-8776-3aabdfcd97e9" />

2. Decision Tree
<img width="553" height="546" alt="image" src="https://github.com/user-attachments/assets/f97b6571-28f4-4ea7-8255-130ee99e07d2" />

3. Random Forest
<img width="553" height="546" alt="image" src="https://github.com/user-attachments/assets/4a9c099d-24ef-4137-b863-d0abb40dcf1f" />



## Conclusion

Among the three models, **Random Forest** provides the best overall performance for diamond price prediction, followed closely by **Decision Tree**. **Linear Regression** serves as a useful baseline but is less effective due to its inability to model complex nonlinear relationships in the data.
