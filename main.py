# Tic Tac Toe by James Corino
# Version 5/21/24
# Utilizing: Flask, Python, HTML, and HTMX

from flask import Flask, request
import functions


app = Flask(__name__)

# Home page with links to the two different game modes
@app.route('/')
def index():
    return '''
    <HTML>
        <style>
            body {
                text-align: center;
            }
            button {
                background-color: white;
                outline: 10px;
                font-size: 20px;
            }
        </style>
        <body>
            <h1>Welcome to Tic Tac Toe</h1>
            <h3>Choose a game mode:</h3>
            <button onclick="window.location.href='/one_on_one'">One on One 👥: Play against a friend</button>
            <br>
            <button onclick="window.location.href='/cpu'">Against CPU 💻: Play against a computer</button>

            <h4>Purpose</h4>
            <p>This is a simple Tic Tac Toe game created for the purpose of learning. <br>The game is built using Flask, Python, HTML, and HTMX.</p>
            <p><i>Created by James Corino</i></p>
        </body>
    </HTML>
    '''
@app.route('/cpu')
def cpu():
    return '''
    <html>
      <head>
         <script src="https://unpkg.com/htmx.org@1.9.12"></script>
      </head>
      <style>
        body {
          text-align: center;
          margin-top: 50%;
        }
        button {
          margin:10px 10px;
          background-color: white;
          height: 75px;
          width: 75px;
          outline: 10px;
          font-size: 40px;
        }
        button:disabled {
          color: black;
          background-color: white;
          border-color: black;
        }
      </style>
      <body>
        <form hx-post="/tic_tac_toe_CPU" hx-target="this" hx-swap="innerHTML">
          <input name="h0" value="&#25" type="hidden"></input>
          <button name="b0" type="submit">&#25</button>
          <input name="h1" value="&#25" type="hidden"></input>
          <button name="b1" type="submit">&#25</button>
          <input name="h2" value="&#25" type="hidden"></input>
          <button name="b2" type="submit">&#25</button>
          <br>
          <input name="h3" value="&#25" type="hidden"></input>
          <button name="b3" type="submit">&#25</button>
          <input name="h4" value="&#25" type="hidden"></input>
          <button name="b4" type="submit">&#25</button>
          <input name="h5" value="&#25" type="hidden"></input>
          <button name="b5" type="submit">&#25</button>
          <br>
          <input name="h6" value="&#25" type="hidden"></input>
          <button name="b6" type="submit">&#25</button>
          <input name="h7" value="&#25" type="hidden"></input>
          <button name="b7" type="submit">&#25</button>
          <input name="h8" value="&#25" type="hidden"></input>
          <button name="b8" type="submit">&#25</button>
        </form>
      </body>
      </head>
    '''

@app.route('/one_on_one')
def one_on_one():
    return '''
    <html>
      <head>
         <script src="https://unpkg.com/htmx.org@1.9.12"></script>
      </head>
      <style>
        body {
          text-align: center;
          margin-top: 5%;
        }
        button {
          margin:10px 10px;
          background-color: white;
          height: 75px;
          width: 75px;
          outline: 10px;
          font-size: 40px;
        }
        button:disabled {
          color: black;
          background-color: white;
          border-color: black;
        }
      </style>
      <body>
        <form hx-post="/tic_tac_toe" hx-target="this" hx-swap="innerHTML">
          <input name="h0" value="&#25" type="hidden"></input>
          <button name="b0" type="submit">&#25</button>
          <input name="h1" value="&#25" type="hidden"></input>
          <button name="b1" type="submit">&#25</button>
          <input name="h2" value="&#25" type="hidden"></input>
          <button name="b2" type="submit">&#25</button>
          <br>
          <input name="h3" value="&#25" type="hidden"></input>
          <button name="b3" type="submit">&#25</button>
          <input name="h4" value="&#25" type="hidden"></input>
          <button name="b4" type="submit">&#25</button>
          <input name="h5" value="&#25" type="hidden"></input>
          <button name="b5" type="submit">&#25</button>
          <br>
          <input name="h6" value="&#25" type="hidden"></input>
          <button name="b6" type="submit">&#25</button>
          <input name="h7" value="&#25" type="hidden"></input>
          <button name="b7" type="submit">&#25</button>
          <input name="h8" value="&#25" type="hidden"></input>
          <button name="b8" type="submit">&#25</button>
        </form>
      </body>
      </head>
    '''


@app.route('/tic_tac_toe', methods=['POST'])
def tic_tac_toe():
    values = [request.form[f'h{i}'] for i in range(9)]

    o_count = 0
    x_count = 0

    for x in range(len(values)):
        if values[x] == 'O':
            o_count += 1
    for x in range(len(values)):
        if values[x] == 'X':
            x_count += 1

    turn = ""

    if x_count <= o_count:
        turn = "X"
    else:
        turn = "O"

    buttons = [request.form.get(f'b{i}') for i in range(9)]

    for i in range(9):
        if buttons[i] is not None:
            values[i] = turn

    resp = ''

    if functions.isWin(values) == 'X' or functions.isWin(values) == 'O':
        resp += f"<h2>{turn}'s have won</h2>"
        for i in range(9):
            resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    elif (functions.isWin(values) == 'tie'):
        resp += f"<h2>Tied</h2>"
        for i in range(9):
            resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    else:
        for i in range(9):
            resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" {"disabled" if (values[i] == "X" or values[i] == "O") else " "}>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'

    resp += '''
            <br>
            <a href="/one_on_one">Restart</a>
            <a href="/">Home</a>
            '''

    return resp


# --------------------------------------------------------------------------------------------------------#

@app.route('/tic_tac_toe_CPU', methods=['POST'])
def tic_tac_toe2():
    values = [request.form[f'h{i}'] for i in range(9)]

    turn = "X"
    cTurn = "O"

    buttons = [request.form.get(f'b{i}') for i in range(9)]

    for i in range(9):
        if buttons[i] is not None:
            values[i] = turn

    if functions.isWin(values) != 'X':
        if type(functions.findWinningMove(values)) == type(1):
            values[functions.findWinningMove(values)] = cTurn

    resp = ''''''

    if functions.isWin(values) == 'X':
        resp += f"<h2>{turn}'s have won<</h2>"
        for i in range(9):
            resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    elif functions.isWin(values) == 'O':
        resp += f"<h2>{cTurn}'s have won</h2>"
        for i in range(9):
            resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    elif functions.isWin(values) == 'tie':
        resp += f"<h2>Tied</h2>"
        for i in range(9):
            resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    else:
        for i in range(9):
            resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" {"disabled" if (values[i] == "X" or values[i] == "O") else " "}>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'

    resp += '''
        <br>
        <a href="/cpu">Restart</a>
        <a href="/">Home</a>
        '''

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

