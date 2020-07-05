import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    q = Question.objects.create(question_text=question_text, pub_date=time)
    return q

class QuestionIndexViewTest(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('mc_poll:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Polls Found')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        create_question(question_text='Quel age as-tu?', days=-30)
        response = self.client.get(reverse('mc_poll:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Quel age as-tu?>']
        )

    def test_future_question(self):
        create_question(question_text='Ils vient du Future?', days=+30)
        response = self.client.get(reverse('mc_poll:index'))
        self.assertContains(response, 'No Polls Found')
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            []
        )

    def test_future_question_and_past_question(self):
        create_question(question_text='Are you from the future?', days=30)
        create_question(question_text='Are you from the past?', days=-30)
        response = self.client.get(reverse('mc_poll:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Are you from the past?>']
        )

    def test_two_past_question(self):
        create_question(question_text='Past tense?', days=-30)
        create_question(question_text='Another Past?', days=-20)
        response = self.client.get(reverse('mc_poll:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Another Past?>', '<Question: Past tense?>']
        )

class QuestionDetailsViewTest(TestCase):
    def test_future_question(self):
        fut_q =create_question(question_text="Am I from the future?", days=30)
        url = reverse('mc_poll:details', args=(fut_q.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_q = create_question(question_text="Am I from the past?", days=-30)
        url = reverse('mc_poll:details', args=(past_q.id,))
        response = self.client.get(url)
        self.assertContains(response, past_q.question_text)