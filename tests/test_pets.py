from api import Pets


pet = Pets()


def test_get_token():
    token = pet.get_token()[0]
    status = pet.get_token()[2]
    assert token
    assert status == 200


def test_post_register_delete_user():
    status = pet.post_register_delete_user()
    assert status == 200


def test_get_list_users():
    status = pet.get_list_users()[0]
    my_id = pet.get_list_users()[1]
    assert status == 200
    assert my_id


def test_post_pet():
    status = pet.post_pet()[1]
    pet_id = pet.post_pet()[0]
    assert status == 200
    assert pet_id


def test_post_pet_photo():
    status = pet.post_pet_photo()[0]
    link = pet.post_pet_photo()[1]
    assert status == 200
    assert link


def test_get_pet_id():
    status = pet.get_pet_id()[1]
    pet_id = pet.get_pet_id()[0]
    assert status == 200
    assert pet_id


def test_delete_pet():
    status = pet.delete_pet()
    assert status == 200


def test_patch_pet():
    status = pet.patch_pet()[1]
    pet_id = pet.patch_pet()[0]
    assert status == 200
    assert pet_id


def test_put_pet_like():
    status = pet.put_pet_like()
    assert status == 200


def test_put_pet_comment():
    status = pet.put_pet_comment()
    assert status == 200


def test_get_token_invalid_pw():
    status = pet.get_token_invalid_pw()[0]
    detail = pet.get_token_invalid_pw()[1]
    assert status == 400
    assert detail == 'Username is taken or pass issue'


def test_get_token_invalid_email():
    status = pet.get_token_invalid_pw()[0]
    detail = pet.get_token_invalid_pw()[1]
    assert status == 400
    assert detail == 'Username is taken or pass issue'

