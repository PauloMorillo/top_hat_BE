# TOP HAT BE TEST

This is a discussion API built in django

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements.

```bash
pip install -r requirements.txt
```

## Versions

-   python 3.9
-   Django 4.2.7

## Usage

Run webserver (By default Django uses 8000 port)

```bash
python manage.py runserver
```
To run the unittest
```bash
python manage.py test
```

To use the Tree Discussion Question structure check the swagger or redoc documentation
- http://localhost:8000/swagger/
- http://localhost:8000/redoc/

Raw_data example or you can use DRF directly from browser:
```bash
{
    "comment": "Hello Guys",
    "user": "teacher",
    "parent": null
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)