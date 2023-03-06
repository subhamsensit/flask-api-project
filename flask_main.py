from flask import Flask,jsonify
import subprocess,sys,json,os
from datetime import datetime
import logging,time
app = Flask(__name__)
# logger code
# setting time
LOG_TIMESTAMP_FORMAT = "%Y-%m-%d %H-%M-%S"

TIME = datetime.now().strftime(LOG_TIMESTAMP_FORMAT)

# below logger will create log file db_certification.log under current directory
# file path for logging
current_directory=os.getcwd()
# Zoom_ipv6.txt and Team ip folder
# setting up log file
log_path_certification=os.path.join(current_directory,"Log_files","flask_app.log")
logger=logging.getLogger("zoom-trigger")
logger.setLevel(logging.DEBUG)
format=logging.Formatter("'%(asctime)s %(message)s")
fh=logging.FileHandler(log_path_certification,mode="w")
fh.setFormatter(format)
logger.addHandler(fh)
logger.debug("======starting of  Flask log ========")

# initializing configparser to read Configurations.ini




@app.route("/",methods=["GET"])
def trigger_script():
    try:
        theproc = subprocess.Popen([sys.executable, r"C:\Users\Zscaler\Documents\backup-dr-db\MR-1993-DR-Zoom-call\dr_zoom_team_call.py"])
        theproc.communicate()
        # reading result.json file
        time.sleep(5)
        result_file_path=r"C:\Users\Zscaler\Documents\backup-dr-db\MR-1993-DR-Zoom-call\result.json"
        with open(result_file_path,"r") as fh:
            logger.debug("reading the result.json file")
            data = json.load(fh)
        logger.debug(f"Returning result to client {data}")
        return jsonify(data)
    except Exception as e :
        logger.debug(f"Ecxception occured as {e} in Flask script returning value")
        logger.debug("Failed to send data to client")
        data={"zoom_call_status":False,"Status":404}
        return jsonify(data)


if __name__ == "__main__":
    app.run(host='10.66.19.64', port=80,debug=True)