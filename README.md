# python-sse
Project that demoes server sent events using Python and FastAPI 

Setting up the dev environment 
--------  
# Create and activate a new virtual environment  
# Note we are going to use this env for all advanced python pocs  
$ conda create -n sse-env python=3.13 -y 

#list discoverable environments
$ conda info --envs 

#activate the virtual environment
$ conda activate sse-env 

Install necessary libraries 
$ pip install fastapi uvicorn
$ pip install psutil
$ pip install polars

Start the server
$ uvicorn app:app --reload 
press ctrl + c to stop the server 

Browse the urls
http://localhost:8000/stream-time
http://localhost:8000/system-stats

Setting up PyCharm 
---------- 
OPen the project folder in pyCharm. It will say Python interpreter is not configured. 
Click on configure click on add interpreter, click on add local , select "Existing" tab" and then naviage to 
the folder /Applications/anaconda3/envs/sse-env/bin/python and click ok. 
