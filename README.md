# Insurance Premium Category Predictor

A full-stack application that predicts insurance premium categories based on customer demographics and lifestyle factors using machine learning.

## Overview

This application consists of:
- **FastAPI Backend**: RESTful API that serves a machine learning model for insurance premium prediction
- **Streamlit Frontend**: Interactive web interface for users to input customer data and get predictions

## Features

- Predicts insurance premium categories based on customer profile
- Real-time BMI calculation
- Age group categorization (young, adult, middle_aged, senior)
- Lifestyle risk assessment based on smoking and BMI
- City tier classification (Tier 1, 2, or 3 cities in India)
- Input validation using Pydantic models
- User-friendly web interface

## Project Structure

```
insurance_prediction/
├── app.py              # FastAPI backend application
├── frontend.py         # Streamlit frontend application
├── model.pkl          # Trained machine learning model (pickle file)
└── README.md          # This file
```

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Dependencies

Install the required packages:

```bash
pip install fastapi uvicorn streamlit pandas pydantic requests pickle
```

## Usage

### 1. Start the FastAPI Backend

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at `http://127.0.0.1:8000`

### 2. Start the Streamlit Frontend

In a new terminal window:

```bash
streamlit run frontend.py
```

The web interface will open in your browser (typically at `http://localhost:8501`)

## API Documentation

### Endpoint: `/predict`
- **Method**: POST
- **Content-Type**: application/json

#### Request Body Schema

```json
{
  "age": 30,
  "weight": 70.5,
  "height": 1.75,
  "income_lpa": 12.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

#### Field Descriptions

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| age | integer | Customer's age in years | > 0 |
| weight | float | Customer's weight in kg | > 0 |
| height | float | Customer's height in meters | > 0 |
| income_lpa | float | Annual income in LPA (Lakhs Per Annum) | > 0 |
| smoker | boolean | Whether the customer smokes | true/false |
| city | string | Customer's city of residence | Any string |
| occupation | string | Customer's occupation | One of: 'retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job' |

#### Response

```json
{
  "Prediction": "medium"
}
```

## Model Features

The application automatically computes the following derived features:

1. **BMI**: Calculated as weight/(height²)
2. **Age Group**: 
   - young (< 25)
   - adult (25-44)
   - middle_aged (45-59)  
   - senior (≥ 60)
3. **Lifestyle Risk**:
   - high: smoker + BMI > 30
   - medium: smoker + BMI > 27
   - low: otherwise
4. **City Tier**:
   - Tier 1: Major metros (Mumbai, Delhi, Bangalore, etc.)
   - Tier 2: Important regional cities
   - Tier 3: All other cities

## City Classifications

### Tier 1 Cities
Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune

### Tier 2 Cities
Includes 50+ cities like Jaipur, Chandigarh, Indore, Lucknow, Patna, and others

### Tier 3 Cities
All cities not listed in Tier 1 or Tier 2

## Model File

Ensure the trained model file `model.pkl` is present in the correct path:
```
C:\Users\mdriz\Youtube tut\fastapi\insurance_prediction\model.pkl
```

**Note**: Update the model path in `app.py` if your file structure is different.

## Error Handling

The application includes error handling for:
- Invalid input data (Pydantic validation)
- API connection errors
- Model loading issues
- HTTP status code errors

## Development

### API Documentation
When the FastAPI server is running, visit:
- Interactive docs: `http://127.0.0.1:8000/docs`
- Alternative docs: `http://127.0.0.1:8000/redoc`

### Testing the API
You can test the API directly using curl:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "age": 35,
       "weight": 75.0,
       "height": 1.8,
       "income_lpa": 15.0,
       "smoker": false,
       "city": "Mumbai",
       "occupation": "private_job"
     }'
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for more details.

## Support

For issues or questions, please create an issue in the project repository.
