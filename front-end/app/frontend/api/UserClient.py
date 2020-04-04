from flask import session
import logging
import requests


class UserClient:


    @staticmethod
    def post_login(form):
        logging.debug('post_login()')
        api_key = False
        payload = {
            'username': form.username.data,
            'password': form.password.data,
        }
        url = 'http://user:5000/api/user/login'
        response = requests.request("POST", url=url, data=payload)
        if response:
            d = response.json()
            if d['api_key'] is not None:
                api_key = d['api_key']
        return api_key

    @staticmethod
    def does_exist(username):
        logging.debug(f'does_exist({username})')
        url = 'http://user:5000/api/user/'+username+'/exist'
        response = requests.request("GET", url=url)
        return response.status_code == 200

    @staticmethod
    def post_user_create(form):
        logging.debug('post_user_create()')
        user = False
        payload = {
            'email': form.email.data,
            'password': form.password.data,
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'username': form.username.data
        }
        url = 'http://user:5000/api/user/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            user = response.json()
        return user

    @staticmethod
    def get_user():
        logging.debug(f'post_user_create()')
        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }

        response = requests.request(method="GET", url='http://user:5000/api/user', headers=headers)
        user = response.json()
        return user
