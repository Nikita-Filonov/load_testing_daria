"""
https://locust.io/

http://46.101.117.86/docs#/lessons
"""
from locust import HttpUser, SequentialTaskSet, between, task


class CreateLessonScenario(SequentialTaskSet):
    wait_time = between(5, 10)
    
    @task(1)
    def answer_question(self):
        self.client.get('/api/v1/lessons/')

class LessonWorkflow(HttpUser):
    wait_time = between(5, 10)
    tasks = {CreateLessonScenario: 1}
