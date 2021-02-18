# View
The site is live [here](https://ins-dashboard.uc.r.appspot.com).

# CNS-Discover
A database for seeing computed and experimental inelastic neutron scattering spectra.

# How to Contribute
1. File an issue via this repo's issue queue.

2. Write code to fix issues or to create new features. When contributing code, please be sure to:

* Fork this repository, modify the code (changing only one thing at a time), and then issue a pull request for each change.

* Follow the project's coding style.

* Test your code locally before issuing a pull request.

* Clearly state the purpose of your change in the description field for each commit.


# Architecture
The django modules are stored in the src folder. Materials is the main django app which contains all of the information about how to store a material in the SQL database. 

The static and staticfiles folders contain the raw INS spectra, .cif files, and skeletal formula files for each material. The folder structure is set up so that each material has its own folder.

The HTML templates are stored in the templates folder. base.html is the base for all other html files.

# Dependencies
appdirs==1.4.3

asgiref==3.3.1

bokeh==2.2.3

CacheControl==0.12.6

certifi==2019.11.28

chardet==3.0.4

chart-studio==1.1.0

colorama==0.4.3

contextlib2==0.6.0

cycler==0.10.0

distlib==0.3.0

distro==1.4.0

Django==3.1.3

gunicorn==20.0.4

html5lib==1.0.1

idna==2.8

ipaddr==2.2.0

Jinja2==2.11.2

jsmol-bokeh-extension==0.2.1

kiwisolver==1.3.1

lockfile==0.12.2

MarkupSafe==1.1.1

matplotlib==3.3.3

msgpack==0.6.2

numpy==1.19.4

packaging==20.3

pep517==0.8.2

Pillow==8.0.1

plotly==4.12.0

progress==1.5

PyMySQL==1.0.2

pyparsing==2.4.6

python-dateutil==2.8.1

pytoml==0.1.21

pytz==2020.4

PyYAML==5.3.1

requests==2.22.0

retrying==1.3.3

six==1.14.0

sqlparse==0.4.1

tornado==6.1

typing-extensions==3.7.4.3

urllib3==1.25.8

webencodings==0.5.1

whitenoise==5.2.0

# Cite As
Dettmann, M.A.; Vong, D.; Cavalcante, L.S.R.; Magdaleno, C.; Masalkovaitė, K.; Harrelson, T.F.; Daemen, L.L.; Moulė, A.J. (2021) CNS Discover. https://ins-dashboard.uc.r.appspot.com [![DOI](https://zenodo.org/badge/339552091.svg)](https://zenodo.org/badge/latestdoi/339552091)

# Contact
Makena Dettmann <mdettmann@ucdavis.edu>

Adam Moulė <amoule@ucdavis.edu>
