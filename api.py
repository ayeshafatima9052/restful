from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///api.db')


table = db['employees']

def fetch_db(employee_id):  
    return table.find_one(employee_id=employee_id)

def fetch_db_all():
    employees = []
    for employee in table:
        employees.append(employee)
    return employees



@app.route('/api/db_populate', methods=['GET'])
def db_populate():
    table.insert({
        "employee_id":"1",
        "name":"john",
        "department":"Finance"
        })
    
    table.insert({
        "employee_id":"2",
        "name":"jack",
        "department":"Marketing"
        }
    )

    return make_response(jsonify(fetch_db_all()),200)
   


@app.route('/api/employees', methods=['GET', 'POST'])
def api_employees():
     if request.method =='GET':
        return make_response(jsonify(fetch_db_all()),200)
     elif request.method == 'POST':
        content = request.json
        employee_id = content['employee_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(employee_id)), 201)


@app.route('/api/employees/<employee_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_employee(employee_id):
    if request.method == "GET":
        employee_obj = fetch_db(employee_id)
        if employee_obj:
            return make_response(jsonify(employee_obj), 200)
        else:
            return make_response(jsonify(employee_obj), 404)

    elif request.method == "PUT":  # Updates the employee
        content = request.json
        table.update(content,['employee_id'])
        

        employee_obj = fetch_db(employee_id)
        return make_response(jsonify(employee_obj), 200)
    elif request.method == "DELETE":
        table.delete(id=employee_id)
       
        return make_response(jsonify({}), 204)    




if __name__ == '__main__':
    app.run(debug=True)
