import dagshub
import mlflow

dagshub.init("sudent_data_insights", "Pradhyumn1", mlflow=True)
mlflow.start_run()


mlflow.log_param("parameter name ", "value")
mlflow.log_metric("metric name", 1)

mlflow.end_run()