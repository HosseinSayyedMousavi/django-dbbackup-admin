from setuptools import setup

setup(
    name='django-dbbackup-admin',
    version='1.0.0',
    description='Get Backup From Database Through Admin Panel',
    author='Hossein Sayyedmousavi',
    author_email='Hossein.Sayyedmousavi@gmail.com',
    packages=['dbbackup-admin'],
    install_requires=[
                            'django-dbbackup==4.0.2',
                            'django-solo==2.1.0',
                      ],
    url="https://github.com/HosseinSayyedMousavi",
    keywords=[
        "django",
        "database",
        "media",
        "backup",
        "amazon",
        "s3",
        "dropbox",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Environment :: Console",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Database",
        "Topic :: System :: Archiving",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: System :: Archiving :: Compression",
    ],
)