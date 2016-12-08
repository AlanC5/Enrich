# Enrich #

## Purpose ##
Enrich is a tool for seamlessly finding enrichment programs. We understand that for many parents, discovering after-school programs can be difficult; often they rely on word of mouth and don't have a good way of seeing how reputable they are. Enrich changes that by offering a platform for parents and organizers to connect, and for people who send their kids to these enrichment programs to rate how they are. Finding the programs should be the easy part.



## Contributors:

- Product Owner: Khadeeja Din
- SCRUM Master: Alan Chen
- Dev: Samuel Cohen
- Dev: Anthony Shalagin


## Developer Guide 
Do this before running tests, coverage, or pylint.

git clone git@bitbucket.org:AlanCTW/enrich.git

pip install -r requirements.txt 

python manage.py runserver

## Deployment on Heroku:
https://ancient-lowlands-74290.herokuapp.com/

## Suggested Browser:
Google Chrome

## Testing and Coverage:
python manage.py test
coverage report

## Pylint:
Please run the following line below on all of our apps.

pylint --load-plugins=pylint_django ./* --rcfile .pylintrc