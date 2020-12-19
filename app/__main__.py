import asyncio
import logging
import argparse
import os

from app.api import Server, Configuration

debug = False


def main(args):
    # Directory setup
    os.makedirs(os.path.join("logs"), exist_ok=True)
    os.makedirs(os.path.join("database"), exist_ok=True)

    # Logging setup
    log_path = "logs/app.log"
    log_format = "[%(asctime)s][%(threadName)s][%(name)s.%(funcName)s:%(lineno)d][%(levelname)s] %(message)s"

    # Log file output
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(log_format))

    # Async event loop creation for later usage in serving up the w
    loop = asyncio.get_event_loop()

    # Check if debug flag is set
    debug = False
    if args.debug:
        debug = True
        loop.set_debug(True)

    logging.basicConfig(
        level=logging.DEBUG,
        format=log_format
    )

    logging.getLogger().addHandler(file_handler)

    if debug:
        logging.debug("Debug Enabled")

    host = args.host or "127.0.0.1"

    port = args.port or 8000

    # Get the server
    server = Server(config=Configuration("api:app",
                                         host=host,
                                         port=port,
                                         log_config=None,
                                         debug=debug))  # Debug here refers back to the check for the debug flag

    # We run the server as a task as this allows us to run other asynchronous applications (e.g. a twitter bot)
    # within the same program if we ever decide to expand the application in the future
    tasks = [
        loop.create_task(server.serve())
    ]
    loop.run_until_complete(asyncio.wait(tasks))  # Python 3.7 or higher required for the asyncio.wait call


if __name__ == "__main__":
    # Setting up some arguments for the console
    parser = argparse.ArgumentParser(description="MovePros website")
    parser.add_argument('--debug', help="Enable debug mode", action="store_true")
    parser.add_argument('--host', help="The IP to run on, e.g. 127.0.0.1", type=str, default="127.0.0.1")
    parser.add_argument('--port', help="Sets the port to run on", type=int, default=8000)
    main(parser.parse_args())
