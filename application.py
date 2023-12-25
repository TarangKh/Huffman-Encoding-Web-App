from flask import Flask, render_template, request, url_for, redirect 
from flask import send_file
import huffman_encoder
from src import utils

application  = Flask(__name__)
app = application

path = ""

@app.route("/", methods=["GET", "POST"])
def main_page():
    try:
        if request.method == "POST":
            string = request.form.get("input")
            encoder = huffman_encoder.HuffmanEncoder()
            encoded_string = encoder.encode(string)
            
            total_words = encoder.getTotalWords()
            unique_words = len(encoder.getFrequency())
            freq_arr = encoder.getFrequency()
            code_arr = encoder.getCode()
            tree_root = encoder.getRoot()
            compressed_size = len(encoded_string)
            pkl_file_path = huffman_encoder.serialize(tree_root)
            rar_file_path = utils.make_rar(pkl_file_path)
            global path
            path = rar_file_path
            # print(pkl_file_path)
            # print(rar_file_path)
            # print(total_words)
            

            return render_template("index.html",
                                encoded_string=encoded_string,
                                freq_arr=freq_arr,
                                total_words=total_words,
                                unique_words=unique_words,
                                code_arr=code_arr,
                                compressed_size=compressed_size)
        else:
            return render_template("index.html")
    except Exception as e:
        return render_template("exception.html", error_name = e)
    

@app.route("/download")
def download_file():
     return send_file(path, as_attachment=True)
   


    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="8000")