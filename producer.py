import pika,sys, os



def main(message:str):

#create connection
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # create channel
    channel = connection.channel()

    #if the queue dose not exist alrredy
    #create a queue through the channel
    channel.queue_declare(queue="hello")


    # public the message
    channel.basic_publish(exchange="", routing_key="hello", body=str(message))
    print("[x] Sent Hello World")


    # Close connection
    # automatically close he channel

    connection.close()

if __name__ == "__main__":
    try:
        main(sys. argv)
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
