# Omnitrix Web Project

#### Video Demo:  <https://youtu.be/Ar0IfSA0tNU>

#### Description:


## Overview

The Omnitrix Web Project is a web application inspired by the Omnitrix from the Ben 10 series. This project aims to provide an interactive and engaging platform where users can explore various aliens from the Omnitrix and share their favorite alien with the world. The application is built using Flask for the backend and Bootstrap for the frontend, ensuring a responsive and user-friendly experience.

## Project Structure

### 1. `app.py`

This is the main application file that initializes the Flask app and defines the routes for the web application. It includes the following key components:

- **Initialization**: Configures the Flask application and sets up session management.
- **Routes**: Defines routes for different pages, such as the homepage, individual alien pages, and the form submission page.
- **Database Integration**: Uses the CS50 SQL library to interact with an SQLite database, storing user submissions.

### 2. `templates/`

This directory contains all the HTML templates used in the project. Each template corresponds to a different route defined in `app.py`.

- **`index.html`**: The homepage of the application, providing an omnitrex semulation and navigation to other pages.
- **`heatblast.html`, `wildmutt.html`, etc.**: Individual pages for each alien, displaying relevant information and images.
- **`favorite.html`**: A form where users can submit their favorite alien, along with a display of all submissions.
- **`apology.html`**: A template used to display error messages to the user.

### 3. `static/`

This directory contains all the static files, including CSS, JavaScript, sounds and images.

- **`styles.css`**: Custom CSS file for styling the application.
- **`java.js`**: JavaScript file containing functions for interactive elements, such as the sidebar menu.
- **Images**: Various images used throughout the application, stored in the `static` directory.
-**Sounds**: Various sounds used throughout the application, stored in the `static` directory.

### 4. `requirements.txt`

This file lists all the dependencies required for the project. It ensures that anyone who clones the repository can install the necessary packages using `pip`.

## Design Choices

### Flask for Backend

Flask was chosen for its simplicity and flexibility. It allows for quick development and easy integration with other libraries, such as the CS50 SQL library for database management. Flask's routing system is straightforward, making it easy to define and manage different pages of the application.

### Bootstrap for Frontend

Bootstrap was selected to ensure a responsive and visually appealing design. Its grid system and pre-built components make it easy to create a layout that works well on both desktop and mobile devices. Custom CSS was added to further enhance the design and match the theme of the Omnitrix.

### Database Integration

The application uses SQLite for storing user submissions. The CS50 SQL library was chosen for its simplicity and ease of use. The database schema includes a `users` table to store usernames and their favorite aliens. This allows for easy retrieval and display of user submissions.

### Form Handling and Validation

The form on the "Your favourite alien" page includes validation to ensure that all fields are filled out correctly. If a user tries to submit the form without entering a name or selecting an alien, an error message is displayed using the `apology` function. This ensures a smooth user experience and prevents incomplete submissions.

### Interactive Elements

JavaScript is used to add interactivity to the application. For example, the sidebar menu can be opened and closed using JavaScript functions. Additionally, sound effects are played when users interact with certain elements, enhancing the overall experience.

## Future Enhancements

There are several potential enhancements that could be made to the project:

- **User Authentication**: Adding user authentication would allow users to create accounts and save their favorite aliens.
- **More Aliens**: Expanding the list of aliens and providing more detailed information about each one.
- **Enhanced Interactivity**: Adding more interactive elements, such as animations and additional sound effects.
- **Improved Design**: Further refining the design to make it even more visually appealing and user-friendly.

## Conclusion

The Omnitrix Web Project is a fun and interactive application that allows users to explore the world of the Omnitrix and share their favorite aliens. By combining Flask and Bootstrap, the project provides a responsive and engaging experience. The detailed documentation and clear structure make it easy for others to understand and contribute to the project.


## Contact

For any questions or suggestions, please contact [mahmros20fe4g@gmail.com].

