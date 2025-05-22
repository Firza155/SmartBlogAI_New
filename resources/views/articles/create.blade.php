<!DOCTYPE html>
<html>
<head>
    <title>Tambah Artikel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
            position: relative;
            min-height: 100vh;
        }
        h1 {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }
        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 20px auto;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            position: relative;
        }
        input[type="text"], textarea {
            width: calc(100% - 20px);
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        textarea {
            height: 150px;
        }
        button, .back-button {
            background-color: #5a67d8;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            font-size: 16px;
        }
        button:hover, .back-button:hover {
            background-color:rgb(66, 154, 83);
        }
        .error {
            color: red;
            margin-bottom: 10px;
        }
        form div {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
        }
    </style>
</head>
<body>
    <h1>Tambah Artikel Baru</h1>

    @if ($errors->any())
        <div class="error">
            <strong>Ups!</strong> Ada kesalahan:<br>
            <ul>
                @foreach ($errors->all() as $error)
                    <li>{{ $error }}</li>
                @endforeach
            </ul>
        </div>
    @endif

    <form action="{{ route('articles.store') }}" method="POST">
        @csrf
        <label>Judul:</label><br>
        <input type="text" name="title" value="{{ old('title') }}" placeholder="Judul Artikel"><br><br>

        <label>Isi:</label><br>
        <textarea name="content" placeholder="Isi Artikel">{{ old('content') }}</textarea><br><br>

        <div>
            <button type="submit">Simpan</button>
            <a href="{{ route('articles.index') }}" class="back-button">Kembali</a>
        </div>
    </form>
</body>
</html>
