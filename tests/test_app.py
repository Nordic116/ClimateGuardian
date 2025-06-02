"""
Test suite for ClimateGuardian application
"""

import unittest
import json
from app import app, guardian

class ClimateGuardianTestCase(unittest.TestCase):
    """Test cases for ClimateGuardian application"""
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], 'ClimateGuardian')
    
    def test_datasets_endpoint(self):
        """Test datasets information endpoint"""
        response = self.app.get('/api/datasets')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIsInstance(data['data'], list)
        self.assertGreater(len(data['data']), 0)
    
    def test_query_endpoint_valid(self):
        """Test query endpoint with valid input"""
        query_data = {
            "question": "What are the flood risks for Bangladesh?"
        }
        
        response = self.app.post('/api/query',
                               data=json.dumps(query_data),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('answer', data['data'])
        self.assertIn('sources', data['data'])
        self.assertIn('confidence', data['data'])
    
    def test_query_endpoint_empty(self):
        """Test query endpoint with empty question"""
        query_data = {
            "question": ""
        }
        
        response = self.app.post('/api/query',
                               data=json.dumps(query_data),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')
    
    def test_query_endpoint_missing_question(self):
        """Test query endpoint without question field"""
        query_data = {}
        
        response = self.app.post('/api/query',
                               data=json.dumps(query_data),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
    
    def test_index_page(self):
        """Test main index page"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ClimateGuardian', response.data)
    
    def test_history_endpoint(self):
        """Test conversation history endpoint"""
        # First make a query to create history
        query_data = {
            "question": "Test question"
        }
        self.app.post('/api/query',
                     data=json.dumps(query_data),
                     content_type='application/json')
        
        # Then get history
        response = self.app.get('/api/history')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIsInstance(data['data'], list)

class ClimateGuardianLogicTestCase(unittest.TestCase):
    """Test cases for ClimateGuardian logic"""
    
    def setUp(self):
        """Set up test guardian instance"""
        self.guardian = guardian
    
    def test_intent_analysis_risk_assessment(self):
        """Test intent analysis for risk assessment queries"""
        intent = self.guardian._analyze_intent("What are the flood risks for Bangladesh?")
        self.assertEqual(intent, "risk_assessment")
        
        intent = self.guardian._analyze_intent("vulnerability assessment for coastal areas")
        self.assertEqual(intent, "risk_assessment")
    
    def test_intent_analysis_policy(self):
        """Test intent analysis for policy queries"""
        intent = self.guardian._analyze_intent("What policies should we implement?")
        self.assertEqual(intent, "policy_recommendation")
        
        intent = self.guardian._analyze_intent("climate strategy recommendations")
        self.assertEqual(intent, "policy_recommendation")
    
    def test_intent_analysis_funding(self):
        """Test intent analysis for funding queries"""
        intent = self.guardian._analyze_intent("climate funding opportunities")
        self.assertEqual(intent, "funding_intelligence")
        
        intent = self.guardian._analyze_intent("grants for climate projects")
        self.assertEqual(intent, "funding_intelligence")
    
    def test_intent_analysis_data(self):
        """Test intent analysis for data queries"""
        intent = self.guardian._analyze_intent("show me climate data trends")
        self.assertEqual(intent, "data_analysis")
        
        intent = self.guardian._analyze_intent("temperature statistics for 2023")
        self.assertEqual(intent, "data_analysis")
    
    def test_query_processing(self):
        """Test complete query processing"""
        response = self.guardian.query("What are the flood risks for Bangladesh?")
        
        self.assertIn('answer', response)
        self.assertIn('sources', response)
        self.assertIn('confidence', response)
        self.assertIn('intent', response)
        self.assertIn('timestamp', response)
        
        self.assertIsInstance(response['sources'], list)
        self.assertIsInstance(response['confidence'], (int, float))
        self.assertGreater(response['confidence'], 0)
        self.assertLessEqual(response['confidence'], 100)
    
    def test_conversation_history(self):
        """Test conversation history tracking"""
        initial_count = len(self.guardian.conversation_history)
        
        self.guardian.query("Test question 1")
        self.guardian.query("Test question 2")
        
        final_count = len(self.guardian.conversation_history)
        self.assertEqual(final_count, initial_count + 2)

if __name__ == '__main__':
    unittest.main()