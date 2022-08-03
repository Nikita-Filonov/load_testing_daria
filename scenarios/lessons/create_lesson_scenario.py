"""
https://locust.io/

http://46.101.117.86/docs#/lessons

Темы:
   - Использование task
   - on_start, on_stop
   - Шаринг переменных
   - Разные файлы для разных сценариев
   - Улучшение работы с client, locust.contrib.fasthttp.FastHttpSession + авторизация + кеширование
"""
from base.base import BaseTaskSet
from locust import HttpUser, between, task


class CreateLessonScenario(BaseTaskSet):
    wait_time = between(5, 10)
    lesson = None
    token = None

    def on_start(self):
        print('getting token')
    
    def on_stop(self):
        print('logout')
    
    @task(1)
    def get_lessons(self):
        self.get('/api/v1/lessons/')
    
    @task(1)
    def create_lesson(self):
        payload = {
            "title": "string"
        }
        lesson = self.post('/api/v1/lessons/', json=payload)
        self.lesson = lesson.json()

    @task(1)
    def update_lesson(self):
        self.patch(f'/api/v1/lessons/{self.lesson["id"]}')

class LessonWorkflow(HttpUser):
    wait_time = between(5, 10)
    tasks = {CreateLessonScenario: 1}
