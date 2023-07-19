from flask import Flask, Blueprint, Response
from flask import render_template
import io
import base64
import asyncio
import threading
import queue
import time

# TODO delete these eventually
from pymoo.visualization.scatter import Scatter
from pymoo.problems import get_problem
# end delete these 

import matplotlib.pyplot as plt
import numpy as np

from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.problems import get_problem
from pymoo.core.callback import Callback
from pymoo.optimize import minimize


class MyCallback(Callback):

    def __init__(self) -> None:
        super().__init__()
        self.data["best"] = []

        self.announcer = self.MessageAnnouncer()    

        self.flask_thread = threading.Thread(target=self.start_server, daemon=True)
        self.flask_thread.start() 

        print("Press enter to start optimization.")
        input() 
        

    def notify(self, algorithm):
        self.data["best"].append(algorithm.pop.get("F").min())
      
        # TODO Send test update to client
        msg = self.format_sse(data="Generation %d" % algorithm.n_gen)
        self.announcer.announce(msg=msg)


        if algorithm.termination.has_terminated():

            print("Press enter to exit")
            input() 




    def start_server(self):
        # Set up blueprints to organize routes
        self.app = Flask(__name__)        

        blue_print = Blueprint('blue_print', __name__)
        blue_print.add_url_rule('/', view_func=self.dash_home)
        blue_print.add_url_rule('/listen', view_func=self.listen)

        self.app.register_blueprint(blue_print)
        self.app.run() 


    # Site listeners
    def listen(self):

        def stream():
            messages = self.announcer.listen()  # returns a queue.Queue
            while True:
                msg = messages.get()  # blocks until a new message arrives
                yield msg

        return Response(stream(), mimetype='text/event-stream')



    def dash_home(self):

        # Get demo code 
        F = get_problem("zdt3").pareto_front()
        plt = Scatter().add(F).show()

        # Set up I/O buffer to save the image 
        buffer = io.BytesIO()

        plt.fig.savefig(buffer, format='png', dpi=300)
        buffer.seek(0)

        # Encode bytes
        plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        return render_template('app.html', image=plot_base64)




    # SSE code taken from https://github.com/MaxHalford/flask-sse-no-deps
    class MessageAnnouncer:

        def __init__(self):
            self.listeners = []

        def listen(self):
            self.listeners.append(queue.Queue(maxsize=5))
            return self.listeners[-1]

        def announce(self, msg):
            # We go in reverse order because we might have to delete an element, which will shift the
            # indices backward
            for i in reversed(range(len(self.listeners))):
                try:
                    self.listeners[i].put_nowait(msg)
                except queue.Full:
                    del self.listeners[i]


    @staticmethod
    def format_sse(data: str, event=None) -> str:
        """Formats a string and an event name in order to follow the event stream convention.

        >>> format_sse(data=json.dumps({'abc': 123}), event='Jackson 5')
        'event: Jackson 5\\ndata: {"abc": 123}\\n\\n'

        """
        msg = f'data: {data}\n\n'
        if event is not None:
            msg = f'event: {event}\n{msg}'
        return msg



problem = get_problem("sphere")

algorithm = GA(pop_size=100)

res = minimize(problem,
               algorithm,
               ('n_gen', 20),
               seed=1,
               callback=MyCallback(),
               verbose=True)

