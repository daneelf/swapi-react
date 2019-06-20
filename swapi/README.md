# Swapi-react

This is my first attempt to interact with React.
I fetch the list of Star Wars movies. You can get the Species that were into the movies and filter by species the characters.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This a full-stack project based on Python Django and React. 
You will need to have Python and pip installed and create a virtual enviroment to run the django project.

Linux based systems(this is for Ubuntu):
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-18-04-quickstart#step-6-%E2%80%94-create-a-virtual-environment

Windows:
https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/

You will need to have Node.js installed on your computer for the frontend section.
https://www.taniarascia.com/how-to-install-and-use-node-js-and-npm-mac-and-windows/

### Installing

Once you have your your pip installed and the virtualenv running you can go ahead and just execute the folloing command:

```pip install -r requirements.txt```

ALso you need to install the frontend packages: 

navigate to:

```/swapi-react/swapi/frontend```

and then

```npm install```

After all the dependencies are installed in order to run the project you should execute the folloing steps:


navigate to:

``` /swapi-react/swapi``` 

run the following command:

```python manage.py runserver```

In a different terminal navigate to 

```/swapi-react/swapi/frontend```

and then run the following command: 

```npm run start```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [React](https://reactjs.org/) - Dependency Management



## Authors

* **Danae Vogiatzi** 

