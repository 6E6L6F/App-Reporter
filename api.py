from flask import *
from werkzeug.utils import secure_filename
import os
from services import SpamReport

app = Flask(
    __name__,
    template_folder="template",
    static_folder="static"
)
UPLOAD_FOLDER = 'databases'
ALLOWED_EXTENSIONS = {'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     

@app.route("/" , methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/panel" , methods=["POST" , "GET"])
def panel_sender():
    response = {       
                'count_emails' : 0,
                'message'      : 'none',
                'count_error'  : 0,
                'count_sended' : 0
                } 
    if request.method == "POST":
        if 'file' in request.files:            
            file = request.files['file']
            if file.filename == '':
                flash('No selected file' , 'danger')
                return redirect(request.url)
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                pwd = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(pwd)  
                result = os.stat(pwd).st_size
                if result < 10:
                    os.remove(pwd)
                    flash("file is emtpy" , 'danger')
                else:
                    flash("file uploaded" , 'success')
                    response['count_emails'] = len(open(pwd ,'r').read().split('\n'))
                    
            else:
                flash("format file not suported just file text " , 'danger')
        else:
            text_message = request.form['message']
            target = request.form['target'] 
            list_emails = request.form['emails'] 
            service_sender = request.form['service']
            sender = SpamReport(
                file_name="databases/" + list_emails,
                text=text_message,
                send_to=target
            )    
            if service_sender == "gmail":
                result = sender.send_gmail()

            else:
                result = sender.send_yahoo()  
                              
            count_emails = sender.count_emails
            count_error = sender.false_send
            count_sended = sender.true_send
            if count_sended != 0:
                message = f"{count_sended} user sended a message"
            else:
                message = "can't send a message"                
            
            response = {       
                    'count_emails' : count_emails,
                    'message'      : message,
                    'count_error'  : count_error,
                    'count_sended' : count_sended
                }         
       
    emails = os.listdir("databases")     
    if not emails:
         emails = None
         
    return render_template("index.html" , email_list=emails,response=response)



if __name__ == "__main__":
    app.run("0.0.0.0" , 8080 , debug=True)
    