"""
ClimateGuardian - AI-powered climate risk analysis and policy recommendations
Main Flask application for web deployment
"""

import os
import json
import logging
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import requests
from typing import Dict, List, Optional
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'climate-guardian-secret-key-2025')

# Enable CORS for all routes
CORS(app, origins=['*'], allow_headers=['*'], methods=['*'])

# Configuration
class Config:
    WATSONX_API_KEY = os.environ.get('WATSONX_API_KEY')
    WATSONX_PROJECT_ID = os.environ.get('WATSONX_PROJECT_ID')
    IBM_CLOUD_API_KEY = os.environ.get('IBM_CLOUD_API_KEY')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    PORT = int(os.environ.get('PORT', 12000))

# Mock data for demonstration (in production, this would connect to real APIs)
MOCK_CLIMATE_DATA = {
    "flood_risks": {
        "Bangladesh": {
            "risk_level": "HIGH",
            "confidence": 89,
            "factors": [
                "Increased monsoon intensity (+23% by 2030)",
                "Sea level rise of 15-20cm expected",
                "40% of population in flood-prone areas"
            ],
            "sources": ["ND-GAIN Country Index 2023", "NOAA Climate Projections"]
        },
        "Netherlands": {
            "risk_level": "MEDIUM",
            "confidence": 76,
            "factors": [
                "Advanced flood protection systems",
                "Sea level rise of 10-15cm expected",
                "25% of land below sea level"
            ],
            "sources": ["European Climate Assessment", "Dutch Delta Works Data"]
        }
    },
    "policy_recommendations": {
        "small_island_nations": {
            "priorities": [
                {
                    "policy": "Coastal protection infrastructure",
                    "funding": "$2.3B funding available",
                    "impact": "High"
                },
                {
                    "policy": "Renewable energy transition",
                    "funding": "74% potential reduction in emissions",
                    "impact": "Very High"
                },
                {
                    "policy": "Climate-smart agriculture adaptation",
                    "funding": "$500M available",
                    "impact": "Medium"
                }
            ],
            "funding_opportunities": [
                {
                    "name": "Green Climate Fund",
                    "deadline": "June 2025",
                    "amount": "$50M"
                },
                {
                    "name": "Adaptation Fund",
                    "deadline": "August 2025",
                    "amount": "$25M"
                }
            ],
            "sources": ["UN SDG13 Database", "Climate Watch Policy Tracker"]
        }
    },
    "funding_opportunities": {
        "africa_ngos": [
            {
                "name": "Adaptation Fund",
                "amount": "$50M",
                "deadline": "August 2025",
                "eligibility": "Must demonstrate community impact and have local partnerships"
            },
            {
                "name": "Climate Investment Funds",
                "amount": "$25M",
                "deadline": "September 2025",
                "focus": "Community-based adaptation"
            },
            {
                "name": "Global Environment Facility",
                "amount": "$15M",
                "deadline": "October 2025",
                "focus": "Ecosystem-based solutions"
            }
        ]
    }
}

