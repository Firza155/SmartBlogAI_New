<?php

namespace App\Http\Controllers;

use App\Models\Article;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;

class ArticleController extends Controller
{
    use AuthorizesRequests; // ✅ Tambahkan baris ini

    public function index()
    {
        $articles = Article::latest()->where('user_id', Auth::id())->get();
        return view('articles.index', compact('articles'));
    }

    public function create()
    {
        return view('articles.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'title' => 'required',
            'content' => 'required',
        ]);

        Auth::user()->articles()->create([
            'title' => $request->input('title'),
            'body' => $request->input('content'),
        ]);

        return redirect()->route('articles.index')->with('success', 'Artikel berhasil dibuat!');
    }

    public function show(Article $article)
    {
        return view('articles.show', compact('article'));
    }

    public function edit(Article $article)
    {
        $this->authorize('update', $article);
        return view('articles.edit', compact('article'));
    }

    public function update(Request $request, Article $article)
    {
        $this->authorize('update', $article);

        $request->validate([
            'title' => 'required',
            'content' => 'required',
        ]);

        $article->update([
            'title' => $request->input('title'),
            'body' => $request->input('content'),
        ]);

        return redirect()->route('articles.index')->with('success', 'Artikel berhasil diperbarui!');
    }

    public function destroy(Article $article)
    {
        // $this->authorize('delete', $article);
        $article->delete();
        return redirect()->route('articles.index')->with('success', 'Artikel berhasil dihapus!');
    }
}
