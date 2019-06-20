# E-TSHIRT-STORE

[![Maintainability](https://api.codeclimate.com/v1/badges/bb34ba25ecfdf1535c4f/maintainability)](https://codeclimate.com/github/SamueGathua/e-tshirt-store-api/maintainability)

## About the project
An online store for t-shirts

## Key principles observed during the development of this project:

    a) Pivotal tracker
    b) Workflow -Version control
    c) Test Driven Development(TDD).
    d) Object Oriented Programming.
    e) Data structures.
    f) Continuous Integration.
    g) Flask-restful.

### Project requirements
1. Python 3.6

### Getting Started
1. Clone this repository https://github.com/SamueGathua/e-tshirt-store.git' to your local machine.
2. Install a virtual environment 'pip install virtualenv'.
3. Create a virtual environment 'virtualenv myenv'.
4. Activate the environment 'source myenv/bin/activate'.
5. Install the required  project packages 'pip install -r requirements.txt'.
6. Setup the database environment variables
7. Enter 'Flask run' to test the API.

### API Endpoints(v1)
| **HTTP METHOD**  | **URI**                                    |  **DESCRIPTION**           |
| -----------      | -----------                                |  ---------------           |
| **POST**         | /api/v2/user/register                      |  Create a new user.        |  
| **POST**         | /api/v2/user/login                         |  Login a user.             |

### Running Tests
Enter 'coverage run --source=app -m pytest && coverage report' command to run tests.

### Author

Samuel Gathua
