from django.test import TestCase
from django.urls import reverse
from .models import Club

class ClubTests(TestCase):
    def setUp(self):
        # Create a sample club for testing
        self.club = Club.objects.create(
            name="Chess Club",
            description="A club for chess enthusiasts.",
            city="Hanover",
            country="USA",
            contact_email="chess@school.edu"
        )

    def test_club_list_view_status_code(self):
        # Test that the club list page loads correctly
        url = reverse('club_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_club_list_view_content(self):
        # Test that the club list page shows the club's name
        url = reverse('club_list')
        response = self.client.get(url)
        self.assertContains(response, self.club.name)

    def test_add_club(self):
        # Test creating a new club via POST
        url = reverse('add_club')
        data = {
            'name': 'Debate Club',
            'description': 'For debating skills.',
            'city': 'Hanover',
            'country': 'USA',
            'contact_email': 'debate@school.edu'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect to club_list
        self.assertTrue(Club.objects.filter(name='Debate Club').exists())


    def test_delete_club(self):
        # Test deleting a club
        url = reverse('delete_club', args=[self.club.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirect to club_list
        self.assertFalse(Club.objects.filter(id=self.club.id).exists())
