from distutils.core import setup

setup(
    name="django-iubenda-web",
    version="0.0.8",
    license="Iubenda integration for web application",
    description="Iubenda integration for web application",
    author="ShadMod",
    author_email="support@shadmod.it",
    url="https://github.com/shadMod/django_iubenda",
    download_url="https://github.com/shadMod/django_iubenda/archive/refs/tags/0.0.8.tar.gz",
    packages=[
        "django_iubenda",
        "django_iubenda.core",
        "django_iubenda.tests",
    ],
    keywords=[
        "Django iubenda",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
