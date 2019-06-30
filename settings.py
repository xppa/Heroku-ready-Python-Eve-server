password = "zzxxcc111"
MONGO_URI = "mongodb+srv://kel:" + password + "@werf-11lw7.azure.mongodb.net/test?retryWrites=true&w=majority"


# По умолчанию Eve запускает API в режиме "read-only" (т.е. поддерживаются только GET запросы),
# мы включаем поддержку методов POST, PUT, PATCH, DELETE.
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

X_DOMAINS = '*'
X_HEADERS = '*'


DOMAIN = {
    # Описываем ресурс `/users`
    'users': {
        'schema': {
            'username': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 32,
                'required': True,
                # уникальное поле (индекс не создаётся, значение должно быть уникальным)
                'unique': True,
            },
			'email': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 32,
                'required': True,
                # уникальное поле (индекс не создаётся, значение должно быть уникальным)
                'unique': True,
            },
            'firstname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 10,
                'required': True,
            },
            'lastname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
                'required': True,
            },
            'born': {
                'type': 'datetime',
            },
            'active': {
                'type': 'boolean',
                'default': True
            },
			'sx': {
                'type': 'boolean',
                'nullable': 'True'
            },
            'preferences': {
                'type': 'list',  # тип: список
                'default': [],   # по умолчанию: пустой список
                # описываем "схему" списка
                'schema': {
                    'type': 'string',
                    'minlength': 5,
                    'maxlength': 32,
                }
            }
        }
    },

    # Описываем ресурс `/events`
    'events': {
        # Описываем модель данных
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 32,
                'required': True,
                'unique': True
            },
            'tags': {
                'type': 'list',
                'default': [],  # по умолчанию: пустой список
                # описываем "схему" списка
                'schema': {
                    'type': 'string',
                    'minlength': 5,
                    'maxlength': 32,
                }
             },
            'users': {
                'type': 'list',  # тип: список
                'default': [],  # по умолчанию: пустой список
                # описываем "схему" списка
                'schema': {
                    'type': 'objectid',  # тип данных: objectid
                    # ссылаемся на запись в другой коллекции
                    'data_relation': {
                        'resource': 'users',  # на ресурс `users` (который мы описали выше)
                        'field': '_id',  # на поле `_id`
                        'embeddable': True #разрешено встраивание модели
                    }
                }
            }
        }
    }
}