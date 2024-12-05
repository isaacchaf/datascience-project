from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngetionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngetionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformationn Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_transformatiom = DataTransformationTrainingPipeline()
    data_transformatiom.initiate_data_transformation()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.initiate_model_trainer()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e