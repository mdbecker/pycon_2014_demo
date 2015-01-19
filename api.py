"""Copyright (C) 2015  Michael Becker <mike@beckerfuffle.com> (@beckerfuffle)"""


from flask import Flask, jsonify, request, g
import rabbitpy

def get_rabbit_channel(ip='192.168.50.101'):
    # Connect to RabbitMQ on localhost, port 5672 as guest/guest
    conn = g.get('_rabbit_conn', None)
    if conn is None:
        conn = rabbitpy.Connection('amqp://guest:guest@{0}:5672/%2f'.format(ip))

    # Open the channel to communicate with RabbitMQ
    channel = g.get('_rabbit_channel', None)
    if channel is None:
        channel = conn.channel()

    # Turn on publisher confirmations
    channel.enable_publisher_confirms()
    return channel

app = Flask(__name__)

@app.route('/', methods=['POST'])
def test():
    args = request.get_json()
    channel = get_rabbit_channel()
    message = rabbitpy.Message(channel, args)
    if message.publish('', 'test', mandatory=True):
        return jsonify(success=True)
    return jsonify(success=False)

if __name__ == '__main__':
    app.run()
