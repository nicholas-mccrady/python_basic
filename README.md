# python_basic
This project is multi repository demonstration of the core python modules and concepts.

first we created a git hub repository using a python git ignore and we included a read me.
next we need to run the command "git config --global credential.helper wincred" (this identifies your matching and you wont be able to do commits without running it)
next we need to config our global email and username by running these two commands
"git config --global user.email (youremail@email.com"
"git config --global user.name (your githubusername)" note to enter the code exactly as it appears the user.blank is a setting not a fill in
next we need to open a git bash terminal to the directory or folder that we want our project to be cloned to 
next we cloned the repository to our work environment using command "git clone (copy and paste web site url here)" noting that we double checked that our work went to the proper directory or folder that we wanted to work in 
then we want to open the project folder and we want to view the hidden items so that we can see the git ignore folder
next we created a .py file named main to start working with our code and made a print function to make sure that our compiler is up and running properly
our next step is to add the files that we need to our get ignore we do this by creating a folder named "keys" but it can be any name that you want and we created a apikeys.json file and typed a statement that we want to add to the git ignore to demonstrate this example
then we run the git status command after we add the apikeys file to the keys folder and now the bash sees it
next we open the git ignore with some type of editor sut as note++ or just open it in viscode
next you scroll to the bottom of the gitignore file and add the "keys\"or the folder you are adding and then save the changes
next we will do a get status command again and we will see that bash is no longer tracking that folder
this is used to keep api keys and passwords from being accessed by unauthorized people
