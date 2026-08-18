"""
Master Execution Script for Bluestock Mutual Fund ETL Pipeline.

This script orchestrates the extraction, transformation, and loading (ETL)
processes for mutual fund historical and operational data.
"""

import logging
import sys
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def run():
    """Executes the end-to-end data pipeline."""
    logging.info("Starting Bluestock MF Data Pipeline...")
    
    try:
        raw_data = extract_data()
        logging.info("Extraction complete.")
        
        clean_data = transform_data(raw_data)
        logging.info("Transformation complete.")
        
        load_data(clean_data)
        logging.info("Loading complete. Pipeline executed successfully.")
        
    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run()