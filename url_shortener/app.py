from flask import Flask,request,redirect
import db

app=Flask(__name__)
@app.route("/",methods=["GET"])
def get_url():
    key = request.json
    value=db.generate_random()
    short_url=db.generate_url(key,value)
    return short_url

@app.route("/<short_url_code>",methods=["GET"])
def getdata(short_url_code):
    if short_url_code:
        long_url=db.checking_for_url(short_url_code)

        return redirect(long_url)




if __name__=="__main__":
    app.run(port=5000,debug=True)