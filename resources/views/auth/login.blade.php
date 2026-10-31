<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Log in - Laravel Reverb</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=figtree:400,500,600&display=swap" rel="stylesheet" />
</head>
<body class="font-sans text-gray-900 antialiased bg-gray-100 flex flex-col sm:justify-center items-center pt-6 sm:pt-0 min-h-screen">
    <div>
        <a href="/">
            <svg class="w-16 h-16 fill-current text-red-600" viewBox="0 0 62 65" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M61.8548 14.6253C61.8778 14.7102 61.8895 14.7978 61.8897 14.8858V28.5615C61.8898 29.8607 60.8372 30.9135 59.538 30.9138H48.4379C48.0699 30.9137 47.708 30.8252 47.3812 30.6554L34.1956 23.8291C33.7297 23.5878 33.4356 23.1047 33.4355 22.5804V8.90469C33.4355 7.60555 34.4882 6.55273 35.7874 6.55273H46.8875C47.2554 6.55286 47.6173 6.64134 47.9441 6.81119L61.1298 13.6375C61.4648 13.8111 61.7208 14.1673 61.8548 14.6253Z"/>
            </svg>
        </a>
    </div>

    <div class="w-full sm:max-w-md mt-6 px-6 py-4 bg-white shadow-md overflow-hidden sm:rounded-lg">
        @if ($errors->any())
            <div class="mb-4 text-sm text-red-600">
                <ul>
                    @foreach ($errors->all() as $error)
                        <li>{{ $error }}</li>
                    @endforeach
                </ul>
            </div>
        @endif

        <form method="POST" action="/login">
            @csrf
            <div>
                <label class="block font-medium text-sm text-gray-700" for="email">Email</label>
                <input class="border-gray-300 focus:border-indigo-500 focus:ring-indigo-500 rounded-md shadow-sm block mt-1 w-full border p-2" id="email" type="email" name="email" value="{{ old('email', 'admin@example.com') }}" required autofocus autocomplete="username" />
            </div>

            <div class="mt-4">
                <label class="block font-medium text-sm text-gray-700" for="password">Password</label>
                <input class="border-gray-300 focus:border-indigo-500 focus:ring-indigo-500 rounded-md shadow-sm block mt-1 w-full border p-2" id="password" type="password" name="password" required autocomplete="current-password" value="password" />
            </div>

            <div class="block mt-4">
                <label for="remember_me" class="inline-flex items-center">
                    <input id="remember_me" type="checkbox" class="rounded border-gray-300 text-indigo-600 shadow-sm focus:ring-indigo-500" name="remember">
                    <span class="ms-2 text-sm text-gray-600">Remember me</span>
                </label>
            </div>

            <div class="flex items-center justify-between mt-4">
                <a class="underline text-sm text-gray-600 hover:text-gray-900 rounded-md focus:outline-none" href="/register">
                    Belum punya akun? Register
                </a>

                <button type="submit" class="inline-flex items-center px-4 py-2 bg-gray-800 border border-transparent rounded-md font-semibold text-xs text-white uppercase tracking-widest hover:bg-gray-700 focus:bg-gray-700 active:bg-gray-900 focus:outline-none transition ease-in-out duration-150 ms-3">
                    Log in
                </button>
            </div>
        </form>
    </div>
</body>
</html>
