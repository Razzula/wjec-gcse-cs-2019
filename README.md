# WJEC GCSE Computer Science Unit 3 Controlled Assessment
This is my GCSE CA from 2019.

Uses Python 3.4.4.
Below is the original README from submission
<hr>
RUN IN CMD INTERFACE AND NOT THE IDLE! The cls() function won't work otherwise, and the breaker() function won't be fitted to the screen.
Font should be SIZE 16 for breaker() function to work properly.

Only one user exists by default:
	User:     admin
	Password: root

Only two texts exists by default
	Name    : Test
	Age     : 16
	Keywords: Test, Example

	Title   : Evaluation
	Age     : 16
	Keywords: Evaluation, Report, Test 

The ages (16) and keywords (Test) are the same to demonstrate how searching through for multiple items works.

All logins are stored in the 'logins' folder
All texts are stored in the 'texts' folder

Some comments reference lines numbers. The line numbers may not be exact, but are in close proximity (due to code changing).
I’ve tried to correct them as much as possible but may have missed some.

The program will only allow texts of over 100 words.
This is due to external research of the ARI formula, where I discovered this was required, as too short texts can generate negative reading ages.

Extra Features: Login w/ Username/Password System
		Can add new users
		Can change passwords of users (if logged in as Admin or said user)
		Can display all texts without search
		Can search for a file directly, by name
		A verification system to prompt the user to ask if they want to continue
		Checks

If the password system breaks for some reason, create a .txt file called 'ADMIN' in the 'logins' folder with 'd25e3e333b385d98bd5bc90da9fd1a7247b08bd37bd4f3cafddd6dc193d1e6b57119013589c15bf158d1f79c08da7d8b269d715827e90c10128200d83b4c3cba' in it. The password for that login will be root.