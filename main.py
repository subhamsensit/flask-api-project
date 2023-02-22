from flask import Flask,jsonify
import subprocess,sys,json
import logging
app = Flask(__name__)

@app.route("/",methods=["GET"])
def trigger_script():
    try:
        theproc = subprocess.Popen([sys.executable, r"C:\Users\Zscaler\Documents\backup-dr-db\MR-1993-DR-Zoom-call\dr_zoom_team_call.py"])
        theproc.communicate()
        # reading result.json file
        result_file_path=r"C:\Users\Zscaler\Documents\backup-dr-db\MR-1993-DR-Zoom-call\result.json"
        with open(result_file_path,"r") as fh:
            print("reading the result.json file")
            data = json.load(fh)

        return jsonify(data)
    except:
        return "failed to run the script"


if __name__ == "__main__":
    app.run(host='10.66.19.64', port=80,debug=True)