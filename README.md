# Graph ql assignment by Saif Ali Khan

## naming conventions followed
* variable, files and folders :- snake_case
* classes and names :- CamelCase
Follow the Steps below to set up the project locally

* pip install -r requirements.txt
* Update the .env file with the required credentials 

## Steps to run the project
- Before pushing your changes to the remote repo do `git pull` from the concerned branch to ensure if there's any update on the branch to avoid getting into merge conflicts.
- Install all the dependencies and packages required for the project by `pip install -r requirements.txt`
- Add any additional libraries you have installed to `requirements.txt`.t
- to run it via terminal `uvicorn main:app --reload`
- Run docker command `docker compose -f docker/docker-compose.yml up -d` to run inside docker container