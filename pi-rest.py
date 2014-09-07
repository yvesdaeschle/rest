from flask import Flask, render_template
import datetime
import os
app = Flask(__name__)


@app.route("/")
def hello():
   #now = datetime.datetime.now()
   #timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'response': ""
      }
   return render_template('main.html', **templateData)

@app.route("/single/<channel>/<device>/<status>")
def single(channel, device, status):
   try:
      intChannel = int(channel)
      intDevice = int(device)
      intStatus = int(status)
      strChannel = ""

      if intChannel == 1:
         strChannel = "10000"
      elif intChannel == 2:
         strChannel = "01000"
      else:
         strChannel = "10000"

      os.system("sudo /home/pi/prj/rcswitch-pi/send " + strChannel +  " " + str(intDevice) + " " + str(intStatus))

      response = "done"
   except:
      response = "error"

   templateData = {
      'response' : response
      }

   return render_template('main.html', **templateData)

@app.route("/function/<code>")
def functionCode(code):
   try:
      intCode = int(code)
      strScript = ""
      response = "done"

      if intCode == 1:
         strScript = "alle_lampen_an"
      elif intCode == 2:
         strScript = "alle_lampen_aus"
      elif intCode == 3:
         strScript = "alle_lampen_sch_an"
      elif intCode == 4:
         strScript = "alle_lampen_sch_aus"
      elif intCode == 5:
         strScript = "alle_lampen_whn_an"
      elif intCode == 6:
         strScript = "alle_lampen_whn_aus"
      elif intCode == 7:
         strScript = "alles_aus"
      else:
         response = "error"

      if not response == "error":
         os.system("echo " + "sudo sh /home/pi/prj/rcauto/" + strScript + ".sh")
         os.system("sudo sh /home/pi/prj/rcauto/" + strScript + ".sh")

   except:
      response = "error"

   templateData = {
      'response' : response
      }

   return render_template('main.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)