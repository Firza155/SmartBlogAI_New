<!DOCTYPE html>
<html>
<head>
    <title>Edit Artikel</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #f0f2f5;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 18px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 100%;
        }

        h1 {
            text-align: center;
            color: #333333;
            margin-bottom: 30px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #444444;
        }

        input[type="text"],
        textarea {
            width: 100%;
            padding: 10px;
            border-radius: 6px;
            border: 1px solid #cccccc;
            font-size: 16px;
            margin-bottom: 20px;
            box-sizing: border-box;
        }

        textarea {
            resize: vertical;
            min-height: 150px;
        }

        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #218838;
        }

        a {
            display: inline-block;
            margin-top: 20px;
            color: #007bff;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .error-box {
            background-color: #ffe6e6;
            border-left: 6px solid #ff4d4d;
            padding: 15px;
            margin-bottom: 20px;
            color: #cc0000;
        }

        .error-box ul {
            margin: 0;
            padding-left: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Edit Artikel</h1>

        @if ($errors->any())
            <div class="error-box">
                <strong>Ups!</strong> Ada kesalahan:<br>
                <ul>
                    @foreach ($errors->all() as $error)
                        <li>{{ $error }}</li>
                    @endforeach
                </ul>
            </div>
        @endif

        <form action="{{ route('articles.update', $article->id) }}" method="POST">
            @csrf
            @method('PUT')

            <label>Judul:</label>
            <input type="text" name="title" value="{{ old('title', $article->title) }}">

            <label>Isi:</label>
            <textarea name="content">{{ old('content', $article->body) }}</textarea>

            <button type="submit">Update</button>
        </form>

        <a href="{{ route('articles.index') }}">← Kembali ke Daftar</a>
    </div>
</body>
</html>
