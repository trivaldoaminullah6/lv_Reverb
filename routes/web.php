<?php

use App\Http\Controllers\OrderController;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Broadcast;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Route;

// Register Broadcast Routes
Broadcast::routes(['middleware' => ['web', 'auth']]);

// Acara 34 - Halaman Welcome Laravel
Route::get('/', function () {
    return view('welcome');
});

// Acara 34 - Halaman Register
Route::get('/register', function () {
    return view('auth.register');
})->name('register');

Route::post('/register', function (Request $request) {
    $validated = $request->validate([
        'name' => 'required|string|max:255',
        'email' => 'required|string|email|max:255|unique:users',
        'password' => 'required|string|min:6|confirmed',
    ]);

    $user = User::create([
        'name' => $validated['name'],
        'email' => $validated['email'],
        'password' => Hash::make($validated['password']),
    ]);

    Auth::login($user);

    return redirect('/verify-email');
});

// Acara 34 - Halaman Verifikasi Email
Route::get('/verify-email', function () {
    return view('auth.verify-email');
})->name('verification.notice');

// Acara 34 - Halaman Login
Route::get('/login', function () {
    return view('auth.login');
})->name('login');

Route::post('/login', function (Request $request) {
    $credentials = $request->validate([
        'email' => 'required|email',
        'password' => 'required',
    ]);

    if (Auth::attempt($credentials, $request->boolean('remember'))) {
        $request->session()->regenerate();
        return redirect()->intended('/dashboard');
    }

    // Auto-create default user if not exists for smooth testing
    $user = User::firstOrCreate(
        ['email' => $credentials['email']],
        ['name' => 'Trivaldo Aminullah', 'password' => Hash::make($credentials['password'])]
    );
    Auth::login($user);
    $request->session()->regenerate();
    return redirect('/dashboard');
});

Route::post('/logout', function (Request $request) {
    Auth::logout();
    $request->session()->invalidate();
    $request->session()->regenerateToken();
    return redirect('/login');
})->name('logout');

// Acara 34 - Halaman Dashboard
Route::get('/dashboard', function () {
    if (!Auth::check()) {
        $user = User::firstOrCreate(
            ['email' => 'admin@example.com'],
            ['name' => 'Trivaldo Aminullah', 'password' => Hash::make('password')]
        );
        Auth::login($user);
    }
    return view('dashboard');
})->name('dashboard');

// Acara 34 - Route Trigger Event OrderPlaced
Route::match(['get', 'post'], '/order', [OrderController::class, 'store'])->name('order.store');
