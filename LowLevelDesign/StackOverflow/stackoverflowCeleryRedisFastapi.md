# Run the FastAPI application with Celery and Redis integration
# 
# This will run the FastAPI application and the Celery task for vote syncing in parallel.
# install postgres and run this
# brew install postgresql
# brew services start postgresql

# if on mac, create postgres table by running this
# createdb stack_overflow
# psql -d stack_overflow

# install redis on your mac by running this
# brew install redis
# brew services start redis
# check if the redis is running by running this
# redis-cli ping


# install celery by running this
# pip install celery
# run your app on celery by running this
# celery -A stackOverflow.celery_app worker --loglevel=info

# install fastapi by running this
# pip install fastapi
# run your app on fastapi by running this
# uvicorn stackOverflow.stackOverflow:app --host 0.0.0.0 --port 8000


# check out the api docs by opening this link
# http://127.0.0.1:8000/docs