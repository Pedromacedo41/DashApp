
## Overview 

Online interactive dashboard for exploratory medical data analysis

### Technical details

- Starts with user *csv* file upload with some variables conventions, alternatively pre-processing csv  
- User session solution: downloadable session.json file  
- No user persistent data on server
- Server-based cache solution

## Install and Run Instructions:

Python version: 3.8


**Create python environment**:

```
$ conda create -n sample_app python=3.8
$ conda activate sample_app
```

**Install packages and dependencies**:

```
$ pip install -r requirements.py
```

**Run app** 

Developement version:

```
$ python app.py --debug
```

Production verions:

```
$ python app.py 
```