from http.client import HTTPException
from typing import Annotated, Dict
import asyncio
import json
from nats.aio.client import Client as NATS
import asyncio
import json
import asyncio

class Calc:
    def __init__(self):
        self.result = 0.0

    def add(self, num):
        self.result += float(num)

    def subtract(self, num):
        self.result -= float(num)

    def multiply(self, num):
        self.result *= float(num)

    def divide(self, num):
        if float(num) != 0:
            self.result /= float(num)
        else:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")

    def put_in(self, num):
        self.result = float(num)

    def clear(self):
        self.result = 0.0

    def get_result(self):
        return self.result


users: Dict[str, str] = {}

def get_user_calc(user_id):
    if user_id not in users.keys():
        users[user_id] = Calc()
    return users[user_id]


def get_answer(calc, operator, num1=1):
    if operator == "add":
        calc.add(num1)
    elif operator == "subtract":
        calc.subtract(num1)
    elif operator == "multiply":
        calc.multiply(num1)
    elif operator == "divide":
        try:
            calc.divide(num1)
        except HTTPException:
            return calc.get_result()
    elif operator == "put_in":
        calc.put_in(num1)
    elif operator == "clear":
        calc.clear()
    else:
        raise HTTPException(status_code=400, detail="Invalid operator")
    return calc.get_result()


######################## nat server ############################



async def handle_message(msg):
    data = json.loads(msg.data.decode())
    operator = data.get("operator")
    
    num = data.get("num")
    user_id = data.get("user_id")
    calc = get_user_calc(user_id)
    try:
        result = get_answer(calc, operator, num)
    except HTTPException:
        result = get_answer(calc,'add',0)
    
    # Publish the result to the response subject
    response_subject = msg.reply
    try:
        await nc.publish(response_subject, json.dumps({"result": result}).encode())
    except Exception as e:
        # Handle the error 
        print(f"Error publishing message: {str(e)}")

async def start_server():
    await nc.connect("nats://localhost:4222")  # Updated connection to use environment variable
    await nc.subscribe("calc", cb=handle_message)

######### running the NATS server ########
if __name__ == "__main__":
    

    nc = NATS()
    loop = asyncio.get_event_loop()
       # Read the NATS server address from the environment variable

    try:
        loop.run_until_complete(start_server())
        print("the server is up and running")
        loop.run_forever()  # Keep the event loop running indefinitely

    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
    



