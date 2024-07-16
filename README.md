# Cloud-based-inventory-management-system-prototype

# Cloud-Based Inventory Management System

This project is a cloud-based inventory management system developed using Python and Django, hosted on AWS. It includes features for tracking inventory levels, orders, sales, and deliveries.

## Features
- Track inventory levels, orders, sales, and deliveries.
- Utilize AWS services for storage, database, and deployment.
- Ensure scalability and reliability.

## Installation

1. Clone the repository:

    git clone https://github.com/Jayp1010/Cloud-based-inventory-management-system-prototype
    cd cloud_inventory_management


2. Create a virtual environment and activate it:
  
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  

3. Install the required packages:
  
    pip install -r requirements.txt


4. Set up the Django project:
   
    python manage.py migrate
    python manage.py createsuperuser
  

5. Run the development server:
  
    python manage.py runserver


## Deployment on AWS

1. Create an AWS account and set up the necessary services.
2. Update the `settings.py` file with your AWS configurations.
3. Build and push the Docker image to AWS ECR.
4. Deploy the Docker container to AWS ECS or EC2.

## File Descriptions

- `inventory_management/`: Django project settings and configuration files.
- `inventory/`: Django app for inventory management.
- `requirements.txt`: Lists the dependencies required for the project.
- `manage.py`: Django command-line utility for administrative tasks.
- `Dockerfile`: Dockerfile for containerizing the application.

## License

This project is licensed under the MIT License.
