from django.test import TestCase
from easyjob.models import Company 
# Create your tests here.

class CompanyTestCase(TestCase):
    def test_company_name_blank_check(self):
        c1=Company.objects.Create(cCompanyName="Herald", cEmail="herald@heraldcollege.edu.np")
        self.assertTrue(c1.company_name_blank_check())


    