"""
Author: Nabila Kumala Gantari
Date: 21/07/2024
This is the local_pipeline.py module.
Usage:
- Run the ML pipeline components
"""

# Import libraries
import os
from typing import Text
from absl import logging
from tfx.orchestration import metadata, pipeline
from tfx.orchestration.beam.beam_dag_runner import BeamDagRunner

PIPELINE_NAME = "nkumala16-pipeline"

# Pipeline inputs
DATA_ROOT = "data"
TRANSFORM_MODULE_FILE = "modules/heart_attack_transform.py"
TRAINER_MODULE_FILE = "modules/heart_attack_trainer.py"

# Pipeline outputs
OUTPUT_BASE = "output"
serving_model_dir = os.path.join(OUTPUT_BASE, 'serving_model')
pipeline_root = os.path.join(OUTPUT_BASE, PIPELINE_NAME)
metadata_path = os.path.join(pipeline_root, "metadata.sqlite")

def init_local_pipeline(
    components, pipeline_root: Text
) -> pipeline.Pipeline:
    """
    Initialize the local pipeline.

    Args:
        components: The components to include in the pipeline.
        pipeline_root: The root directory for the pipeline.

    Returns:
        A TFX Pipeline object.
    """
    logging.info(f"Pipeline root set to: {pipeline_root}")
    beam_args = [
        "--direct_running_mode=multi_processing",
        "--direct_num_workers=0"
    ]
    
    return pipeline.Pipeline(
        pipeline_name=PIPELINE_NAME,
        pipeline_root=pipeline_root,
        components=components,
        enable_cache=True,
        metadata_connection_config=metadata.sqlite_metadata_connection_config(
            metadata_path
        ),
        beam_pipeline_args=beam_args
    )

if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)
    
    from modules.components import init_components
    
    components = init_components(
        DATA_ROOT,
        training_module=TRAINER_MODULE_FILE,
        transform_module=TRANSFORM_MODULE_FILE,
        training_steps=5000,
        eval_steps=1000,
        serving_model_dir=serving_model_dir,
    )
    
    local_pipeline = init_local_pipeline(components, pipeline_root)
    BeamDagRunner().run(pipeline=local_pipeline)