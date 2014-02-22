import importer
import unittest
import os

class Test(unittest.TestCase):
    def setUp(self):
        filename = os.path.join(os.path.dirname(__file__), 'walla_contacts.txt')
        self.gmail_names, self.gmail_emails = importer.walla_to_gmail_import(filename)
    
    def test_emails_without_names(self):
        self.assertEqual(self.gmail_names[0], u'aaa1 hotmail')
        self.assertEqual(self.gmail_names[1], u'bbb2 walla')
        self.assertEqual(self.gmail_names[2], u'ccc3 yahoo')

        self.assertEqual(self.gmail_emails[0], u'aaa1@hotmail.com')
        self.assertEqual(self.gmail_emails[1], u'bbb2@walla.com')
        self.assertEqual(self.gmail_emails[2], u'ccc3@yahoo.com')        
    
    def test_emails_with_names(self):
        self.assertEqual(self.gmail_names[3].strip(), u'moshe cohen')
        self.assertEqual(self.gmail_names[4].strip(), u'\u05d3"\u05e8 \u05d1\u05df \u05d9\u05e9\u05e8\u05d0\u05dc')
        self.assertEqual(self.gmail_names[5].strip(), u'\u05d3\u05e0\u05d9 \u05d3\u05df')
    
        self.assertEqual(self.gmail_emails[3], u'office@moshe-cohen.com')
        self.assertEqual(self.gmail_emails[4], u'benyi@013.net')
        self.assertEqual(self.gmail_emails[5], u'dannnydan@gmail.com')  
        
if __name__ == "__main__":
    unittest.main()