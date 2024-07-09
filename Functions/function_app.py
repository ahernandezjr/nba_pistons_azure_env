import logging
import azure.functions as func

# Creation packages
import os
import time
import pandas as pd
from basketball_reference_web_scraper import client

# Processing packages
import os
import numpy as np
import pandas as pd

# Filtering packages
##



app = func.FunctionApp()

@app.schedule(schedule="0 0 0 1 * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def player_data_collection(myTimer: func.TimerRequest) -> None:
    '''
    This function is triggered by a timer. It will collect player data from the NBA API and store it in a database.
    '''

    if myTimer.past_due:
        logging.info('The timer is past due!')

    result = 1 + 1
    logging.info(f'Python timer trigger function executed. Test output: {result}')