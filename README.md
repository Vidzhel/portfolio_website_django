# Portfolio website
This was my previous Python-based website powered by the Django framework. The main purpose of the site was to provide me with a place where I can store my portfolio, some additional information about me, CV.


<p align="center"><a href="https://i.ibb.co/Db517Rr/Oleg-Talaver-Google-Chrome-17-08-2019-12-24-35-2.png"><img src="https://i.ibb.co/Db517Rr/Oleg-Talaver-Google-Chrome-17-08-2019-12-24-35-2.png" width="700" alt="header of the home page"/></a></p>


## Table of contents
* [I have learned](#i-have-learned)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Built With](#built-with)

## I have learned
- Dealing with the Django framework;
- Working with AJAX queries to speed up the website;
- Using SASS/SCSS;
- Improved Web Design skills;


<p align="center"><a href="https://i.ibb.co/5rMvgDV/portfolio-website-django.jpg"><img src="https://i.ibb.co/5rMvgDV/portfolio-website-django.jpg" width="700" alt="header of the home page"/></a></p>
<p align="center" style="text-align:center; margin:-=0">Database tables diagram</p>

## Getting Started
To copy the project open bash, go to the folder where you would like to store files and write:
```
git clone https://github.com/Vidzhel/portfolio_website_django.git
```

To run Django server type in the bash:
```
python3 relative/path/to/manage.py runserver
```

**Note:** see [Prerequisites](#prerequisites) to find out requiered files.
If you would like to deploy the site look [here](https://docs.djangoproject.com/en/2.2/howto/deployment/).

### Prerequisites
To run the website, you will need to install python v3+, Django, how to install them you can find out [here](https://docs.djangoproject.com/en/2.2/intro/install/) and [here](https://docs.djangoproject.com/en/2.2/topics/install/)

It will be better if you use a [virtual environment](https://tutorial.djangogirls.org/en/django_installation/
), as if you want to install a different version of the Django, you will be able to do this without any hassle.

Next step will change the [settings.py](portfolio_website/settings.py) file. First thing first, I have moved the SECRET_KEY into another file due to security reasons, so you need to generate it on your own. [Here](https://gist.github.com/sandervm/2b15775012685553f0e2) you can find how to do this. Later you need to specify USER_EMAIL and USER_PASS. Those are your email address and the [app password for gmail](https://support.google.com/accounts/answer/185833?hl=en)(as I use Gmail). This email will be used when someone submits a form on the Home page.

## Built With
- Python v3.7.3
- Django v2.2.4
- HTML/SASS
- JavaScript
- Visual Code - IDE
