<!DOCTYPE html>
<html>
<head>
    <title>Daftar Artikel</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center; /* horizontal center */
            align-items: center;     /* vertical center */
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            max-width: 600px;
            width: 100%;
        }

        h1 {
            text-align: center;
        }

        ul {
            padding-left: 0;
            list-style: none;
        }

        li {
            margin-bottom: 10px;
        }

        hr {
            border: none;
            border-top: 1px solid #ccc;
            margin: 10px 0;
        }

        a {
            text-decoration: none;
            color: #007bff;
        }

        a.button {
            background-color: #5a67d8;
            color: white;
            padding: 3px 8px;
            border-radius: 4px;
            text-decoration: none;
            font-size: 16px;
            margin-right: 5px;
        }
        a.button:hover {
            background-color: rgb(66, 154, 83);
        }

        button {
            background:rgb(224, 76, 91);
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background:rgb(255, 0, 25);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Artikel Saya</h1>

        @if (session('success'))
            <p style="color: green;">{{ session('success') }}</p>
        @endif

        <a href="{{ route('articles.create') }}" class="button">+ Tambah Artikel</a><br><br>

        @if ($articles->count())
            <ul>
                @foreach ($articles as $article)
                    <li>
                        <strong>{{ $article->title }}</strong><br>
                        <a href="{{ route('articles.show', $article->id) }}" class="button">Lihat</a> |
                        <a href="{{ route('articles.edit', $article->id) }}" class="button">Edit</a> |
                        <form action="{{ route('articles.destroy', $article->id) }}" method="POST" style="display:inline;">
                            @csrf
                            @method('DELETE')
                            <button type="submit" class="btn-hapus" onclick="return confirm('Yakin ingin hapus artikel ini?')" >Hapus</button>
                        </form>
                    </li>
                    <hr>
                @endforeach
            </ul>
        @else
            <p>Kamu belum membuat artikel.</p>
        @endif
    </div>
</body>
</html>
