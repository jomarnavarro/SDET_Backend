# SDET-test
## Challenge
Create pilot Java test framework for testing NASA's open API.

NASA has an open API: https://api.nasa.gov/index.html#getting-started. It grants access to different features e.g: Astronomy Picture of the Day, Mars Rover Photos, etc.

We would like to test different scenarios that the API offers:
1. Retrieve the first 10 Mars photos made by "Curiosity" on 1000 Martian sol.
2. Retrieve the first 10 Mars photos made by "Curiosity" on Earth date equal to 1000 Martian sol.
3. Retrieve and compare the first 10 Mars photos made by "Curiosity" on 1000 sol and on Earth date equal to 1000 Martian sol.
4. Validate that the amounts of pictures that each "Curiosity" camera took on 1000 Mars sol is not greater than 10 times the amount taken by other cameras on the same date.

## Instructions
You will need to fork the repository and build the solution in Github **publicly**. Once you are finished, let HR know and share a link to your fork or a Zip file with your solution and the URL of the repository.

Implementation deadline is 3 days. Please let us know the time that you spent to achieve the task.

##Solution

The api tests were implemented using pytest instead of java as an exercise of personal gain (I've already implemented java frameworks, but not python ones for API).  

It has been dockerized to allow the user to run it without worrying about the dependencies.  I uploaded it to dockerhub (omarnavarro/nasa-api).  In order to run it, one must only setup an environment variable in the 'docker-compose.yml' file:  NASA_API_KEY.


