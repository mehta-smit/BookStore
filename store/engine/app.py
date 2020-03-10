from flask import Flask


def create_app(app_name, app_root):
    """
    Creates a Flask Application with given name.
    And binds the template & staic folder path to the flask application.
    :param app_name: Str: Name of the flask application.
    :param app_root: Str: Name of the package that contains the templates & Static data.
    :return: Flask Application
    """
    return Flask(
        app_name,
        template_folder="{}/templates".format(app_root),
        static_folder="{}/static".format(app_root)
    )
