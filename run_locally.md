# Running the project locally

## Clone Repo
`git clone https://github.com/snghnishant/Techbooks.git`
## Installing Python 
- Go to [Python](python.org) and install python with add to path option, Recommended version 3.8.1.
## Setting up python package manager
- Open cmd as admin and update pip -
`python -m pip install --upgrade pip`
## Setting up virtual environment 
0. Check installed packages to verify if virtul envt is not installed - `pip list`
1. Install virtual envt - `pip3 install virtualenvwrapper-win`
2. Create virtul envt - `mkvirtualenv envt_name`
3. List virtual envt - `workon`
4. Select a virtual envt - `workon envt_name`
- Deactivate current active virtual envt - `deactivate`
- Remove a virtual envt - `rmvirtualenv envt_name`

> Activate virtual enviroment before moving onto next installation steps by using command `workon envt_name`

## Installing Django and other dependencies
1. Install - `pip install django`
2. Check version - `python -m django --version`
3. Install - `pip install dj-database-url`
4. Install - `pip install Pillow`

## Run project
1. Go to folder root- Techbooks
2. Run cmd prompt, run command (replace 'your_virtual_envt_name' with your created virtual environmant name, list it using command `workon`) - `workon your_virtual_envt_name`
> For first time running the project
- `python manage.py makemigrations` for registering models to the admin dashboard
- `python manage.py migrate` applies migration in previous step
- `python manage.py createsuperuser` create superuser for admin login
3. Run Project - `python manage.py runserver`
