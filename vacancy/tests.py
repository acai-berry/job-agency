from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.test.client import Client


from .models import Vacancy


class VacancyTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            username='testuser',
            password='secret'
        )

        self.vacancy = Vacancy.objects.create(
            description='A description',
            author=self.user,
        )

    def test_vacancy_content(self):
        self.assertEqual(f'{self.vacancy.description}', 'A description')
        self.assertEqual(f'{self.vacancy.author}', 'testuser')
    

    def test_vacancy_list_view(self):
        response = self.client.get(reverse('vacancies'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A description')
        self.assertTemplateUsed(response, 'vacancy/vacancies.html')

   
    def test_my_vacancies_view(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('my_vacancies'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A description')
        self.assertTemplateUsed(response, 'vacancy/my_vacancies.html')

    def test_vacancy_create_view(self): 
        self.client.login(username='testuser', password='secret')
        response = self.client.post(reverse('new_vacancy'), {
            'description': 'New description',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Vacancy.objects.last().description, 'New description')