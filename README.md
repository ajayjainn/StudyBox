# Study Box

StudyBox is a platform that promotes positive competition among friends. Anyone can create tasks which all of your friends are required to complete. You can also track your progress alongside your friends. View the tasks completed by others and gain inspiration from their achievements. The graph compares the number of tasks completed by all users. 

HTML-CSS along with Bootstrap framework is used on the frontend while Django is used on the backend. SQLite is used to persist data.

### Main features

* Registed and login securely.

* Create tasks.

* Complete your tasks while viewing the progress of your friends.

* Intuitive graph that compares the progress of all users.

* Build a healthy competition among your friends.

  
![image](https://github.com/ajayjainn/study-box/assets/64261776/b7988084-63a2-4328-b572-c68be5630d85)
![image](https://github.com/ajayjainn/study-box/assets/64261776/9fadbfb0-0d65-40a7-97e1-1b5f8b190213)
![image](https://github.com/ajayjainn/study-box/assets/64261776/cccfccec-19d9-45a8-8f9e-c6f4d4caa69c)




# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:ajayjainn/study-box.git
    $ cd study-box
    
Activate the virtualenv for your project.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

Once the server is hosted, head over to http://127.0.0.1:8000/ for the App.

Cheers and Happy Coding :)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
