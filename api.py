import json
import requests
import uuid

class Pets:
    """API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Запрос к Swagger для получения уникального токена при входе в систему с валидными email и password"""
        data = {'email': 'olga12345@test.com',
                'password': '12345test'}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        user_id = res.json()['id']
        status = res.status_code
        print(res.json())
        return my_token, user_id, status

    def post_register_delete_user(self) -> json:
        email = uuid.uuid4().hex
        data = {"email": f'volha@{email}.com',
                "password": '12345test', "confirm_password": '12345test'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json().get('id')
        my_token = res.json()['token']
        headers = {'Authorization': f'Bearer {my_token}'}
        params = {'id': my_id}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers, params=params)
        status = res.status_code
        return status

    def get_list_users(self) -> json:
        """Запрос к Swagger для получения списка пользователей, зарегистрированных на сайте"""
        my_token = self.get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        my_status = res.status_code
        user_id = res.text
        return my_status, user_id

    def post_pet(self) -> json:
        """ Запрос к Swagger для добавления нового питомца """
        my_token = self.get_token()[0]
        user_id = self.get_token()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {

            "name": "Pushok",
            "type": "cat",
            "age": 5,

            "owner_id": user_id

        }
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def post_pet_photo(self):
        """ Запрос к Swagger для добавления фото питомца """
        my_token = self.get_token()[0]
        pet_id = self.post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('picturecat.jpg', open('C:\\Users\\Olga\\PycharmProjects\\Tests_API\\tests\\photo\\hari_picture.jpg', 'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def get_pet_id(self):
        """ Запрос к Swagger для получения id питомца """
        my_token = self.get_token()[0]
        pet_id = self.post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        pet_id = res.json()
        return pet_id, status

    def delete_pet(self):
        """ Запрос к Swagger для удаления питомца """
        my_token = self.get_token()[0]
        pet_id = self.post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def patch_pet(self):
        """ Запрос к Swagger для изменения информации об уже добавленном питомце """
        my_token = self.get_token()[0]
        user_id = self.get_token()[1]
        pet_id = self.post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "id": pet_id,
            "name": "Snezhok",
            "type": "cat",
            "owner_id": user_id
        }
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def put_pet_like(self):
        """ Запрос к Swagger для добавления лайка профилю питомца """
        my_token = self.get_token()[0]
        pet_id = self.post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status

    def put_pet_comment(self):
        """ Запрос к Swagger для добавления комментария к профилю питомца """
        my_token = self.get_token()[0]
        user_id = self.get_token()[1]
        pet_id = self.post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "pet_id": pet_id,
            "date": "2023-02-28T12:07:43.093Z",
            "message": "Nice cat!",
            "user_id": user_id,
            "user_name": "olga2202@test.com"
        }
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def get_token_invalid_pw(self) -> json:
        """Запрос к Swagger для получения уникального токена при входе в систему с валидным email и невалидным password"""
        data = {'email': 'olga12345@test.com',
                'password': '1234test'}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        status = res.status_code
        detail = res.json()['detail']
        return status, detail

    def get_token_invalid_email(self) -> json:
        """Запрос к Swagger для получения уникального токена при входе в систему с невалидным email и валидным password"""
        data = {'email': 'olga12345test.com',
                'password': '1234test'}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        status = res.status_code
        detail = res.json()['detail']
        return status, detail





