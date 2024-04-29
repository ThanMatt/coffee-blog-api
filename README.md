## Getting Started

First, run the development server:

### Installation

```bash

# :: Thru docker

$ docker network create coffee-blog

$ sh setup-dev.sh

# :: Thru venv

$ source venv/bin/activate.fish

$ pip install -r requirements.txt
```

### Migrations (for non docker)

```
$ python manage.py migrate
```

### To run

```bash

# :: Thru docker

$ docker compose up

# :: Thru venv

$ python manage.py runserver 0.0.0.0:8000
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
