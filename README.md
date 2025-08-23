# python-sse
Project that demoes server sent events using Python and FastAPI

New learning in creating a virtual environment using anaconda - 23-Aug-25
$ conda create -n sse-env python=3.13 -y

activate the new virtual environment created
$ conda activate sse-env

check python version
(sse-env)$ python --version
Python 3.13.5

deactivate the conda virtual environment
$ conda deactivate

check python version
$ python --version
Python 3.12.4

Beauty is it does not create any folder under the current folder unlike the
python -m venv command that I was using earlier

Let us do another check. I go to home folder
$ which python
/Applications/anaconda3/bin/python


activate sse-env virtual environment. Note the prompt change
$ conda activate sse-env  

I come to app folder ~/poc/python/python-sse
(sse-env) $ which python
/Applications/anaconda3/envs/sse-env/bin/python

Install necessary librararies
$ pip install fastapi uvicorn

Start the server
$ uvicorn app:app --reload

Browse the url
http://localhost:8000/stream-time

