import os
import time

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_from_directory
)

from layout_preserving_pdf import translate_pdf


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

app = Flask(
    __name__,
    template_folder=os.path.join(
        BASE_DIR,
        "frontend",
        "templates"
    ),
    static_folder=os.path.join(
        BASE_DIR,
        "frontend",
        "static"
    )
)

INPUT_FOLDER = os.path.join(
    BASE_DIR,
    "input"
)

OUTPUT_FOLDER = os.path.join(
    BASE_DIR,
    "output"
)

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():

    try:

        if "file" not in request.files:

            return jsonify({

                "success": False,

                "message": "No file selected."

            })

        file = request.files["file"]

        if file.filename == "":

            return jsonify({

                "success": False,

                "message": "No file selected."

            })

        target_language = request.form.get(
            "target_language",
            "Hindi"
        )

        input_path = os.path.join(
            INPUT_FOLDER,
            file.filename
        )

        file.save(input_path)

        output_filename = "translated.pdf"

        output_path = os.path.join(
            OUTPUT_FOLDER,
            output_filename
        )

        start = time.time()

        translate_pdf(
            input_path,
            output_path,
            target_language
        )

        processing_time = round(
            time.time() - start,
            2
        )

        return jsonify({

            "success": True,

            "filename": output_filename,

            "original_file": file.filename,

            "target_language": target_language,

            "processing_time": processing_time,

            "download_url": "/download/" + output_filename

        })

    except Exception as error:

        return jsonify({

            "success": False,

            "message": str(error)

        })


@app.route("/download/<filename>")
def download(filename):

    return send_from_directory(

        OUTPUT_FOLDER,

        filename,

        as_attachment=True

    )


if __name__ == "__main__":

    app.run(

        debug=True

    )