from flask import Flask,jsonify
import subprocess,sys
import logging
app = Flask(__name__)

@app.route("/",methods=["GET"])
def trigger_script():
    try:
        theproc = subprocess.Popen([sys.executable, r"C:\Users\Zscaler\Documents\backup-dr-db\MR-1993-DR-Zoom-call\dr_zoom_team_call.py"])
        theproc.communicate()
        # reading result.json file
        result_file_path=r"C:\Users\Zscaler\Documents\backup-dr-db\MR-1993-DR-Zoom-call\result.json"
        return "Script Triggered successfully"
    except:
        return "failed to run the script"


if __name__ == "__main__":
    app.run(host='10.66.19.64', port=80,debug=True)