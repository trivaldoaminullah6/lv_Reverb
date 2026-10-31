<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>Dashboard - Laravel Reverb Broadcasting</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=figtree:400,500,600,700&display=swap" rel="stylesheet" />
    <!-- Load Pusher and Laravel Echo via CDN for immediate execution -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pusher/8.3.0/pusher.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/laravel-echo/1.16.1/echo.iife.js"></script>
</head>
<body class="font-sans antialiased bg-gray-100 min-h-screen">
    <!-- Navigation -->
    <nav class="bg-white border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex">
                    <div class="shrink-0 flex items-center">
                        <span class="text-xl font-bold text-indigo-600 flex items-center gap-2">
                            <svg class="w-8 h-8 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                            </svg>
                            Laravel Reverb
                        </span>
                    </div>
                    <div class="hidden space-x-8 sm:-my-px sm:ms-10 sm:flex">
                        <a href="/dashboard" class="inline-flex items-center px-1 pt-1 border-b-2 border-indigo-400 text-sm font-medium leading-5 text-gray-900 focus:outline-none focus:border-indigo-700 transition duration-150 ease-in-out">
                            Dashboard
                        </a>
                    </div>
                </div>

                <div class="flex items-center gap-4">
                    <span class="text-sm font-semibold text-gray-700">{{ auth()->user()->name ?? 'Trivaldo Aminullah' }} (User ID: {{ auth()->id() ?? 1 }})</span>
                    <form method="POST" action="/logout">
                        @csrf
                        <button type="submit" class="text-sm text-red-600 hover:text-red-800 font-medium">Log Out</button>
                    </form>
                </div>
            </div>
        </div>
    </nav>

    <!-- Page Header -->
    <header class="bg-white shadow">
        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
            <div>
                <h2 class="font-semibold text-2xl text-gray-800 leading-tight">
                    Dashboard Notifikasi Real-Time (Acara 34)
                </h2>
                <p class="text-sm text-gray-500 mt-1">Pengujian Event Broadcasting WebSocket menggunakan Laravel Reverb & Laravel Echo</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-green-100 text-green-800">
                    <span class="w-2 h-2 me-1.5 bg-green-500 rounded-full animate-pulse"></span>
                    WebSocket Connected
                </span>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="py-10">
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8 space-y-6">

            <!-- Notification Alert Banner (Hidden by default) -->
            <div id="toastNotification" class="hidden bg-indigo-50 border-l-4 border-indigo-500 p-4 rounded shadow-md transition-all duration-300">
                <div class="flex items-center">
                    <div class="flex-shrink-0">
                        <svg class="h-6 w-6 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                        </svg>
                    </div>
                    <div class="ml-3">
                        <p id="toastMessage" class="text-sm font-semibold text-indigo-900"></p>
                    </div>
                </div>
            </div>

            <!-- Action Panel -->
            <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg p-6">
                <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                    <div>
                        <h3 class="text-lg font-bold text-gray-900">Uji Event Broadcasting Transaksi</h3>
                        <p class="text-sm text-gray-600 mt-1">Klik tombol di samping untuk memicu event <code class="bg-gray-100 px-2 py-0.5 rounded text-indigo-600 font-mono">OrderPlaced</code> melalui route <code class="bg-gray-100 px-2 py-0.5 rounded text-indigo-600 font-mono">POST /order</code>.</p>
                    </div>
                    <div>
                        <button id="btnTesNotifikasi" onclick="triggerOrder()" class="inline-flex items-center px-6 py-3 bg-indigo-600 border border-transparent rounded-lg font-bold text-sm text-white uppercase tracking-wider hover:bg-indigo-700 active:bg-indigo-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition ease-in-out duration-150 shadow-lg cursor-pointer">
                            <svg class="w-5 h-5 me-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                            </svg>
                            Tes Notifikasi
                        </button>
                    </div>
                </div>
            </div>

            <!-- Status and Logs Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Configuration Details -->
                <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg p-6">
                    <h4 class="font-bold text-gray-900 text-md mb-3 flex items-center gap-2">
                        <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        </svg>
                        Konfigurasi Broadcast
                    </h4>
                    <div class="space-y-2 text-sm text-gray-600">
                        <div class="flex justify-between py-1 border-b">
                            <span class="font-medium">Broadcaster:</span>
                            <span class="font-mono text-indigo-600 font-bold">Laravel Reverb</span>
                        </div>
                        <div class="flex justify-between py-1 border-b">
                            <span class="font-medium">Host / Port:</span>
                            <span class="font-mono">127.0.0.1 : 8080</span>
                        </div>
                        <div class="flex justify-between py-1 border-b">
                            <span class="font-medium">Private Channel:</span>
                            <span class="font-mono text-indigo-600">user.{{ auth()->id() ?? 1 }}</span>
                        </div>
                        <div class="flex justify-between py-1 border-b">
                            <span class="font-medium">Event Name:</span>
                            <span class="font-mono text-indigo-600">order.placed (OrderPlaced)</span>
                        </div>
                        <div class="flex justify-between py-1">
                            <span class="font-medium">User Aktif:</span>
                            <span class="font-semibold">{{ auth()->user()->name ?? 'Trivaldo Aminullah' }} ({{ auth()->user()->email ?? 'admin@example.com' }})</span>
                        </div>
                    </div>
                </div>

                <!-- Event Log Box -->
                <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg p-6">
                    <h4 class="font-bold text-gray-900 text-md mb-3 flex items-center gap-2">
                        <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                        Event Broadcast Log
                    </h4>
                    <div id="eventLogContainer" class="bg-gray-900 text-green-400 p-3 rounded font-mono text-xs h-40 overflow-y-auto space-y-1">
                        <div>[System] Terhubung ke Reverb WebSocket pada ws://127.0.0.1:8080...</div>
                        <div>[Channel] Subscribed ke private channel: user.{{ auth()->id() ?? 1 }}</div>
                        <div id="waitingMsg" class="text-gray-400">[Listener] Menunggu event OrderPlaced dikirim...</div>
                    </div>
                </div>
            </div>

        </div>
    </main>

    <!-- Script Listener Echo & Trigger -->
    <script>
        const userId = {{ auth()->id() ?? 1 }};
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

        // Setup Echo
        window.Echo = new Echo({
            broadcaster: 'reverb',
            key: 'x9a2k8m4yq7p1w5c0v3d',
            wsHost: window.location.hostname || '127.0.0.1',
            wsPort: 8080,
            wssPort: 8080,
            forceTLS: false,
            enabledTransports: ['ws', 'wss'],
            authEndpoint: '/broadcasting/auth',
            auth: {
                headers: {
                    'X-CSRF-TOKEN': csrfToken
                }
            }
        });

        function handleIncomingOrder(e) {
            console.log('Order Placed:', e);
            const msg = `Order #${e.order_id} telah ditempatkan! Total: Rp ${e.total}`;

            // Tampilkan di Log box
            const logBox = document.getElementById('eventLogContainer');
            const newLog = document.createElement('div');
            newLog.className = 'text-yellow-300 font-bold';
            newLog.innerText = `[Received] ${msg} (User: ${e.user_name || 'Trivaldo Aminullah'})`;
            logBox.appendChild(newLog);
            logBox.scrollTop = logBox.scrollHeight;

            // Tampilkan Toast Banner
            const banner = document.getElementById('toastNotification');
            document.getElementById('toastMessage').innerText = msg;
            banner.classList.remove('hidden');

            // Trigger browser alert
            alert(msg);
        }

        // Listener Laravel Echo
        window.Echo.private(`user.${userId}`)
            .listen('.order.placed', (e) => {
                handleIncomingOrder(e);
            })
            .listen('OrderPlaced', (e) => {
                handleIncomingOrder(e);
            });

        // Trigger Event via Fetch
        async function triggerOrder() {
            try {
                const response = await fetch('/order', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': csrfToken,
                        'Accept': 'application/json'
                    }
                });
                const data = await response.json();
                console.log('API Response:', data);

                const logBox = document.getElementById('eventLogContainer');
                const triggerLog = document.createElement('div');
                triggerLog.className = 'text-cyan-400';
                triggerLog.innerText = `[Dispatched] Event OrderPlaced berhasil dipicu (Order #${data.order_id}, Total: Rp ${data.total})`;
                logBox.appendChild(triggerLog);
            } catch (err) {
                console.error('Trigger Error:', err);
            }
        }
    </script>
</body>
</html>
