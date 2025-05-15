# Student_Performance_API
A FastAPI-based service that predicts student performance using a machine learning model. Easy to deploy with Docker and tested with pytest.


## What This Project Does

- Provides RESTful endpoints to input data and retrieve student performance metric.
- Supports configuration via environment variables.
- Includes validation and settings management using Pydantic.
- Containerized using Docker for consistent environments.
- Supports automated testing with pytest.
- Uses pre-commit hooks to ensure code quality.
- Integrates CI/CD via GitHub Actions.

---

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
--------
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
--------
### Testing
```bash
 $env:PYTHONPATH = "."                  
  pytest
```



