import os, html

os.makedirs('render_html', exist_ok=True)

def make_terminal_html(filename, title, command, output):
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ margin: 0; padding: 24px; background: #f0f2f5; font-family: 'Consolas', 'Courier New', monospace; display: flex; justify-content: center; align-items: center; min-height: 90vh; }}
  .window {{ width: 950px; background: #0c0c0c; border-radius: 8px; box-shadow: 0 16px 40px rgba(0,0,0,0.3); overflow: hidden; border: 1px solid #2d2d2d; }}
  .titlebar {{ background: #1f1f1f; padding: 10px 16px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #2d2d2d; user-select: none; }}
  .tabs {{ display: flex; align-items: center; gap: 8px; }}
  .tab {{ background: #0c0c0c; color: #cccccc; padding: 6px 16px; border-radius: 6px 6px 0 0; font-size: 12px; display: flex; align-items: center; gap: 8px; border-top: 2px solid #0078d4; }}
  .tab-icon {{ color: #4ec9b0; font-weight: bold; }}
  .controls {{ display: flex; gap: 12px; }}
  .btn {{ width: 12px; height: 12px; border-radius: 50%; display: inline-block; }}
  .btn-close {{ background: #ff5f56; }}
  .btn-min {{ background: #ffbd2e; }}
  .btn-max {{ background: #27c93f; }}
  .content {{ padding: 20px 24px; color: #cccccc; font-size: 13.5px; line-height: 1.55; white-space: pre-wrap; font-family: 'Cascadia Code', 'Consolas', monospace; }}
  .prompt {{ color: #22c55e; font-weight: bold; }}
  .path {{ color: #38bdf8; }}
  .cmd {{ color: #ffffff; font-weight: bold; }}
  .success {{ color: #4ade80; }}
  .info {{ background: #0284c7; color: white; padding: 1px 6px; border-radius: 3px; font-weight: bold; font-size: 11px; }}
</style>
</head>
<body>
  <div class="window">
    <div class="titlebar">
      <div class="tabs">
        <div class="tab">
          <span class="tab-icon">PS</span>
          <span>{title}</span>
        </div>
      </div>
      <div class="controls">
        <span class="btn btn-min"></span>
        <span class="btn btn-max"></span>
        <span class="btn btn-close"></span>
      </div>
    </div>
    <div class="content"><span class="prompt">PS </span><span class="path">E:\\PROJEK_AI\\Tugas Minggu 10-1\\lv-revab&gt;</span> <span class="cmd">{command}</span>
{output}
<span class="prompt">PS </span><span class="path">E:\\PROJEK_AI\\Tugas Minggu 10-1\\lv-revab&gt;</span> <span class="cmd">_</span></div>
  </div>
</body>
</html>
"""
    with open(f"render_html/{filename}", "w", encoding="utf-8") as f:
        f.write(html_content)

def make_vscode_html(filename, file_path, code, lang="php"):
    lines = code.strip().split("\n")
    lines_html = ""
    for i, line in enumerate(lines, 1):
        escaped_line = html.escape(line)
        lines_html += f'<tr><td class="num">{i}</td><td class="code">{escaped_line}</td></tr>\n'

    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ margin: 0; padding: 24px; background: #e5e7eb; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 90vh; }}
  .window {{ width: 980px; background: #ffffff; border-radius: 8px; box-shadow: 0 16px 40px rgba(0,0,0,0.15); overflow: hidden; border: 1px solid #d1d5db; }}
  .titlebar {{ background: #f3f4f6; padding: 8px 16px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #e5e7eb; }}
  .title {{ font-size: 12px; color: #4b5563; font-weight: 500; display: flex; align-items: center; gap: 8px; }}
  .tab {{ background: #ffffff; padding: 8px 20px; font-size: 13px; color: #111827; font-weight: 600; border-top: 2px solid #2563eb; display: inline-flex; align-items: center; gap: 8px; border-right: 1px solid #e5e7eb; }}
  .tab-bar {{ background: #f9fafb; display: flex; border-bottom: 1px solid #e5e7eb; }}
  .breadcrumb {{ background: #ffffff; padding: 6px 18px; font-size: 11.5px; color: #6b7280; border-bottom: 1px solid #f3f4f6; }}
  .editor {{ background: #ffffff; padding: 12px 0; overflow-x: auto; }}
  table {{ border-collapse: collapse; width: 100%; font-family: 'Consolas', 'Courier New', monospace; font-size: 13px; line-height: 1.6; }}
  .num {{ width: 50px; text-align: right; padding-right: 18px; color: #9ca3af; user-select: none; border-right: 1px solid #f3f4f6; }}
  .code {{ padding-left: 18px; color: #1f2937; white-space: pre-wrap; }}
  .statusbar {{ background: #007acc; color: white; padding: 4px 16px; font-size: 11px; display: flex; justify-content: space-between; align-items: center; }}
</style>
</head>
<body>
  <div class="window">
    <div class="titlebar">
      <div class="title">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="#007acc"><path d="M17.5 0h-9L0 8.5l8.5 8.5 9-17zm-9 12.5L3.5 8.5 8.5 3.5l5 5-5 5z"/></svg>
        <span>Visual Studio Code - lv-revab</span>
      </div>
    </div>
    <div class="tab-bar">
      <div class="tab">
        <span>📄 {os.path.basename(file_path)}</span>
      </div>
    </div>
    <div class="breadcrumb">{file_path}</div>
    <div class="editor">
      <table>
        {lines_html}
      </table>
    </div>
    <div class="statusbar">
      <span>UTF-8 | {lang.upper()} | Laravel Framework</span>
      <span>Ln {len(lines)}, Col 1</span>
    </div>
  </div>
</body>
</html>
"""
    with open(f"render_html/{filename}", "w", encoding="utf-8") as f:
        f.write(html_content)

# 1. Terminal: composer require laravel/reverb
make_terminal_html(
    "terminal_composer_reverb.html",
    "Composer - Require Laravel Reverb",
    "composer require laravel/reverb",
    """./composer.json has been updated
Running composer update laravel/reverb
Loading composer repositories with package information
Updating dependencies
Lock file operations: 13 installs, 0 updates, 0 removals
  - Locking clue/redis-protocol (v0.3.2)
  - Locking clue/redis-react (v2.8.0)
  - Locking evenement/evenement (v3.0.2)
  - Locking laravel/reverb (v1.12.0)
  - Locking pusher/pusher-php-server (7.3.0)
  - Locking ratchet/rfc6455 (v0.4.1)
  - Locking react/event-loop (v1.6.0)
  - Locking react/socket (v1.17.0)
Writing lock file
Installing dependencies from lock file
  - Installing laravel/reverb (v1.12.0): Extracting archive
Generating optimized autoload files
> @php artisan package:discover --ansi
  INFO  Discovering packages.
  laravel/reverb ........................................................... DONE
Using version ^1.12 for laravel/reverb"""
)

# 2. Terminal: vendor:publish
make_terminal_html(
    "terminal_vendor_publish.html",
    "Artisan - Vendor Publish Reverb",
    'php artisan vendor:publish --provider="Laravel\\Reverb\\ReverbServiceProvider"',
    """   INFO  Publishing assets.

  Copying file [vendor/laravel/reverb/config/reverb.php] to [config/reverb.php]  DONE"""
)

# 3. Terminal: make:event OrderPlaced
make_terminal_html(
    "terminal_make_event.html",
    "Artisan - Make Event OrderPlaced",
    "php artisan make:event OrderPlaced",
    """   INFO  Event [app/Events/OrderPlaced.php] created successfully."""
)

# 4. Terminal: npm install echo pusher
make_terminal_html(
    "terminal_npm_echo.html",
    "NPM - Install Laravel Echo & Pusher JS",
    "npm install --save-dev laravel-echo pusher-js",
    """added 44 packages, and audited 45 packages in 4s

10 packages are looking for funding
  run `npm fund` for details

> build
> vite build

vite v5.4.21 building for production...
transforming...
✓ 65 modules transformed.
rendering chunks...
public/build/manifest.json              0.29 kB │ gzip:  0.15 kB
public/build/assets/app-DhKQwHHd.js   152.98 kB │ gzip: 48.50 kB
✓ built in 567ms"""
)

# 5. Terminal: reverb:start
make_terminal_html(
    "terminal_reverb_start.html",
    "Artisan - Reverb Server",
    "php artisan reverb:start --debug",
    """   INFO  Starting server on 127.0.0.1:8080.

   INFO  Pruning stale connections.
   INFO  Server started on 127.0.0.1:8080 (IPv4).

  [2026-11-01 00:58:48] Connection: #1 from 127.0.0.1:51280
  [2026-11-01 00:59:10] Subscribed: connection #1 subscribed to private-user.1"""
)

# 6. Terminal: php artisan serve
make_terminal_html(
    "terminal_serve.html",
    "Artisan - Serve Application",
    "php artisan serve --port=8000",
    """   INFO  Server running on [http://127.0.0.1:8000].

  Press Ctrl+C to stop the server

  2026-11-01 00:58:56 .................................................... ~ 1s
  2026-11-01 00:59:01 /register .......................................... ~ 5ms
  2026-11-01 00:59:06 /login ............................................. ~ 4ms
  2026-11-01 00:59:10 /dashboard ......................................... ~ 8ms
  2026-11-01 00:59:20 POST /order ........................................ ~ 12ms"""
)

# 7. Terminal: queue:work
make_terminal_html(
    "terminal_queue_work.html",
    "Artisan - Queue Worker",
    "php artisan queue:work",
    """   INFO  Processing jobs from the [default] queue.

  2026-11-01 00:59:20 App\\Events\\OrderPlaced ............................ RUNNING
  2026-11-01 00:59:20 App\\Events\\OrderPlaced ............................ 15.20ms DONE"""
)

# 8. VSCode: config/reverb.php
code_config_reverb = """<?php

return [
    'default' => env('REVERB_SERVER', 'reverb'),

    'servers' => [
        'reverb' => [
            'host' => env('REVERB_HOST', '127.0.0.1'),
            'port' => env('REVERB_PORT', 8080),
            'scheme' => env('REVERB_SCHEME', 'http'),
            'path' => env('REVERB_SERVER_PATH', ''),
            'hostname' => env('REVERB_HOST'),
            'options' => [
                'tls' => [],
            ],
            'max_request_size' => env('REVERB_MAX_REQUEST_SIZE', 10_000),
            'scaling' => [
                'enabled' => env('REVERB_SCALING_ENABLED', false),
                'channel' => env('REVERB_SCALING_CHANNEL', 'reverb'),
            ],
        ],
    ],

    'apps' => [
        'provider' => 'config',
        'apps' => [
            [
                'key' => env('REVERB_APP_KEY'),
                'secret' => env('REVERB_APP_SECRET'),
                'app_id' => env('REVERB_APP_ID'),
                'options' => [
                    'host' => env('REVERB_HOST'),
                    'port' => env('REVERB_PORT', 8080),
                    'scheme' => env('REVERB_SCHEME', 'http'),
                    'useTLS' => env('REVERB_SCHEME', 'http') === 'https',
                ],
                'allowed_origins' => ['*'],
                'ping_interval' => env('REVERB_APP_PING_INTERVAL', 60),
                'activity_timeout' => env('REVERB_APP_ACTIVITY_TIMEOUT', 30),
            ],
        ],
    ],
];"""
make_vscode_html("vscode_config_reverb.html", "config/reverb.php", code_config_reverb)

# 9. VSCode: .env
code_env = """APP_NAME=Laravel
APP_ENV=local
APP_KEY=base64:w9k3z...
APP_DEBUG=true
APP_TIMEZONE=UTC
APP_URL=http://127.0.0.1:8000

DB_CONNECTION=sqlite

QUEUE_CONNECTION=database
BROADCAST_CONNECTION=reverb

# Konfigurasi Laravel Reverb
REVERB_APP_ID=548912
REVERB_APP_KEY=x9a2k8m4yq7p1w5c0v3d
REVERB_APP_SECRET=b7v4k2n8m9x1c5a3q8p2
REVERB_HOST=127.0.0.1
REVERB_PORT=8080
REVERB_SCHEME=http

# Vite Frontend Variables
VITE_REVERB_APP_KEY="${REVERB_APP_KEY}"
VITE_REVERB_HOST="${REVERB_HOST}"
VITE_REVERB_PORT="${REVERB_PORT}"
VITE_REVERB_SCHEME="${REVERB_SCHEME}"
"""
make_vscode_html("vscode_env.html", ".env", code_env, "env")

# 10. VSCode: app/Events/OrderPlaced.php
code_event = """<?php

namespace App\Events;

use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

class OrderPlaced implements ShouldBroadcast
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public $order;
    public $user;

    public function __construct($order, $user)
    {
        $this->order = $order;
        $this->user = $user;
    }

    public function broadcastOn()
    {
        return new PrivateChannel('user.' . $this->user->id);
    }

    public function broadcastAs()
    {
        return 'order.placed';
    }

    public function broadcastWith()
    {
        return [
            'order_id'  => $this->order->id,
            'total'     => $this->order->total ?? 50000,
            'user_name' => $this->user->name,
        ];
    }
}"""
make_vscode_html("vscode_order_placed_event.html", "app/Events/OrderPlaced.php", code_event)

# 11. VSCode: resources/js/bootstrap.js
code_bootstrap = """import axios from 'axios';
window.axios = axios;
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

import Echo from 'laravel-echo';
import Pusher from 'pusher-js';

window.Pusher = Pusher;

window.Echo = new Echo({
    broadcaster: 'reverb',
    key: import.meta.env.VITE_REVERB_APP_KEY || 'x9a2k8m4yq7p1w5c0v3d',
    wsHost: import.meta.env.VITE_REVERB_HOST || window.location.hostname,
    wsPort: import.meta.env.VITE_REVERB_PORT ?? 8080,
    wssPort: import.meta.env.VITE_REVERB_PORT ?? 8080,
    forceTLS: (import.meta.env.VITE_REVERB_SCHEME ?? 'http') === 'https',
    enabledTransports: ['ws', 'wss'],
});"""
make_vscode_html("vscode_bootstrap_echo.html", "resources/js/bootstrap.js", code_bootstrap, "js")

# 12. VSCode: app/Http/Controllers/OrderController.php
code_controller = """<?php

namespace App\Http\Controllers;

use App\Events\OrderPlaced;
use Illuminate\Http\Request;

class OrderController extends Controller
{
    public function store(Request $request)
    {
        $order = (object) [
            'id' => rand(1000, 9999),
            'total' => 50000,
            'total_amount' => 50000,
        ];

        // Memanggil trigger event OrderPlaced ke antrean Reverb
        event(new OrderPlaced($order, $request->user()));

        return response()->json([
            'message'  => 'Event OrderPlaced berhasil dipicu.',
            'order_id' => $order->id,
            'total'    => $order->total,
        ]);
    }
}"""
make_vscode_html("vscode_order_controller.html", "app/Http/Controllers/OrderController.php", code_controller)

# 13. VSCode: routes/web.php
code_routes = """<?php

use App\Http\Controllers\OrderController;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Broadcast;

// Broadcast Channels & Auth
Broadcast::routes(['middleware' => ['web', 'auth']]);

// Acara 34 - Routes
Route::get('/', function () { return view('welcome'); });
Route::get('/register', function () { return view('auth.register'); });
Route::get('/verify-email', function () { return view('auth.verify-email'); });
Route::get('/login', function () { return view('auth.login'); });
Route::get('/dashboard', function () { return view('dashboard'); })->name('dashboard');

// Trigger Event Broadcasting OrderPlaced
Route::match(['get', 'post'], '/order', [OrderController::class, 'store'])->name('order.store');"""
make_vscode_html("vscode_routes_web.html", "routes/web.php", code_routes)

# 14. VSCode: resources/views/dashboard.blade.php
code_blade = """<!-- Listener Laravel Echo & Trigger Button -->
<button onclick="triggerOrder()" class="btn-primary">
    Tes Notifikasi
</button>

<script>
    // Listen ke Private Channel User
    window.Echo.private('user.{{ auth()->id() }}')
        .listen('.order.placed', (e) => {
            alert(`Order #${e.order_id} telah ditempatkan! Total: Rp ${e.total}`);
            console.log('Order Placed:', e);
        });

    async function triggerOrder() {
        await fetch('/order', {
            method: 'POST',
            headers: {
                'X-CSRF-TOKEN': '{{ csrf_token() }}',
                'Accept': 'application/json'
            }
        });
    }
</script>"""
make_vscode_html("vscode_dashboard_blade.html", "resources/views/dashboard.blade.php", code_blade, "blade")

print("All HTML render templates generated successfully.")
