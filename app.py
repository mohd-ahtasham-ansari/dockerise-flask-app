from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic Tac Toe</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #141e30, #243b55);
            color: white;
        }

        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.08);
            padding: 40px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
        }

        h1 {
            font-size: 42px;
            margin-bottom: 10px;
        }

        p {
            color: #bbb;
            margin-bottom: 25px;
        }

        .board {
            display: grid;
            grid-template-columns: repeat(3, 90px);
            gap: 10px;
            justify-content: center;
            margin-bottom: 25px;
        }

        .cell {
            width: 90px;
            height: 90px;
            border: none;
            border-radius: 15px;
            background: rgba(255,255,255,0.12);
            color: white;
            font-size: 40px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.2s;
        }

        .cell:hover {
            background: rgba(255,255,255,0.22);
            transform: scale(1.05);
        }

        .restart {
            padding: 12px 25px;
            border: none;
            border-radius: 10px;
            background: #00c6ff;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }

        .restart:hover {
            background: #0072ff;
        }

        #status {
            margin-bottom: 20px;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>❌ Tic Tac Toe ⭕</h1>
    <p>Flask Demo Application</p>

    <div id="status">Player X's Turn</div>

    <div class="board">
        <button class="cell" onclick="play(0)"></button>
        <button class="cell" onclick="play(1)"></button>
        <button class="cell" onclick="play(2)"></button>

        <button class="cell" onclick="play(3)"></button>
        <button class="cell" onclick="play(4)"></button>
        <button class="cell" onclick="play(5)"></button>

        <button class="cell" onclick="play(6)"></button>
        <button class="cell" onclick="play(7)"></button>
        <button class="cell" onclick="play(8)"></button>
    </div>

    <button class="restart" onclick="restart()">
        🔄 New Game
    </button>

</div>

<script>

    let board = ["", "", "", "", "", "", "", "", ""];
    let currentPlayer = "X";
    let gameOver = false;

    const cells = document.querySelectorAll(".cell");
    const status = document.getElementById("status");

    const winningCombinations = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ];

    function play(index) {

        if (board[index] !== "" || gameOver) {
            return;
        }

        board[index] = currentPlayer;
        cells[index].textContent = currentPlayer;

        if (checkWinner()) {
            status.textContent = "🎉 Player " + currentPlayer + " Wins!";
            gameOver = true;
            return;
        }

        if (!board.includes("")) {
            status.textContent = "🤝 It's a Draw!";
            gameOver = true;
            return;
        }

        currentPlayer = currentPlayer === "X" ? "O" : "X";

        status.textContent = "Player " + currentPlayer + "'s Turn";
    }

    function checkWinner() {

        for (let combination of winningCombinations) {

            const [a, b, c] = combination;

            if (
                board[a] !== "" &&
                board[a] === board[b] &&
                board[a] === board[c]
            ) {
                return true;
            }
        }

        return false;
    }

    function restart() {

        board = ["", "", "", "", "", "", "", "", ""];
        currentPlayer = "X";
        gameOver = false;

        cells.forEach(cell => {
            cell.textContent = "";
        });

        status.textContent = "Player X's Turn";
    }

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)