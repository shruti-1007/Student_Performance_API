# Student_Performance_API
A FastAPI-based service that predicts student performance using a machine learning model. Easy to deploy with Docker and tested with pytest.


##  Features

- Predict student performance using input features like study hours, previous scores, and sleep hours.
- RESTful API built with **FastAPI**
- ML model integration via `joblib`
- Pydantic-based data validation
- Structured project layout
- Pre-commit hooks and GitHub Actions for CI
- Config management with environment variables
- Docker and Docker Compose support
- MkDocs-powered documentation

---
##  Sample Input

```json
{
  "Hours_Studied": 5.5,
  "Previous_Scores": 78.0,
  "Extracurricular_Activities": "Yes",
  "Sleep_Hours": 7.0,
  "Sample_Question_Papers_Practiced": 10
}
```
## How to Run the Project

### Prerequisites

- Python 3.10+
- Docker (optional, but recommended)
- git

### Running Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/student_performance_api.git
cd student_performance_api
```
2. Create and activate a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the API server:
```bash
uvicorn app.app:app --reload
```
5. Open http://localhost:8000.

### Running with Docker
1. Build the Docker image:
```bash
docker build -t student_performance_api .
```
2. Run the Container
```bash
docker run -d -p 8000:8000 --env-file .env student_performance_api
```
3. Open http://localhost:8000.

### Testing
Run automated tests with:
```bash
 $env:PYTHONPATH = "."                  
  pytest
```
### Documentation
Basic docs are maintained with MkDocs:
- To preview docs locally:
```bash
cd docs
mkdocs build
mkdocs serve
```
- Open http://localhost:8000 to view docs.

### Demo
[Watch Here](https://youtu.be/UjTWZ3WANnM?si=IlncwMfc1Q7za9kt)

