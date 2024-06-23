import sys
import os

from Shipment_root_folder.logger import logging
from Shipment_root_folder.exception import Shipment_Exception
from Shipment_root_folder.pipeline.training_pipeline import TrainPipeline


if __name__ == '__main__':
    obj = TrainPipeline()
    obj.run_pipeline()