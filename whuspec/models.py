#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import string
from hashlib import md5
from random import choice
from torext.mongodb import Document, Struct, ObjectId
from whuspec.database import db


CHARS = string.letters + string.digits


def random_string(length=10):
    return ''.join([choice(CHARS) for i in range(length)])


def md5_string(s):
    if isinstance(s, unicode):
        s = s.encode('utf8')
    return md5(s).hexdigest()


class Skill(Document):
    col = db['skill']
    __validate__ = False
    struct = Struct({
        'parents': [
            {
                'id': ObjectId,
            }
        ],
        'name': str,
        'description': str,
        'top_level': int,
        'course_id': ObjectId,
    })


class Speciality(Document):
    col = db['speciality']
    __validate__ = False
    struct = Struct({
        # Nearest skills
        'skills': [
            {
                'id': ObjectId
            }
        ],
        'name': str,
        'description': str,
        'creator_id': ObjectId,
        'created_at': datetime.datetime,
    })


class Course(Document):
    col = db['course']
    __validate__ = False
    struct = Struct({
        'name': str,
        'description': str,
    })


class User(Document):
    col = db['course']
    __validate__ = False
    struct = Struct({
        'username': str,  # Ignore case when validating
        'raw_username': str,
        'password': str,
        'password_reset_token': str,
        'signature': str,
        'email': str,
        'gender': str,
        'created_at': datetime.datetime,
        'role': int,

        # School information
        'student_number': str,

        # skills and specs
        'learning_skill_ids': [],
        'learning_specs_ids': [],
        'marked_skill_ids': [],
        'marked_specs_ids': []
    })

    @classmethod
    def create(cls, email, username, password, gender, role):
        signature = cls.generate_signature()
        ins = cls.new(
            username=username.lower(),
            raw_username=username,
            password=cls.generate_password(password, signature),
            signature=signature,
            email=email,
            gender=gender,
            created_at=datetime.datetime.now(),
            role=role
        )
        ins.save()
        return ins

    def reset_password(self, new_password):
        signature = self.generate_signature()
        self.update_doc(
            {
                '$set': dict(
                    signature=signature,
                    password=self.generate_password(new_password, signature)
                )
            }
        )

    @staticmethod
    def generate_signature():
        return random_string(12)

    @staticmethod
    def generate_password(raw_password, signature):
        return md5_string(signature + raw_password)

    def check_password(self, raw_password):
        return self['password'] == self.generate_password(raw_password, self['signature'])
