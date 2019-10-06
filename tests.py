import unittest
import transform

class Testtransform(unittest.TestCase):

    def setUp(self):
        #self.case_fixture = ['thisIsAText', "ThisIsAText", "this_is_a_text", "THIS_IS_A_TEXT", "this-is-a-text", "THIS-IS-A-TEXT"]
        self.case_fixture = ['thisIsAText', "ThisIsAText", "this_is_a_text"]

    def test_pascal_case(self):
        for t in self.case_fixture:
            r = transform.transop('pc', t)
            self.assertEqual('ThisIsAText', r)
  
    def test_camel_case(self):
        for t in self.case_fixture:
            r = transform.transop('cc', t)
            self.assertEqual('thisIsAText', r)

    def test_snake_case(self):
        for t in self.case_fixture:
            r = transform.transop('sc', t)
            self.assertEqual('this_is_a_text', r)

    def test_const_case(self):
        for t in self.case_fixture:
            r = transform.transop('cn', t)
            self.assertEqual('THIS_IS_A_TEXT', r)

    def test_upper_case(self):
        for t in self.case_fixture:
            r = transform.transop('uc', t)
            self.assertEqual(t.upper(), r)

    def test_lower_case(self):
        for t in self.case_fixture:
            r = transform.transop('lc', t)
            self.assertEqual(t.lower(), r)
            
class TestTransform(unittest.TestCase):

    def test_replace(self):
        f = ['private', 'Money', 'totalAmount']
        r = transform.replace(f, 'obj.set%pc3();')
        self.assertEqual('obj.setTotalAmount();', r)
    
    def test_replace_hash(self):
        f = ['private', 'Money', 'totalAmount']
        r = transform.replace(f, 'new %#2;', {'Money': 'Money(1.0d, "EUR")'})
        self.assertEqual('new Money(1.0d, "EUR");', r)

    def test_transform(self):

        f = """private Money amount1;
               private String name;
               private TestClass subjectInTest;"""

        r = transform.transform(f.split(';'), 'obj.set%pc3(%id2)')
        self.assertEqual(['obj.setAmount1(Money)', 'obj.setName(String)', 'obj.setSubjectInTest(TestClass)'], r)

if __name__ == "__main__":
    unittest.main()