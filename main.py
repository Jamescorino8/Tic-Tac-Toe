# Tic Tac Toe by James Corino
# Version 5/21/24
# Utilizing: Flask, Python, HTML, and HTMX

from flask import Flask, request
import random
  
app = Flask(__name__)

# Takes values array as input to check for best possible placement for computer player, otherwise random. '\x19' == empty space unicode as hex.
def findWinningMove(values):
  #OHorizontal
  for i in range(0, 9, 3):
    if values[i] == 'O' and values[i+1] == 'O' and (values[i+2] == '\x19'):
      return i+2
    elif values[i] == 'O' and values[i+2] == 'O' and (values[i+1] == '\x19'):
      return i+1
    elif values[i+1] == 'X' and values[i+2] == 'X' and (values[i] == '\x19'):
      return i
  #OVertical
  for i in range(3):
    if values[i] == 'O' and values[i+3] == 'O' and (values[i+6] == '\x19'):
      return i+6
    elif values[i] == 'O' and values[i+6] == 'O' and (values[i+3] == '\x19'):
      return i+3
    elif values[i+3] == 'O' and values[i+6] == 'O' and (values[i] == '\x19'):
      return i
  #ODiagonal
  if values[0] == 'O' and values[4] == 'O' and (values[8] == '\x19'):
    return 8
  elif values[0] == 'O' and values[8] == 'O' and (values[4] == '\x19'):
    return 4
  elif values[4] == 'O' and values[8] == 'O' and (values[0] == '\x19'):
    return 0
  elif values[2] == 'O' and values[4] == 'O' and (values[6] == '\x19'):
    return 6
  elif values[2] == 'O' and values[6] == 'O' and (values[4] == '\x19'):
    return 4
  elif values[4] == 'O' and values[6] == 'O' and (values[2] == '\x19'):
    return 2
  #XHorizontal
  for i in range(0, 9, 3):
    if values[i] == 'X' and values[i+1] == 'X' and (values[i+2] == '\x19'):
      return i+2
    elif values[i] == 'X' and values[i+2] == 'X' and (values[i+1] == '\x19'):
      return i+1
    elif values[i+1] == 'X' and values[i+2] == 'X' and (values[i] == '\x19'):
      return i
  #XVerticle
  for i in range(3):
    if values[i] == 'X' and values[i+3] == 'X' and (values[i+6] == '\x19'):
      return i+6
    elif values[i] == 'X' and values[i+6] == 'X' and (values[i+3] == '\x19'):
      return i+3
    elif values[i+3] == 'X' and values[i+6] == 'X' and (values[i] == '\x19'):
      return i
  #XDiagonal
  if values[0] == 'X' and values[4] == 'X' and (values[8] == '\x19'):
    return 8
  elif values[0] == 'X' and values[8] == 'X' and (values[4] == '\x19'):
    return 4
  elif values[4] == 'X' and values[8] == 'X' and (values[0] == '\x19'):
    return 0
  elif values[2] == 'X' and values[4] == 'X' and (values[6] == '\x19'):
    return 6
  elif values[2] == 'X' and values[6] == 'X' and (values[4] == '\x19'):
    return 4
  elif values[4] == 'X' and values[6] == 'X' and (values[2] == '\x19'):
    return 2
  if values[4] == '\x19':
    return 4
  else:
    empty = []
    for i in range(9):
      if values[i] == '\x19':
        empty.append(i)
    if (len(empty)-1) > 0:
      return empty[random.randint(0, (len(empty)-1),)]
    else:
      return "tie"

# Checks if either X's or O's have won or for a tie
def isWin(values):
# horizontal win
  for i in range(0, 9, 3):
    if values[i] == 'X' and values[i+1] == 'X' and values[i+2] == 'X':
      return 'X'
    elif values[i] == 'O' and values[i+1] == 'O' and values[i+2] == 'O':
      return 'O'
# Verticle win
  for i in range(3):
    if values[i] == 'X' and values[i+3] == 'X' and values[i+6] == 'X':
      return 'X'
    elif values[i] == 'O' and values[i+3] == 'O' and values[i+6] == 'O':
      return 'O'
# Diagonal win
  if (values[0] == 'X' and values[4] == 'X' and values[8] == 'X'):
    return 'X'
  elif((values[0] == 'O' and values[4] == 'O' and values[8] == 'O')):
    return 'O'
  elif (values[2] == 'X' and values[4] == 'X' and values[6] == 'X'):
    return 'X'
  elif (values[2] == 'O' and values[4] == 'O' and values[6] == 'O'):
    return 'O'
# Tied
  empty = []
  for i in range(9):
    if values[i] == '\x19':
      empty.append(i)
  if len(empty) == 0:
    return 'tie'

# front page initial display
@app.route('/')
def index():
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

@app.route('/tic_tac_toe', methods=['POST'])
def tic_tac_toe():
    values = [request.form[f'h{i}'] for i in range(9)]

    o_count = 0
    x_count = 0
  
    for x in range(len(values)):
      if values[x] == 'O':
        o_count+=1
    for x in range(len(values)):
      if values[x] == 'X':
        x_count+=1

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
    
    if isWin(values) == 'X' or isWin(values) == 'O':
      resp += f"<h2>{turn}'s have won</h2>"
      for i in range(9):
        resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    elif (isWin(values) == 'tie'):
      resp += f"<h2>Tied</h2>"
      for i in range(9):
        resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    else:
      for i in range(9):
        resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" {"disabled" if (values[i] == "X" or values[i] == "O") else " "}>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    
    return resp

#--------------------------------------------------------------------------------------------------------#

@app.route('/tic_tac_toe_CPU', methods=['POST'])
def tic_tac_toe2():
    values = [request.form[f'h{i}'] for i in range(9)]
  
    turn = "X"
    cTurn = "O"

    buttons = [request.form.get(f'b{i}') for i in range(9)]

    for i in range(9):
      if buttons[i] is not None:
        values[i] = turn
        
    if isWin(values) != 'X':
      if type(findWinningMove(values)) == type(1):
        values[findWinningMove(values)] = cTurn
  
    resp = ''

    if isWin(values) == 'X':
      resp += f"<h2>{turn}'s have won</h2>"
      for i in range(9):
        resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    elif isWin(values) == 'O':
      resp += f"<h2>{cTurn}'s have won</h2>"
      for i in range(9):
        resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    elif isWin(values) == 'tie':
      resp += f"<h2>Tied</h2>"
      for i in range(9):
        resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" disabled>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    else:
      for i in range(9):
        resp += f'<input name="h{i}" value="{values[i]}" type="hidden"></input>\n<button name="b{i}" type="submit" {"disabled" if (values[i] == "X" or values[i] == "O") else " "}>{values[i]}</button>\n{("<br>" if (i == 2 or i == 5) else " ")}'
    return resp

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)