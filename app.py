from flask import Flask, request, jsonify
import openpyxl
import os

app = Flask(__name__)

# Path for Excel file
EXCEL_FILE = "website1.xlsx"

# Create workbook if not exists
if not os.path.exists(EXCEL_FILE):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["Name", "Email", "Message"])  # headers
    wb.save(EXCEL_FILE)

@app.route("/submit_website1", methods=["POST"])
def submit_website1():
    data = request.get_json()
    name, email, message = data.get("name"), data.get("email"), data.get("message")

    wb = openpyxl.load_workbook(EXCEL_FILE)
    sheet = wb.active
    sheet.append([name, email, message])
    wb.save(EXCEL_FILE)

    return jsonify({"message": "✅ Your details have been saved!"})

if __name__ == "__main__":
    app.run(debug=True)
