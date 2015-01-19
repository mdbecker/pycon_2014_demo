# pycon_2014_demo
Demo app from PyCon 2014

**Note: This is a WIP**

## Usage
This demo requires a RabbitMQ server, a running API, a running worker (consumer) and a front-end. Right now it only has an API, the rest will be completed in the future.

### RabbitMQ
First you'll need a running RabbitMQ instance. There are lots of examples online for setting up RabbitMQ in a VM. Personally I like using [Vessel](https://awvessel.github.io/) because it makes it really easy to get a RabbitMQ VM up and running.

### Environment
I prefer the anaconda virtualenvs over plain-old python virtualenvs. To setup a conda virtualenv with the required packages run:
```sh
$ conda create -n pycon_2014_demo python=2.7 pip scikit-learn ipython-notebook Flask
$ source activate pycon_2014_demo
$ pip install rabbitpy
```

### API
Start the api by running
```sh
$ python api.py
``` 

### A simple request
To hit the api without the front-end, you can make a simple request using curl
```sh
$ curl -H "Content-Type: application/json" -d '{"text":"hello world"}' http://127.0.0.1:5000/
```

### Inspect the message in the RabbitMQ management console
If all goes well, you should now have a message in your RabbitMQ server in the 'test' queue. You can navigate to the management console by navigating to http://``{RABBITMQ_IP}``:15672 in your browser. From there, you can:

 1. Click on the "Queues" tab. 
 2. Click on the "test" queue.
 3. Open up the "Get messages" section (near the bottom).
 4. Click the "Get Message(s)" button.

If everything is working, you should see a message in the management console that matches the json in the curl command from above.
