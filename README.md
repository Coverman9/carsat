<div align="center">
  <h1><img src="https://media.giphy.com/media/JWKu8gbMby8De/giphy.gif" width="65px">
  Welcome to Carsat <img src="https://media.giphy.com/media/lCoX64okzbQsg/giphy.gif" width="65px"></h1>
</div>

[Carsat](https://carsat-emir.onrender.com/) is a car retail application, built using Python Flask, JavaScript, React, Redux and PostgresSQL.

## Technologies

- React/Redux
- Python
- Flask
- SQLAlchemy
- PostgresQL
- AWS


## Features

#### Splash Page
<img src="https://carsat-aws.s3.us-east-2.amazonaws.com/ezgif-2-98ffd8901c.gif" width="1000px">


#### Main Page
<img src="https://carsat-aws.s3.us-east-2.amazonaws.com/ezgif-2-f44a5ba036.gif" width="1000px">

#### Database Schema

![db](https://carsat-aws.s3.us-east-2.amazonaws.com/238710367-77dd3d16-18dd-4f38-9dbe-7a56dc8bb603.png)

#### Authentication

- Users can sign up
- Users can log in
- Users can log in as a demo user
- ![db](https://github.com/nasanov/numizmat/blob/main/docs/login.png)

#### Cars

- Users are able to create a car using the Add car button on the navbar
- Users are able to edit and delete the cars on the particular car details page
- Users can only delete cars that they own
- Users are able to add the car to the wishlist using the `Add to wishlist` button

#### Car detail
<img src="https://carsat-aws.s3.us-east-2.amazonaws.com/7obw5m.gif" width="1000px">

#### Search / Filter

- Users are able to search for the cars using the search input field on the navigation bar
- Users are able to search only for cars that were created by admin user or by themselves
- Users are able to filter by name using the input field on the sidebar
- Users are able to filter coins by make, model, year and color

## Future Implementations

- Live chat so users will be able to talk to each other in one chat room
- Filtering By multiple columns
- Pagination for the main page
- User Profile
- News section with parsed news from different gov mint websites
- Add light mode

## Installation

This project can be run by following these steps:

- Clone the repo into your desired folder.
- Run `pipenv install` from the root project directory.
- Run `npm install` from the react-app directory
- Create a .env file in the root directory (use .env.example).
- Run `pipenv shell` command
- Run `flask run` command from the root directory and `npm start` from the react-app directory

For additional information, checkout project's [Wiki](https://github.com/Coverman9/carsat/wiki) page.

> Developed By: [Emir Usubaliev](https://github.com/Coverman9)

<img src="https://media.giphy.com/media/s9kqO10sLE9smNFM8V/giphy.gif"><img src="https://media.giphy.com/media/s9kqO10sLE9smNFM8V/giphy.gif"><img src="https://media.giphy.com/media/s9kqO10sLE9smNFM8V/giphy.gif">
