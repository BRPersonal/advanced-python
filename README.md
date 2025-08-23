# python-sse
Project that demoes server sent events using Python and FastAPI 

Setting up the dev environment 
--------  
# Create and activate a new virtual environment 
$ conda create -n sse-env python=3.13 -y 

#activate the virtual environment
$ conda activate sse-env 

Install necessary librararies
$ pip install fastapi uvicorn

Start the server
$ uvicorn app:app --reload
press ctrl + c to stop the server

Browse the url
http://localhost:8000/stream-time

Setting up PyCharm 
---------- 
OPen the project folder in pyCharm. It will say Python interpreter is not configured. 
Click on configure click on add interpreter, select "Existing" tab" and then naviage to 
the folder /Applications/anaconda3/envs/sse-env/bin/python and click ok. 
