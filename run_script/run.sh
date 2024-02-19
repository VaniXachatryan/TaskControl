#!/bin/bash
# можно конечно опрашивать доступость бд каждую секнуду, но кому это надо, правильно?)

sleep 5

alembic upgrade head

uvicorn src.main:app --host 0.0.0.0 --port 80