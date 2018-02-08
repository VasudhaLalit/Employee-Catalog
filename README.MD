# Catalog Item

## Introduction
This is a Employee Catalog application developed using python flask.
It lists latest 10 employees on the home page. It also has department wise employee listing.  
Authentic users can create, update or delete records.

## Prerequisite
1. _Google Chrome_
2. _Virtual box_
3. _Vagrant machine_
4. _Python3.0_
5. _SQL Alchemy_
6. _Flask_
7. _Google account login_

## Installation
Step 1 - Install Virtual box
Install Virtual Box from https://www.virtualbox.org/.

Step 2 - Install and Setup vagrant machine
Install vagrant machine from https://www.vagrantup.com/.
Locate vagrantfile and run gitbash in that directory
Execute 'vagrant up' to set up vagrant machine
Run 'vagrant ssh'
change directory with 'cd /vagrant' command. 

Step 3 - Setup application
Execute below commands in sequence to setup database and load initial data.
1. python3 database_setup.py
2. python3 Department.py
3. python3 data_update.py
4. python3 userupdate.py

Step 4 - Run application
1. In same gitbash run python3 Employee.py
2. Open Google Chrome and load http://localhost:5000

## Execution 

Accessing localhost:5000 will load the Employee Catalog Home page.
You need to sign in with your google account to access the employee details.
You need to be signed in for Creating, Updating or Removing the record from the catalog.

## Author
#_**Vasudha Lalit**_

## References
1. Udacity