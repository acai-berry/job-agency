from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.test.client import Client


from .models import Resume


class ResumeTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='secret'
        )

        self.resume = Resume.objects.create(
            description='A description',
            author=self.user,
        )

    def test_resume_content(self):
        self.assertEqual(f'{self.resume.description}', 'A description')
        self.assertEqual(f'{self.resume.author}', 'testuser')
    

    def test_resume_list_view(self):
        response = self.client.get(reverse('resumes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A description')
        self.assertTemplateUsed(response, 'resume/resumes.html')

   
    def test_my_resumes_view(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('my_resumes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A description')
        self.assertTemplateUsed(response, 'resume/my_resumes.html')

    def test_resume_create_view(self): 
        self.client.login(username='testuser', password='secret')
        response = self.client.post(reverse('resume_new'), {
            'description': 'New description',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Resume.objects.last().description, 'New description')
