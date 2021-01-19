# MedicarAPI

## Como rodar

1. Após clonar o projeto, criar um virtual enviroment e ativa-lo
2. Instalar as dependências usando `pip install -r requirements.txt`
3. Rodar as migrações usando `python manage.py`
4. Rodar servidor usando `python manage.py runserver`
5. Criar um superuser usando `python manage.py createsuperuser`
6. Acessar os endpoints ou o gerenciador em `127.0.0.1:8000/admin/`
7. Todos o endpoints necessitam de autenticação.

## Sobre o projeto

Api para marcação de consulta (App Medicar) desenvolvido com Django Rest Framework para o Desafio Intmed.

## Endpoints

`GET /api/`
 
```json
{
    "especialidades": "http://127.0.0.1:8000/api/especialidades/",
    "medicos": "http://127.0.0.1:8000/api/medicos/",
    "agendas": "http://127.0.0.1:8000/api/agendas/",
    "consultas": "http://127.0.0.1:8000/api/consultas/"
}
```

`GET /api/especialidades/`
 
```json
[
    {
        "id": 1,
        "nome": "Pedriatria"
    },
    {
        "id": 2,
        "nome": "Ginecologia"
    },
    {
        "id": 3,
        "nome": "Cardiologia"
    },
    {
        "id": 4,
        "nome": "Clinico Geral"
    }
]
```

`GET /api/medicos/`  
Filtragem por `GET /api/medicos/?especialidade=4&nome=Dr`
 
```json
[
    {
        "id": 1,
        "nome": "Drauzio Varella",
        "crm": "3711",
        "especialidade": {
            "id": 4,
            "nome": "Clinico Geral"
        }
    },
    {
        "id": 2,
        "nome": "House",
        "crm": "12345",
        "especialidade": {
            "id": 1,
            "nome": "Pedriatria"
        }
    },
    {
        "id": 3,
        "nome": "Osvaldo Cruz",
        "crm": "12345",
        "especialidade": null
    }
]
```

`GET /api/agendas/`  
 
```json
[
    {
        "id": 1,
        "medico": 1,
        "dia": "2021-01-16",
        "horarios": [
            {
                "hora": "08:00:00"
            },
            {
                "hora": "09:00:00"
            }
        ]
    }
]
```


`GET /api/consultas/`  
Filtragem por `http://127.0.0.1:8000/api/consultas/?dia=2021-01-17`
 
```json

[
    {
        "id": 1,
        "dia": "2021-01-17",
        "horario": "08:00:00",
        "data_agendamento": "2021-01-17T02:43:56.785677Z",
        "medico": {
            "id": 1,
            "nome": "Drauzio Varella",
            "crm": "3711",
            "especialidade": {
                "id": 4,
                "nome": "Clinico Geral"
            }
        }
    }
]
```
