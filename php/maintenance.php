<?php
declare(strict_types=1);

$phrase = 'Палкой весело махать, полосатой!';
?>
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Палкой весело махать</title>
    <style>
        *{box-sizing:border-box}
        html,body{margin:0;min-height:100%;font-family:Arial,Helvetica,sans-serif}
        body{
            min-height:100vh;
            display:flex;
            align-items:center;
            justify-content:center;
            background:#101010;
            color:#fff;
            overflow:hidden;
        }
        .page{
            width:100%;
            min-height:100vh;
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            padding:40px 20px;
            text-align:center;
            background:
                radial-gradient(circle at 50% 45%,#303030 0,#181818 45%,#080808 100%);
        }
        .baton{
            width:min(520px,75vw);
            height:min(260px,38vw);
            position:relative;
            margin-bottom:38px;
            transform:rotate(-18deg);
            filter:drop-shadow(0 24px 22px rgba(0,0,0,.6));
        }
        /* Корпус жезла */
        .stick{
            position:absolute;
            left:10%;
            top:40%;
            width:80%;
            height:25%;
            border-radius:999px;
            border:6px solid #090909;
            background:repeating-linear-gradient(
                90deg,
                #111 0 42px,
                #f1f1f1 42px 84px
            );
            box-shadow:inset 0 3px 4px rgba(255,255,255,.25),
                       inset 0 -5px 7px rgba(0,0,0,.5);
        }
        .end{
            position:absolute;
            width:10%;
            height:31%;
            top:37%;
            border:6px solid #080808;
            background:#111;
        }
        .end.left{left:5%;border-radius:50% 8px 8px 50%}
        .end.right{right:5%;border-radius:8px 50% 50% 8px}
        .grip{
            position:absolute;
            left:30%;
            top:35%;
            width:27%;
            height:35%;
            border-radius:13px;
            border:5px solid #080808;
            background:repeating-linear-gradient(
                0deg,
                #0a0a0a 0 15px,
                #222 15px 30px
            );
            box-shadow:inset 0 0 10px rgba(255,255,255,.08);
        }
        h1{
            margin:0;
            max-width:1000px;
            font-size:clamp(34px,6vw,78px);
            line-height:1.03;
            letter-spacing:-2px;
            font-weight:900;
        }
        .small{
            margin-top:20px;
            color:#999;
            font-size:14px;
        }
    </style>
</head>
<body>
<main class="page">
    <div class="baton" aria-label="Полицейский полосатый жезл" role="img">
        <div class="stick"></div>
        <div class="end left"></div>
        <div class="end right"></div>
        <div class="grip"></div>
    </div>

    <h1><?= htmlspecialchars($phrase, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') ?></h1>
    <div class="small">Перерыв на шоколадку, звоните, 89101418451 </div>
</main>
</body>
</html>
