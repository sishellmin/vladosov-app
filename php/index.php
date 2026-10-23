<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Экономика — Тьютор</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }
        .card { background: #f4f4f9; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; }
        h1 { color: #2c3e50; }
        input, button { padding: 0.5rem; font-size: 1rem; margin: 4px; }
        #result { margin-top: 1rem; font-weight: bold; color: #27ae60; }
    </style>
</head>
<body>
    <h1>Тьютор по экономике</h1>
    <div class="card">
        <h2>Калькулятор сложного процента</h2>
        <p>Введите сумму, ставку и количество лет.</p>
        <input type="number" id="principal" placeholder="Сумма" value="1000">
        <input type="number" id="rate" placeholder="Ставка, %" value="5">
        <input type="number" id="years" placeholder="Лет" value="10">
        <button onclick="calculate()">Рассчитать</button>
        <div id="result"></div>
    </div>
    <script>
        function calculate() {
            const p = parseFloat(document.getElementById("principal").value);
            const r = parseFloat(document.getElementById("rate").value) / 100;
            const t = parseFloat(document.getElementById("years").value);
            if (isNaN(p) || isNaN(r) || isNaN(t)) {
                document.getElementById("result").innerText = "Заполните все поля.";
                return;
            }
            const total = p * Math.pow(1 + r, t);
            document.getElementById("result").innerText =
                "Итоговая сумма: " + total.toFixed(2) +
                " (прибыль: " + (total - p).toFixed(2) + ")";
        }
    </script>
</body>
</html>
