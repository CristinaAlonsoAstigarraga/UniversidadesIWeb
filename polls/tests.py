import datetime

from django.test import TestCase
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
# Create your tests here.

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_preguntas_futuras(self):
        """
        was_published_recently() devuelve False en las preguntas que la fecha de publicación
        (pub_date) son en el futuro.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_preguntas_antiguas(self):
        """
        was_published_recently() devuelve False en las preguntas que la fecha de publicación
        (pub_date) son más antiguas que '1 día'.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_pregunta_reciente(self):
        """
        was_published_recently() devuelve True en las preguntas que la fecha de publicación
        (pub_date) son durante el último día.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
        """
        Eliminar parte de la repetición del proceso de creación de preguntas.
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        Si no existen preguntas, se muestra por pantalla "No hay encuestas disponibles"
        """
        respuesta = self.client.get(reverse('polls:index'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "No hay encuestas disponibles.")
        self.assertQuerysetEqual(respuesta.context['lista_pregunta_reciente'], [])

    def test_past_question(self):
        """
        Las preguntas con una fecha de publicación (pub_date) en el pasado, se muestran en la página index.
        """
        create_question(question_text="Pregunta pasada.", days=-30)
        respuesta = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            respuesta.context['lista_pregunta_reciente'],
            ['<Pregunta: Pregunta pasada.>']
        )

    def test_future_question(self):
        """
        Las preguntas con una fecha de publicación (pub_date) futura, NO se muestran en la página index.
        """
        create_question(question_text="Pregunta futura.", days=30)
        respuesta = self.client.get(reverse('polls:index'))
        self.assertContains(respuesta, "No hay encuestas disponibles.")
        self.assertQuerysetEqual(respuesta.context['lista_pregunta_reciente'], [])

    def test_future_question_and_past_question(self):
        """
        Aunque existan preguntas pasadas y futuras, solo se muestran las preguntas pasadas.
        """
        create_question(question_text="Pregunta pasada.", days=-30)
        create_question(question_text="Pregunta futura.", days=30)
        respuesta = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            respuesta.context['lista_pregunta_reciente'],
            ['<Question: Pregunta pasada.>']
        )

    def test_two_past_questions(self):
        """
        La página index puede mostrar múltiples preguntas.
        """
        create_question(question_text="Pregunta pasada 1.", days=-30)
        create_question(question_text="Pregunta pasada 2.", days=-5)
        respuesta = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            respuesta.context['lista_pregunta_reciente'],
            ['<Pregunta: Pregunta pasada 2.>', '<Pregunta: Pregunta pasada 1.>']
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        La vista de detalle de una pregunta con una fecha de publicación (pub_date) en
        el futuro, devuelve un error '404 not found'.
        """
        future_question = create_question(question_text='Pregunta futura question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 404)

    def test_past_question(self):
        """
        La vista de detalle de una pregunta con una fecha de publicación (pub_date) en
        el pasado, devuelve/muestra el texto de la pregunta.
        """
        past_question = create_question(question_text='Pregunta pasada.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        respuesta = self.client.get(url)
        self.assertContains(respuesta, past_question.question_text)