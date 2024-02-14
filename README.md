# End-to-End Data Science Project

This project aims to demonstrate an end-to-end data science pipeline for training machine learning models using MLflow for experiment tracking. The pipeline includes data ingestion, preprocessing, model training, and evaluation.

## Setup

1. **Clone Repository**: Clone this repository to your local machine.

2. **Install Dependencies**: Install the required dependencies by running `pip install -r requirements.txt`.

3. **Set Up Environment**: Set up your Python environment using `conda` or `virtualenv`. Activate the environment before running the scripts.

4. **Configuration**: Configure your MLflow tracking URI, username, and password in `app.py`. Ensure that the MLflow tracking server is accessible.

5. **Database Connection**: Update the database connection details in `utils.py` if you're using a MySQL database.

## Project Structure

- **src/**: Contains project source code.
  - **my_mlproject/**: Main project module.
    - **components/**: Modules for different components of the pipeline.
    - **pipelines/**: Modules for different pipeline stages.
  - **exception.py**: Custom exception handling.
  - **logger.py**: Logging configuration.
  - **utils.py**: Utility functions.
- **notebook/**: Contains Jupyter notebooks for exploratory data analysis (EDA) or other analyses.
- **requirements.txt**: List of Python dependencies.
- **setup.py**: Python package setup file.
- **README.md**: Project overview and instructions.
- **Dockerfile**: Docker configuration for containerization.

## Usage

1. **Data Ingestion**: Run `app.py` to start the data ingestion process. This step fetches data from a MySQL database, preprocesses it, and saves it to CSV files.

2. **Data Transformation**: The ingested data is then transformed using various preprocessing techniques, including imputation, scaling, and one-hot encoding. This step is handled by the `data_transformation.py` module.

3. **Model Training**: After preprocessing, the data is split into training and testing sets. Multiple machine learning models are trained using different algorithms and hyperparameters. The best-performing model is selected based on evaluation metrics such as RMSE, MAE, and R2 score.

4. **MLflow Tracking**: Experiment metrics and artifacts are logged using MLflow for tracking and reproducibility. The trained model is registered with MLflow for future reference.

## Troubleshooting

If you encounter any issues during project execution or experiment tracking, refer to the following troubleshooting steps:

- Check the configuration settings in `app.py` and ensure that the MLflow tracking URI, username, and password are correct.
- Verify database connection details in `utils.py` if applicable.
- Review the error messages and logs for more information on failed experiments.
- Debug your code locally to identify and resolve any errors or issues.
- Consult the project documentation and community resources for additional assistance.

bash  = '

export MLFLOW_TRACKING_URI=https://dagshub.com/Pradhyumn1/sudent_data_insights.mlflow 

export MLFLOW_TRACKING_USERNAME=Pradhyumn1 

export MLFLOW_TRACKING_PASSWORD=9668024cdf3cab6718afb606d69ebde8f71b7dcf

'
