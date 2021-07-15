# Online Blood Bank
An open-source project for managing blood donors and receivers. This web application can search for donors in Nepal's different districts or local levels by specific blood group.

[More Info Here](https://arjunsingh.com.np/online-blood-bank)

## Usage
1. First, clone this project,
    ```sh
    git clone https://github.com/mearjunsingh/online-blood-bank.git
    ```
---
2. Then get inside that folder,
    ```sh
    cd online-blood-bank
    ```
---
3. Now make sure you have python installed. It is a best practice to install Python projects in a Virtual Environment. To install and create Virtual Envronment,
    ```sh
    pip install virtualenv
    virtualenv venv
    ```
---
4. Now activate virtualenv,
   - In windows
       ```bat
       venv\Scripts\activate
       ```
   - In Linux
        ```sh
        source venv/bin/activate
        ```
---
5. Then install dependencies. To do that,
    ```bash
    pip install -r requirements.txt
    ```
---
6. Now we are ready to run the project. But before that, you must migrate all migrations. Here is how,
    ```bash
    python manage.py migrate
    ```
---
7.  **IMPORTANT!** You can add superuser via shell by,
    ```bash
    python manage.py createsuperuser
    ```
    But this is uncomfortable because this project requires a lot of imformation. To solve this problem, this project automatically promotes the **FIRST USER** as **SUPERUSER**. Also by default, admin is **not** listed as donor.

    *SKIP THIS STEP, RUN THE SERVER (AS MENTIONED IN STEP 8) AND REGISTER FROM THE BROWSER ITSELF*
---
8. Finally, ready to run the project. Run this command,
    ```bash
    python manage.py runserver
    ```
---
9. Then locate http://127.0.0.1:8000/ in your favorite web browser.
---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.