class ClimateGuardian:
    """Main ClimateGuardian AI assistant class"""
    
    def __init__(self):
        self.api_key = Config.WATSONX_API_KEY
        self.project_id = Config.WATSONX_PROJECT_ID
        self.conversation_history = []
    
    def query(self, question: str, context: Optional[Dict] = None) -> Dict:
        """Process a climate-related query and return AI-generated response"""
        try:
            # Store query in conversation history
            query_id = str(uuid.uuid4())
            timestamp = datetime.now().isoformat()
            
            # Analyze query intent
            intent = self._analyze_intent(question)
            
            # Generate response based on intent
            response = self._generate_response(question, intent, context)
            
            # Store in conversation history
            self.conversation_history.append({
                "id": query_id,
                "timestamp": timestamp,
                "question": question,
                "intent": intent,
                "response": response
            })
            
            return {
                "id": query_id,
                "answer": response["answer"],
                "sources": response["sources"],
                "confidence": response["confidence"],
                "intent": intent,
                "timestamp": timestamp
            }
            
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return {
                "id": str(uuid.uuid4()),
                "answer": "I apologize, but I encountered an error processing your query. Please try again.",
                "sources": [],
                "confidence": 0,
                "intent": "error",
                "timestamp": datetime.now().isoformat()
            }
    
    def _analyze_intent(self, question: str) -> str:
        """Analyze the intent of the user's question"""
        question_lower = question.lower()
        
        if any(word in question_lower for word in ["flood", "risk", "vulnerability", "disaster"]):
            return "risk_assessment"
        elif any(word in question_lower for word in ["policy", "recommend", "should", "strategy"]):
            return "policy_recommendation"
        elif any(word in question_lower for word in ["funding", "grant", "money", "finance"]):
            return "funding_intelligence"
        elif any(word in question_lower for word in ["data", "statistics", "numbers", "trend"]):
            return "data_analysis"
        else:
            return "general_climate"
    
    def _generate_response(self, question: str, intent: str, context: Optional[Dict] = None) -> Dict:
        """Generate AI response based on intent and available data"""
        
        if intent == "risk_assessment":
            return self._handle_risk_assessment(question)
        elif intent == "policy_recommendation":
            return self._handle_policy_recommendation(question)
        elif intent == "funding_intelligence":
            return self._handle_funding_intelligence(question)
        elif intent == "data_analysis":
            return self._handle_data_analysis(question)
        else:
            return self._handle_general_climate(question)
    
    def _handle_risk_assessment(self, question: str) -> Dict:
        """Handle risk assessment queries"""
        # Extract location/region from question
        if "bangladesh" in question.lower():
            data = MOCK_CLIMATE_DATA["flood_risks"]["Bangladesh"]
            answer = f"""Based on ND-GAIN vulnerability data and NOAA precipitation forecasts, 
Bangladesh faces {data['risk_level']} flood risk (confidence: {data['confidence']}%) due to:

{chr(10).join(f"• {factor}" for factor in data['factors'])}

This assessment is based on current climate models and historical data patterns."""
            
            return {
                "answer": answer,
                "sources": data["sources"],
                "confidence": data["confidence"]
            }
        
        # Default risk assessment response
        return {
            "answer": """Climate risk assessment requires specific location data. Please specify a country, 
region, or city for detailed risk analysis. I can provide information on flood risks, drought 
vulnerability, extreme weather patterns, and sea level rise impacts.""",
            "sources": ["ND-GAIN Country Index", "NOAA Climate Data"],
            "confidence": 85
        }
    
    def _handle_policy_recommendation(self, question: str) -> Dict:
        """Handle policy recommendation queries"""
        if "small island" in question.lower() or "island nation" in question.lower():
            data = MOCK_CLIMATE_DATA["policy_recommendations"]["small_island_nations"]
            
            policies_text = "\n".join([
                f"{i+1}. {policy['policy']} ({policy['funding']})"
                for i, policy in enumerate(data["priorities"])
            ])
            
            funding_text = "\n".join([
                f"• {fund['name']}: {fund['amount']} (deadline: {fund['deadline']})"
                for fund in data["funding_opportunities"]
            ])
            
            answer = f"""For small island developing states, priority policies include:

{policies_text}

Funding Opportunities:
{funding_text}

These recommendations are based on IPCC guidelines and successful adaptation strategies from similar regions."""
            
            return {
                "answer": answer,
                "sources": data["sources"],
                "confidence": 92
            }
        
        return {
            "answer": """Policy recommendations depend on specific regional context, governance structure, 
and climate vulnerabilities. Please specify a region, country, or sector for targeted policy guidance. 
I can provide recommendations for adaptation, mitigation, financing, and implementation strategies.""",
            "sources": ["IPCC Policy Guidelines", "UN Climate Policy Database"],
            "confidence": 80
        }
    
    def _handle_funding_intelligence(self, question: str) -> Dict:
        """Handle funding and grant opportunity queries"""
        if "africa" in question.lower() and "ngo" in question.lower():
            opportunities = MOCK_CLIMATE_DATA["funding_opportunities"]["africa_ngos"]
            
            funding_text = "\n".join([
                f"• {opp['name']}: {opp['amount']} (deadline: {opp['deadline']})\n  Focus: {opp.get('focus', opp.get('eligibility', 'General climate action'))}"
                for opp in opportunities
            ])
            
            answer = f"""Current climate funding opportunities for African NGOs:

{funding_text}

Application tips:
• Demonstrate clear community impact and local partnerships
• Include measurable climate adaptation or mitigation outcomes
• Provide detailed budget breakdown and sustainability plan"""
            
            return {
                "answer": answer,
                "sources": ["Climate Finance Database", "Adaptation Fund Project Database"],
                "confidence": 88
            }
        
        return {
            "answer": """Climate funding opportunities vary by region, organization type, and project focus. 
Please specify your location, organization type (NGO, government, private sector), and project area 
for targeted funding recommendations. I can help identify grants, loans, and investment opportunities.""",
            "sources": ["Global Climate Finance Database", "Green Climate Fund"],
            "confidence": 85
        }
    
    def _handle_data_analysis(self, question: str) -> Dict:
        """Handle data analysis and statistics queries"""
        return {
            "answer": """I can provide analysis of climate data including temperature trends, precipitation 
patterns, emissions data, and vulnerability indices. Please specify:
• Geographic region of interest
• Type of climate data (temperature, precipitation, emissions, etc.)
• Time period for analysis
• Specific metrics or indicators needed""",
            "sources": ["NOAA Climate Data", "Climate TRACE", "OpenAQ"],
            "confidence": 90
        }
    
    def _handle_general_climate(self, question: str) -> Dict:
        """Handle general climate queries"""
        return {
            "answer": """I'm ClimateGuardian, your AI assistant for climate risk analysis and policy recommendations. 
I can help with:

• Climate risk assessments for specific regions
• Evidence-based policy recommendations
• Climate funding and grant opportunities
• Data analysis and trend interpretation
• Adaptation and mitigation strategies

Please ask me about specific climate challenges, locations, or policy areas for detailed assistance.""",
            "sources": ["IPCC Reports", "UN Climate Database"],
            "confidence": 95
        }

