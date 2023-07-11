from flask import *
from mymashup  import mashup
# import shutil 
import os.path
from zipfile import ZipFile
from send_email import s

# Creating the ZIP file 
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer=request.form["singer"]
        count=int(request.form["count"])
        duration=int(request.form["duration"])
        outputfile = request.form["outputfile"]
        #email=request.form["email"]
        #print(email)
        mashup(singer,count,duration,outputfile+'.mp3')
        
        # aud_file1 = str(os.getcwd() +'\\' +"mashup.mp3")
        # import shutil
        # shutil.make_archive('file', 'zip', aud_file)
        # Create a ZipFile Object
        # print('Mahupdone')
        # archive_name = 'file.zip'
        # with ZipFile(archive_name, 'w') as file:
        #     file.write(str(os.getcwd() +'\\' +"mashup.mp3"))
        
        # s(email,'E:/webapp/file.zip')
        # return "form submitted to " + email
        return "File Have been saved with file name as " + outputfile
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,port=9000)