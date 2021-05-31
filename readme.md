# Online Blood Bank
An open-source project for managing blood donors and receivers. This web application can search for donors in Nepal's different districts or local levels by specific blood group.

[More Info Here](https://arjunsingh.com.np/online-blood-bank)

## Usage

First, clone this project

```bash
git clone https://github.com/mearjunsingh/online-blood-bank.git
```

Then

```bash
cd online-blood-bank
```

Now make sure you have python installed. It's best practice to install Python projects in a Virtual Environment. To install and create Virtual Envronment, 

```bash
pip install virtualenv
virtualenv venv
```

Now activate virtualenv,

* In windows
```bash
venv\scripts\activate
```
* In Linux
```bash
source venv/bin/activate
```

Then install dependencies. To do that,

```bash
pip install -r requirements.txt
```

Now we are ready to run the project. Here is how,

```python
python manage.py runserver
```

Then locate http://127.0.0.1:8000/ in your favorite web browser.

## Admin Login
```bash
email: admin@gmail.com
password: admin
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.