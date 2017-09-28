from django.test import TestCase
from tasks.test_factory import TaskFactory
from tasks import views
from tasks.models import Tasks


class TestViews(TestCase):

    def test_list_tasks_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks.html')

    def test_create_tasks_post(self):
        number_of_tasks = Tasks.objects.all().count()
        response = self.client.post(
            '/create/',
            {
                'title': 'My Task Title',
                'label': Tasks.URGENT,
            }
        )
        task_created = Tasks.objects.all().last()

        self.assertEqual(task_created.title, 'My Task Title')
        self.assertEqual(task_created.label, Tasks.URGENT)
        self.assertEqual(number_of_tasks+1, Tasks.objects.all().count())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_create_tasks_get(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 403)

    def test_update_task_post(self):
        # This is really cool, if you work with factory
        # You can just call create() and get the defaults values or
        # You can specify some value :)
        task = TaskFactory.create(title='Old Title')
        response = self.client.post(
            '/update-task/',
            {
                'task_id': task.pk,
                'title': 'New Title',
            }
        )
        # Lets refresh or object from database
        task.refresh_from_db()
        self.assertEqual(task.title, 'New Title')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_update_task_get(self):
        response = self.client.get('/complete-task/')
        self.assertEqual(response.status_code, 403)


    def test_complete_task_post(self):
        task = TaskFactory.create(
            title='This task is not done yet',
            completed=False,
        )
        response = self.client.post(
            '/complete-task/',
            {
                'task_id': task.pk,
            }
        )
        # Lets refresh or object from database
        task.refresh_from_db()
        self.assertTrue(task.completed)
        self.assertEqual(response.status_code, 200)

    def test_complete_task_get(self):
        response = self.client.get('/complete-task/')
        self.assertEqual(response.status_code, 403)

    def test_delete_task_post(self):
        task = TaskFactory.create(
            title='This task is not deleted yet',
        )
        response = self.client.post(
            '/delete-task/',
            {
                'task_id': task.pk,
            }
        )
        shold_be_empty = Tasks.objects.filter(
            pk=task.pk, title="This task is not deleted yet",
        )
        self.assertEqual(len(shold_be_empty), 0)
        self.assertEqual(response.status_code, 200)

    def test_delete_task_get(self):
        response = self.client.get('/delete-task/')
        self.assertEqual(response.status_code, 403)

    def test_archive_task_post(self):
        task = TaskFactory.create(
            title='This task is not archived yet',
            archived=False,
        )
        response = self.client.post(
            '/archive-task/',
            {
                'task_id': task.pk,
            }
        )
        # Lets refresh or object from database
        task.refresh_from_db()
        self.assertTrue(task.archived)
        self.assertEqual(response.status_code, 200)

    def test_archive_task_get(self):
        response = self.client.get('/archive-task/')
        self.assertEqual(response.status_code, 403)
