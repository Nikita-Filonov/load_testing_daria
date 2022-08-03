"""
Используя locust написать нагрузочный сценарий для создания, обновления и удаления курса

1. Создаем курс http://46.101.117.86/docs#/courses/create_course_view_api_v1_courses__post
2. Обновляем курс http://46.101.117.86/docs#/courses/update_course_view_api_v1_courses__course_id___patch
3. Удаляем курс http://46.101.117.86/docs#/courses/delete_course_view_api_v1_courses__course_id___delete

Также необходимо учесть, что id курса нужно передавать через переменные

Для примера можно взять нагрузку в 50 пользователей
Сценарий нужно расположить в папке scenarios/courses/
"""