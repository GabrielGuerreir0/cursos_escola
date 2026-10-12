# 🎓 Escola API

API RESTful para gestão acadêmica de estudantes, cursos e matrículas, desenvolvida com **Django** e **Django REST Framework (DRF)**. A aplicação inclui controle granular de acessos, versionamento dinâmico de endpoints, documentação OpenAPI/Swagger interativa, ordenação, busca textual, throttles customizados e testes automatizados.

---

## 🚀 Principais Recursos

- **Gestão de Estudantes:** Operações completas de CRUD (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) com suporte a busca textual por nome/CPF e ordenação por nome.
- **Versionamento de API:** Suporte nativo a versões via query param (`?version=v2`), alternando automaticamente os serializers de estudantes (`EstudanteSerializer` vs `EstudanteSerializerV2`).
- **Gestão de Cursos:** CRUD completo com permissões `IsAuthenticatedOrReadOnly` (leitura pública, escrita restrita a usuários autenticados).
- **Controle de Matrículas:** Endpoints dedicados para vínculo de estudantes aos cursos, restritos aos métodos `GET` e `POST` com throttling dedicado via `MatriculaAnonRateThrottle`.
- **Relatórios & Listagens Aninhadas:**
  - Consulta de matrículas ativas por estudante (`/estudantes/{id}/matriculas/`).
  - Consulta de estudantes matriculados por curso (`/cursos/{id}/matriculas/`).
- **Throttling e Segurança:** Proteção contra requisições abusivas em camadas (global e por ViewSet), autenticação `BasicAuthentication` e permissões nativas do Django.
- **Documentação Interativa:** Swagger UI e ReDoc gerados automaticamente com suporte a schema mock (`swagger_fake_view`).
- **Carga de Dados (Mock):** Scripts utilitários prontos para popular a base de testes com a biblioteca `Faker`.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Framework:** [Django 5.2](https://www.djangoproject.com/)
- **API Toolkit:** [Django REST Framework 3.18](https://www.django-rest-framework.org/)
- **Documentação OpenAPI:** [drf-yasg](https://github.com/axnsan12/drf-yasg)
- **Filtros e Parâmetros:** [django-filter](https://django-filter.readthedocs.io/)
- **Segurança & CORS:** `django-cors-headers`
- **Validação de Documentos:** `validate-docbr`
- **Geração de Dados:** `Faker`
- **Banco de Dados:** SQLite (padrão de desenvolvimento)

---

## 📁 Estrutura do Projeto

```text
├── escola/
│   ├── migrations/          # Histórico de migrações do banco
│   ├── tests/               # Suíte de testes unitários e de integração
│   ├── admin.py             # Configurações do Django Admin
│   ├── models.py            # Modelos Estudante, Curso e Matricula
│   ├── serializers.py       # Serializers (padrão, V2 e aninhados)
│   ├── throttles.py         # Throttles customizados (ex: MatriculaAnonRateThrottle)
│   ├── validators.py        # Validações customizadas (CPF, telefone, etc.)
│   └── views.py             # ViewSets e Generic Views da aplicação
├── setup/
│   ├── settings.py          # Configurações de autenticação, paginação e throttle
│   ├── urls.py              # Roteamento central e rotas Swagger/ReDoc
│   ├── wsgi.py / asgi.py    # Interfaces de entrada WSGI/ASGI
├── popular_banco_cursos.py      # Script de carga inicial de cursos
├── popular_banco_estudantes.py  # Script de geração em lote de estudantes
├── db.sqlite3               # Base de dados local
├── manage.py                # Utilitário CLI do Django
├── requirements.txt         # Dependências do projeto
└── README.md
```

---

## ⚙️ Pré-requisitos

- **Python** (versão 3.10 ou superior recomendada)
- **Git**

---

## 🔧 Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações da base de dados:**
   ```bash
   python manage.py migrate
   ```

5. **(Opcional) Popule a base de dados com dados fictícios:**
   ```bash
   python popular_banco_cursos.py
   python popular_banco_estudantes.py
   ```

6. **Crie as credenciais de superusuário:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```
   A aplicação estará disponível em `http://127.0.0.1:8000/`.

---

## 📚 Documentação dos Endpoints

Com a aplicação em execução, acesse a documentação interativa gerada via `drf-yasg`:

- **Swagger UI:** `http://127.0.0.1:8000/swagger/`
- **ReDoc:** `http://127.0.0.1:8000/redoc/`
- **Admin do Django:** `http://127.0.0.1:8000/admin/`

---

## 📌 Guia de Endpoints

| Método | Endpoint | Descrição | Permissões / Regras |
|---|---|---|---|
| `GET` / `POST` | `/estudantes/` | Lista ou cadastra estudantes | Suporta busca `?search=` e ordenação `?ordering=name` |
| `GET` / `PUT` / `PATCH` / `DELETE` | `/estudantes/{id}/` | Detalhes, atualização ou exclusão de estudante | Serializer alternável via `?version=v2` |
| `GET` | `/estudantes/{id}/matriculas/` | Lista todas as matrículas de um estudante específico | Endpoint de leitura via `ListaMatriculaEstudante` |
| `GET` / `POST` | `/cursos/` | Lista ou cria novos cursos | Leitura aberta; escrita restrita a autenticados (`IsAuthenticatedOrReadOnly`) |
| `GET` / `PUT` / `PATCH` / `DELETE` | `/cursos/{id}/` | Detalhes, atualização ou exclusão de curso | `IsAuthenticatedOrReadOnly` |
| `GET` | `/cursos/{id}/matriculas/` | Lista todas as matrículas de um curso específico | Endpoint de leitura via `ListaMatriculaCurso` |
| `GET` / `POST` | `/matriculas/` | Consulta ou realiza matrículas | Métodos limitados a `GET` e `POST`; possui throttle anônimo e autenticado |

### 🔍 Filtros, Ordenação e Versionamento

- **Busca em Estudantes:**
  ```http
  GET /estudantes/?search=Silva HTTP/1.1
  GET /estudantes/?search=12345678901 HTTP/1.1
  ```
- **Ordenação alfabética:**
  ```http
  GET /estudantes/?ordering=name HTTP/1.1
  GET /estudantes/?ordering=-name HTTP/1.1
  ```
- **Versão da API:**
  ```http
  GET /estudantes/?version=v2 HTTP/1.1
  ```
- **Paginação:**
  ```http
  GET /estudantes/?limit=10&offset=20 HTTP/1.1
  ```

---

## 🧪 Testes Automatizados

Para executar os testes unitários e de integração configurados no app `escola`:

```bash
python manage.py test escola
```

---

## 📄 Licença

Este projeto é distribuído sob os termos da licença [MIT](LICENSE).