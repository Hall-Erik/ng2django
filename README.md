# ng2django

![PyPI](https://img.shields.io/pypi/v/ng2django)
![PyPI - License](https://img.shields.io/pypi/l/ng2django)

This is a simple Python tool that will convert an HTML file built by Angular2+ to Django Template Language. This way static files can be made available to an Agnular app that is served up with a Django project.

The script basically does two things:

- Adds a `{% load static %}` tag to the top of the file
- Changes the value of `href` and `src` attributes of `link` and `script` tags to `{% static "<path-to-the-file>" %}`

## Dependencies

The script uses Beutifulsoup4. You can install it by running `pip install -r requirements.txt`.

## Install

Just run `$ pip install ng2django`

## Usage

Build your Angular app and place the files in `<Django-project-root>/<app>/static/<optional-subdirectory>/`.

The script takes two positional arguments:

- `source`: The path to the HTML file you want to convert.
- `dest`: Where you want the Django Template file saved.

Then you can run

`$ ng2django <Django-project-root>/<app>/static/index.html <Django-project-root>/<app>/templates/index.html`

if you are storing your files directly in your Django app's `static` and `templates` directories (not recommended), or

`$ ng2django <Django-project-root>/<app>/static/<optional-subdirectory>/index.html <Django-project-root>/<app>/templates/<optional-subdirectory>/index.html -s <optional-subdirectory>`

if you are using some subdirectory of those paths.

## Optional Arguments

Short | Long | Description
--- | --- | ---
-s `<subdir>` | --subdir `<subdir>` | Include the subpath under `<Django-app>/static/` where your static files are stored.
-n | --nodelete | Do not delete the source file after converting.
-p | --pretty | Create a dest file that is more human readable.

## Recommended Setup and Usage

In you Angular project open your `package.json` file. Under `scripts`, change `build` to

`ng build --prod --output-path <Your-django-project-root>/<Django-App>/static/ng`.

Add a `postbuild` key under `script` and set the value to

`ng2django <Your-django-project-root>/<Django-App>/static/ng/index.html <Your-django-project-root>/<Django-App>/templates/ng/index.html -s ng`.
or if you have css / js / images in seperate directories within static use args: -css css -js js -img img
`ng2django <Your-django-project-root>/<Django-App>/static/ng/index.html <Your-django-project-root>/<Django-App>/templates/ng/index.html -s ng -css css -js js -img img`.


Run `npm run build` and your Angular JS and CSS files will be saved to your Django app's static directory. Then, this script will run and convert your HTML file and save it in your Django app's templates directory.

## Contributing

Contributions are welcome - submit an issue/pull request.

## Push to PyPi

Use these commands to release on PyPi

<code>
    rm -rf dist/ build/<br>
    python setup.py sdist<br>
    twine upload dist/*
</code>
