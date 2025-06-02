#!/usr/bin/env python3
"""
ClimateGuardian Dataset Initialization Script
This script initializes and validates climate datasets for the application.
"""

import os
import sys
import json
import requests
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DatasetInitializer:
    """Initialize and validate climate datasets"""
    
    def __init__(self):
        self.datasets = {
            "nd_gain": {
                "name": "ND-GAIN",
                "description": "Climate vulnerability and readiness index",
                "url": "https://gain.nd.edu/our-work/country-index/",
                "api_endpoint": None,  # Would be actual API in production
                "license": "CC BY 4.0",
                "update_frequency": "Annual"
            },
            "noaa_climate": {
                "name": "NOAA Climate Data",
                "description": "Historical weather and climate records",
                "url": "https://www.ncei.noaa.gov/products",
                "api_endpoint": None,  # Would be actual API in production
                "license": "Public Domain",
                "update_frequency": "Daily/Monthly"
            },
            "openaq": {
                "name": "OpenAQ",
                "description": "Global air quality measurements",
                "url": "https://openaq.org/",
                "api_endpoint": "https://api.openaq.org/v2/",
                "license": "CC BY 4.0",
                "update_frequency": "Real-time"
            },
            "climate_trace": {
                "name": "Climate TRACE",
                "description": "Greenhouse gas emissions data",
                "url": "https://climatetrace.org/",
                "api_endpoint": None,  # Would be actual API in production
                "license": "CC BY 4.0",
                "update_frequency": "Annual"
            },
            "climate_watch": {
                "name": "Climate Watch",
                "description": "Climate policy and NDC tracking",
                "url": "https://www.climatewatchdata.org/",
                "api_endpoint": None,  # Would be actual API in production
                "license": "CC BY 4.0",
                "update_frequency": "Quarterly"
            },
            "un_sdg13": {
                "name": "UN SDG 13 Indicators",
                "description": "Climate action progress metrics",
                "url": "https://unstats.un.org/sdgs/indicators/database/",
                "api_endpoint": None,  # Would be actual API in production
                "license": "CC BY 3.0",
                "update_frequency": "Annual"
            }
        }
        
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        os.makedirs(self.data_dir, exist_ok=True)
    
    def initialize_all_datasets(self) -> Dict[str, bool]:
        """Initialize all datasets and return status"""
        results = {}
        
        logger.info("Starting dataset initialization...")
        
        for dataset_id, dataset_info in self.datasets.items():
            try:
                logger.info(f"Initializing {dataset_info['name']}...")
                success = self.initialize_dataset(dataset_id, dataset_info)
                results[dataset_id] = success
                
                if success:
                    logger.info(f"✅ {dataset_info['name']} initialized successfully")
                else:
                    logger.warning(f"⚠️ {dataset_info['name']} initialization failed")
                    
            except Exception as e:
                logger.error(f"❌ Error initializing {dataset_info['name']}: {str(e)}")
                results[dataset_id] = False
        
        # Generate summary report
        self.generate_summary_report(results)
        
        return results
    
    def initialize_dataset(self, dataset_id: str, dataset_info: Dict) -> bool:
        """Initialize a specific dataset"""
        try:
            # Create dataset metadata
            metadata = {
                "id": dataset_id,
                "name": dataset_info["name"],
                "description": dataset_info["description"],
                "url": dataset_info["url"],
                "license": dataset_info["license"],
                "update_frequency": dataset_info["update_frequency"],
                "last_updated": datetime.now().isoformat(),
                "status": "initialized",
                "api_available": dataset_info["api_endpoint"] is not None
            }
            
            # Test API connectivity if available
            if dataset_info["api_endpoint"]:
                api_status = self.test_api_connectivity(dataset_info["api_endpoint"])
                metadata["api_status"] = api_status
            
            # Save metadata
            metadata_file = os.path.join(self.data_dir, f"{dataset_id}_metadata.json")
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            # Create sample data file (in production, this would fetch real data)
            self.create_sample_data(dataset_id, dataset_info)
            
            return True
            
        except Exception as e:
            logger.error(f"Error initializing {dataset_id}: {str(e)}")
            return False
    
    def test_api_connectivity(self, api_endpoint: str) -> Dict:
        """Test API connectivity and return status"""
        try:
            response = requests.get(api_endpoint, timeout=10)
            return {
                "accessible": response.status_code == 200,
                "status_code": response.status_code,
                "response_time": response.elapsed.total_seconds(),
                "tested_at": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "accessible": False,
                "error": str(e),
                "tested_at": datetime.now().isoformat()
            }
    
    def create_sample_data(self, dataset_id: str, dataset_info: Dict):
        """Create sample data for demonstration purposes"""
        sample_data = {
            "nd_gain": {
                "countries": [
                    {"country": "Bangladesh", "vulnerability_score": 0.72, "readiness_score": 0.31},
                    {"country": "Netherlands", "vulnerability_score": 0.28, "readiness_score": 0.89},
                    {"country": "Maldives", "vulnerability_score": 0.85, "readiness_score": 0.42}
                ]
            },
            "noaa_climate": {
                "temperature_trends": [
                    {"region": "Global", "year": 2023, "anomaly": 1.2},
                    {"region": "Arctic", "year": 2023, "anomaly": 2.8},
                    {"region": "Tropical", "year": 2023, "anomaly": 0.9}
                ]
            },
            "openaq": {
                "air_quality": [
                    {"city": "Delhi", "pm25": 89.5, "timestamp": "2024-01-01T00:00:00Z"},
                    {"city": "Beijing", "pm25": 67.2, "timestamp": "2024-01-01T00:00:00Z"},
                    {"city": "Los Angeles", "pm25": 23.1, "timestamp": "2024-01-01T00:00:00Z"}
                ]
            },
            "climate_trace": {
                "emissions": [
                    {"country": "China", "co2_emissions_mt": 10175, "year": 2022},
                    {"country": "United States", "co2_emissions_mt": 5007, "year": 2022},
                    {"country": "India", "co2_emissions_mt": 2654, "year": 2022}
                ]
            },
            "climate_watch": {
                "ndc_progress": [
                    {"country": "Costa Rica", "target": "Carbon neutral by 2050", "progress": 0.65},
                    {"country": "Denmark", "target": "70% reduction by 2030", "progress": 0.78},
                    {"country": "Bhutan", "target": "Carbon negative", "progress": 1.0}
                ]
            },
            "un_sdg13": {
                "climate_indicators": [
                    {"indicator": "Climate finance mobilized", "value": 83.3, "unit": "billion USD", "year": 2022},
                    {"indicator": "Countries with NDCs", "value": 195, "unit": "count", "year": 2023},
                    {"indicator": "Renewable energy capacity", "value": 3372, "unit": "GW", "year": 2022}
                ]
            }
        }
        
        if dataset_id in sample_data:
            data_file = os.path.join(self.data_dir, f"{dataset_id}_sample.json")
            with open(data_file, 'w') as f:
                json.dump(sample_data[dataset_id], f, indent=2)
    
    def generate_summary_report(self, results: Dict[str, bool]):
        """Generate initialization summary report"""
        total_datasets = len(results)
        successful = sum(results.values())
        failed = total_datasets - successful
        
        report = {
            "initialization_summary": {
                "timestamp": datetime.now().isoformat(),
                "total_datasets": total_datasets,
                "successful": successful,
                "failed": failed,
                "success_rate": f"{(successful/total_datasets)*100:.1f}%"
            },
            "dataset_status": results,
            "next_steps": [
                "Configure IBM watsonx.ai credentials",
                "Set up vector database for RAG",
                "Implement real-time data fetching",
                "Deploy to production environment"
            ]
        }
        
        report_file = os.path.join(self.data_dir, "initialization_report.json")
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"📊 Initialization complete: {successful}/{total_datasets} datasets successful")
        logger.info(f"📄 Report saved to: {report_file}")
    
    def validate_environment(self) -> bool:
        """Validate environment setup"""
        logger.info("Validating environment...")
        
        required_vars = ['WATSONX_API_KEY', 'WATSONX_PROJECT_ID']
        missing_vars = []
        
        for var in required_vars:
            if not os.environ.get(var):
                missing_vars.append(var)
        
        if missing_vars:
            logger.warning(f"Missing environment variables: {', '.join(missing_vars)}")
            logger.info("Note: These are required for production deployment")
            return False
        
        logger.info("✅ Environment validation passed")
        return True

def main():
    """Main initialization function"""
    print("🌍 ClimateGuardian Dataset Initialization")
    print("=" * 50)
    
    initializer = DatasetInitializer()
    
    # Validate environment
    env_valid = initializer.validate_environment()
    
    # Initialize datasets
    results = initializer.initialize_all_datasets()
    
    # Print summary
    successful = sum(results.values())
    total = len(results)
    
    print(f"\n📊 Summary:")
    print(f"   Datasets initialized: {successful}/{total}")
    print(f"   Environment setup: {'✅' if env_valid else '⚠️'}")
    print(f"   Ready for deployment: {'✅' if successful == total else '⚠️'}")
    
    if successful < total:
        print(f"\n⚠️  Some datasets failed to initialize. Check logs for details.")
        return 1
    
    print(f"\n🚀 ClimateGuardian is ready for deployment!")
    return 0

if __name__ == "__main__":
    sys.exit(main())