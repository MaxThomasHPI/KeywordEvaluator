# KeywordEvaluator
Let users evaluate keywords in an A/B test. This web app is 
based on a database storing keywords assigned to MOOCs by 
the respective course administrators and teachers and 
automatically generated keywords by a large language model
().

Every user is asked at the beginning to give some general 
data about him or her (age, gender, occupation). This is 
purely voluntary. The user is presented with a course title 
and a course description. Additionally, tow lists of keywords 
are shown to the user. The user chooses one of the lists.
The data about the choice is stored in a database the
background. After 10 iterations the survey has ended and the 
user can close the browser.

The results are used for academic research only.


# Setup

The following requirements must be fulfilled:
- OS: Ubuntu 22.04
- Python 3.10
- git (latest)
- PostgreSQL (Version 14 or higher) 
- docker (Version 24 or higher) and docker compose


## Install prerequisites

Upgrade your system:
````
sudo apt update && sudo apt upgrade -y
````

Install git for downloading the source code:
````
sudo apt install git
````

Install PostgrSQL as database management system:

````
sudo apt install postgresql
````

Install Docker for managing containers:

````
# from https://docs.docker.com/engine/install/ubuntu/
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
````


## Build the application

Create new directory for the app, if needed

````
mkdir Programs
cd Programs
````

Clone source code from GitHub using git

````
git clone https://github.com/MaxThomasHPI/KeywordEvaluator.git
````

In the root folder run

````
sudo docker compose up --build
````


## Setting the seed for the database

When the app is deployed the first time, 
the database needs to be fed with the course
titles, descriptions, and manual and generated
keywords. The corresponding script has to be 
run inside the container.

In a second terminal while the app is running,
open a bash in the container environment

````
sudo docker compose exec web bash
````

Inside the container run

````
python3 -m app_data.database.populate_db
````

After the database is populated the terminal can be 
closed.

The setup of the web app is now finished.

# Starting the application

The app should already be running after the setup if
the following command was used:

````
sudo docker compose up --build
````

If the container was stopped it can be run again
with:

````
sudo docker compose up
````

By default, the app listens to port 80. This means
that opening the browser and accessing 127.0.0.1 will
directly result in a forwarding to the web app.