# Initialize ClimateGuardian instance
guardian = ClimateGuardian()

@app.route('/')
def index():
    """Main application page"""
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def api_query():
    """API endpoint for processing climate queries"""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        
        if not question:
            return jsonify({
                "error": "Question is required",
                "status": "error"
            }), 400
        
        # Get user context from session
        context = {
            "user_id": session.get('user_id', str(uuid.uuid4())),
            "session_id": session.get('session_id', str(uuid.uuid4()))
        }
        
        # Store user context in session
        session['user_id'] = context['user_id']
        session['session_id'] = context['session_id']
        
        # Process query
        response = guardian.query(question, context)
        
        return jsonify({
            "status": "success",
            "data": response
        })
        
    except Exception as e:
        logger.error(f"API query error: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "status": "error"
        }), 500

@app.route('/api/history', methods=['GET'])
def api_history():
    """Get conversation history"""
    try:
        # Return last 10 conversations
        history = guardian.conversation_history[-10:]
        return jsonify({
            "status": "success",
            "data": history
        })
    except Exception as e:
        logger.error(f"API history error: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "status": "error"
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "ClimateGuardian",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/datasets', methods=['GET'])
def api_datasets():
    """Get information about available datasets"""
    datasets = [
        {
            "name": "ND-GAIN",
            "description": "Climate vulnerability and readiness index",
            "license": "CC BY 4.0",
            "update_frequency": "Annual",
            "url": "https://gain.nd.edu/our-work/country-index/"
        },
        {
            "name": "NOAA Climate Data",
            "description": "Historical weather and climate records",
            "license": "Public Domain",
            "update_frequency": "Daily/Monthly",
            "url": "https://www.ncei.noaa.gov/products"
        },
        {
            "name": "OpenAQ",
            "description": "Global air quality measurements",
            "license": "CC BY 4.0",
            "update_frequency": "Real-time",
            "url": "https://openaq.org/"
        },
        {
            "name": "Climate TRACE",
            "description": "Greenhouse gas emissions data",
            "license": "CC BY 4.0",
            "update_frequency": "Annual",
            "url": "https://climatetrace.org/"
        },
        {
            "name": "Climate Watch",
            "description": "Climate policy and NDC tracking",
            "license": "CC BY 4.0",
            "update_frequency": "Quarterly",
            "url": "https://www.climatewatchdata.org/"
        },
        {
            "name": "UN SDG 13 Indicators",
            "description": "Climate action progress metrics",
            "license": "CC BY 3.0",
            "update_frequency": "Annual",
            "url": "https://unstats.un.org/sdgs/indicators/database/"
        }
    ]
    
    return jsonify({
        "status": "success",
        "data": datasets
    })

if __name__ == '__main__':
    port = Config.PORT
    debug = Config.DEBUG
    
    logger.info(f"Starting ClimateGuardian on port {port}")
    logger.info(f"Debug mode: {debug}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug,
        threaded=True
    )