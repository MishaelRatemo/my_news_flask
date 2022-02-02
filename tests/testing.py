import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    ''' test class testing Sources class'''
    def setUp(self):
        ''' base function for testing'''
        self.new_source = Sources('alj','Aljazeera','Worldworls news provider','www.aljazeera')
        
     
    def test_instance(self):
        '''
        Test to check creation of new article Source instance
        '''
        self.assertTrue(isinstance(self.new_source,Sources))
   



        
        