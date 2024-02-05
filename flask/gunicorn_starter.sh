#!/bin/sh
# gunicorn main:app --chdir app -w 2 --threads 2 -b 0.0.0.0:8000 --reload


# gunicorn main:app -c "$PWD"/gunicorn.config.py

if [ "$FLASK_DEBUG" = "1" ]; then
    echo "Running on Flask Development Server"
    python3 main.py
else
    echo "Running on gunicorn"
    gunicorn main:app -c "$PWD"/gunicorn.config.py
fi
exec "$@"

