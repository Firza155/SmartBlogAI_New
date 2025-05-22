<!DOCTYPE html>
<html>
<head>
    <title>Detail Artikel</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f4f6f8;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 18px;
        }

        .container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            max-width: 700px;
            width: 100%;
        }

        h1 {
            font-size: 30px;
            margin-bottom: 20px;
            color: #333333;
        }

        p {
            line-height: 1.6;
            color: #555555;
        }

        a {
            display: inline-block;
            margin-top: 30px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            transition: background-color 0.3s ease;
        }

        a:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ $article->title }}</h1>
        <p>{{ $article->body }}</p>
        <a href="{{ route('articles.index') }}">← Kembali ke Daftar</a>
    </div>
</body>
</html>
