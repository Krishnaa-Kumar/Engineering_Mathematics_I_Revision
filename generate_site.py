#!/usr/bin/env python3
"""
CalcVault Site Generator
Builds the complete multi-page website from assets/data/units.json
Curated by Krishna Kumar (B.Tech Cybersecurity, CGC CEC Landran)
"""

import json
import os
import html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'assets/data/units.json')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    UNITS = json.load(f)

# Unit icons for cards
UNIT_ICONS = {
    'unit-1': 'sigma',
    'unit-2': 'shapes',
    'unit-3': 'function-square',
    'unit-4': 'layers',
    'unit-5': 'box',
}

def get_header(active_page='', title_prefix=''):
    page_title = f"{title_prefix} | CalcVault — Engineering Mathematics-I" if title_prefix else "CalcVault — Engineering Mathematics-I Revision Portal"
    
    unit_links_dropdown = "".join([
        f'<a href="{u["id"]}.html" class="block px-4 py-2.5 text-xs font-medium text-slate-700 dark:text-slate-200 hover:bg-indigo-50 dark:hover:bg-indigo-950/40 hover:text-indigo-600 dark:hover:text-indigo-400 transition flex items-center justify-between"><span><strong class="font-bold">{u["badge"]}:</strong> {u["title"]}</span><i data-lucide="chevron-right" class="w-3.5 h-3.5 opacity-40"></i></a>'
        for u in UNITS
    ])

    unit_links_mobile = "".join([
        f'<a href="{u["id"]}.html" onclick="toggleMobileMenu(true)" class="flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-medium {"bg-indigo-50 text-indigo-600 dark:bg-indigo-950/60 dark:text-indigo-400 font-semibold" if active_page == u["id"] else "text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800"}"><span class="px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-[10px] font-bold shrink-0">{u["badge"]}</span><span class="truncate">{u["title"]}</span></a>'
        for u in UNITS
    ])

    return f"""<!DOCTYPE html>
<html lang="en" class="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page_title}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
  
  <!-- KaTeX for fast, crisp mathematical typesetting -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <link rel="stylesheet" href="assets/css/style.css" />
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          }},
        }},
      }},
    }};
  </script>
</head>
<body class="bg-slate-50 text-slate-900 dark:bg-slate-950 dark:text-slate-100 font-sans antialiased selection:bg-indigo-500 selection:text-white transition-colors duration-200 min-h-screen flex flex-col">

  <!-- Print Only Header -->
  <div class="print-only-header hidden">
    <div class="flex justify-between items-center border-b-2 border-slate-900 pb-3 mb-4">
      <div>
        <h1 class="text-xl font-extrabold text-slate-900">CalcVault — Engineering Mathematics-I Revision Notes</h1>
        <p class="text-xs text-slate-600">Curated for CGC College of Engineering / IKG-PTU BTAM101-18 Syllabus • Krishna Kumar</p>
      </div>
      <div class="text-right text-xs text-slate-500">
        <p>100% Free & Open Access</p>
        <p>Revision Portal</p>
      </div>
    </div>
  </div>

  <!-- Toast Container -->
  <div id="toast-container" class="fixed bottom-4 right-4 z-[100] flex flex-col gap-2 max-w-sm w-full pointer-events-none px-4 sm:px-0"></div>

  <!-- Mobile Backdrop -->
  <div id="mobile-backdrop" onclick="toggleMobileMenu(true)" class="fixed inset-0 bg-slate-950/60 backdrop-blur-xs z-40 hidden lg:hidden"></div>

  <!-- Mobile Drawer -->
  <div id="mobile-menu" class="fixed top-0 left-0 bottom-0 w-80 max-w-[85vw] bg-white dark:bg-slate-900 z-50 transform -translate-x-full transition-transform duration-200 ease-in-out border-r border-slate-200 dark:border-slate-800 flex flex-col p-5 shadow-2xl lg:hidden">
    <div class="flex items-center justify-between pb-4 border-b border-slate-200 dark:border-slate-800">
      <div class="flex items-center gap-2.5">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-indigo-600 to-cyan-600 flex items-center justify-center text-white shadow-sm">
          <i data-lucide="function-square" class="w-5 h-5"></i>
        </div>
        <div>
          <h2 class="font-extrabold text-sm text-slate-900 dark:text-white">CalcVault M-1</h2>
          <p class="text-[10px] text-slate-500 dark:text-slate-400">Engineering Mathematics-I</p>
        </div>
      </div>
      <button onclick="toggleMobileMenu(true)" class="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 dark:hover:text-slate-200">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>
    </div>

    <div class="py-4 space-y-1">
      <a href="index.html" onclick="toggleMobileMenu(true)" class="flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-semibold {'bg-indigo-50 text-indigo-600 dark:bg-indigo-950/60 dark:text-indigo-400' if active_page == 'home' else 'text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800'}">
        <i data-lucide="home" class="w-4 h-4"></i>
        <span>Home Portal</span>
      </a>
      <a href="formulas.html" onclick="toggleMobileMenu(true)" class="flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-semibold {'bg-indigo-50 text-indigo-600 dark:bg-indigo-950/60 dark:text-indigo-400' if active_page == 'formulas' else 'text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800'}">
        <i data-lucide="calculator" class="w-4 h-4"></i>
        <span>Formula & Theorems Sheet</span>
      </a>
      <a href="questions.html" onclick="toggleMobileMenu(true)" class="flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-semibold {'bg-indigo-50 text-indigo-600 dark:bg-indigo-950/60 dark:text-indigo-400' if active_page == 'questions' else 'text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800'}">
        <i data-lucide="help-circle" class="w-4 h-4"></i>
        <span>Solved Question Bank</span>
      </a>
      <a href="whiteboard.html" onclick="toggleMobileMenu(true)" class="flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-semibold {'bg-indigo-50 text-indigo-600 dark:bg-indigo-950/60 dark:text-indigo-400' if active_page == 'whiteboard' else 'text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800'}">
        <i data-lucide="presentation" class="w-4 h-4"></i>
        <span>Interactive Whiteboard</span>
      </a>
    </div>

    <div class="text-[11px] font-bold text-slate-400 dark:text-slate-500 uppercase tracking-wider px-3 mb-2">Syllabus Units</div>
    <div class="flex-1 overflow-y-auto space-y-1 pr-1">
      {unit_links_mobile}
    </div>

    <div class="pt-4 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between">
      <span class="text-xs text-slate-500">Dark / Light Mode</span>
      <button onclick="toggleTheme()" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
        <i data-lucide="moon" class="w-4 h-4 theme-toggle-icon"></i>
      </button>
    </div>
  </div>

  <!-- Global Navigation Header -->
  <header class="sticky top-0 z-30 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 no-print transition-colors">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      <!-- Left: Logo & Brand -->
      <div class="flex items-center gap-3">
        <button onclick="toggleMobileMenu(false)" class="p-2 -ml-2 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 lg:hidden">
          <i data-lucide="menu" class="w-5 h-5"></i>
        </button>
        <a href="index.html" class="flex items-center gap-2.5 group">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-600 to-cyan-600 flex items-center justify-center text-white shadow-md shadow-indigo-500/20 group-hover:scale-105 transition-transform">
            <i data-lucide="function-square" class="w-6 h-6"></i>
          </div>
          <div>
            <div class="flex items-center gap-1.5">
              <span class="font-extrabold text-base tracking-tight text-slate-900 dark:text-white">CalcVault</span>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 font-bold border border-emerald-500/20">Free</span>
            </div>
            <p class="text-[11px] text-slate-500 dark:text-slate-400 font-medium hidden sm:block">Engineering Mathematics-I</p>
          </div>
        </a>
      </div>

      <!-- Center: Desktop Nav -->
      <nav class="hidden lg:flex items-center gap-1">
        <a href="index.html" class="px-3 py-2 rounded-xl text-xs font-semibold transition {'text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/60' if active_page == 'home' else 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'}">Overview</a>
        
        <!-- Units Dropdown -->
        <div class="relative group">
          <button class="px-3 py-2 rounded-xl text-xs font-semibold flex items-center gap-1 transition {'text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/60' if active_page.startswith('unit-') else 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'}">
            <span>Units & Chapters</span>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 opacity-60 group-hover:rotate-180 transition-transform"></i>
          </button>
          <div class="absolute left-0 mt-1 w-80 bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 py-2 hidden group-hover:block transition-all z-50">
            {unit_links_dropdown}
          </div>
        </div>

        <a href="formulas.html" class="px-3 py-2 rounded-xl text-xs font-semibold transition {'text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/60' if active_page == 'formulas' else 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'}">Formula Sheet</a>
        <a href="questions.html" class="px-3 py-2 rounded-xl text-xs font-semibold transition {'text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/60' if active_page == 'questions' else 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'}">Question Bank</a>
        <a href="whiteboard.html" class="px-3 py-2 rounded-xl text-xs font-semibold transition {'text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/60' if active_page == 'whiteboard' else 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'}">Whiteboard</a>
      </nav>

      <!-- Right: Action Tools -->
      <div class="flex items-center gap-2">
        <!-- Search Trigger -->
        <button onclick="openSearchModal()" class="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800/80 hover:bg-slate-200 dark:hover:bg-slate-800 text-slate-500 dark:text-slate-400 text-xs font-medium border border-slate-200 dark:border-slate-700/60 transition shadow-xs">
          <i data-lucide="search" class="w-3.5 h-3.5"></i>
          <span class="hidden md:inline">Quick Search...</span>
          <kbd class="hidden md:inline-block px-1.5 py-0.5 rounded bg-white dark:bg-slate-700 text-[10px] font-mono text-slate-400 dark:text-slate-300 border border-slate-200 dark:border-slate-600">Ctrl K</kbd>
        </button>

        <!-- Theme Toggle -->
        <button onclick="toggleTheme()" title="Toggle dark/light mode" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition">
          <i data-lucide="moon" class="w-4 h-4 theme-toggle-icon"></i>
        </button>

        <!-- Print Action -->
        <button onclick="window.print()" title="Print this page (A4 PDF)" class="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-sm transition">
          <i data-lucide="printer" class="w-3.5 h-3.5"></i>
          <span>Print / PDF</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Global Search Modal -->
  <div id="search-modal" class="fixed inset-0 z-50 hidden items-start justify-center pt-16 sm:pt-24 bg-slate-950/70 backdrop-blur-xs p-4 overflow-y-auto no-print" onclick="closeSearchModal()">
    <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl max-w-2xl w-full shadow-2xl overflow-hidden" onclick="event.stopPropagation()">
      <div class="p-4 border-b border-slate-200 dark:border-slate-800 flex items-center gap-3">
        <i data-lucide="search" class="w-5 h-5 text-indigo-500"></i>
        <input id="search-input" oninput="handleSearchInput(this.value)" type="text" placeholder="Search topics, formulas, or derivations (e.g. Ratio, Raabe, Cardioid, Beta-Gamma, Euler, Maxima, Jacobian)..." class="w-full bg-transparent text-sm text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-hidden" />
        <button onclick="closeSearchModal()" class="text-xs px-2 py-1 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-500 hover:text-slate-800 dark:hover:text-slate-200">ESC</button>
      </div>
      <div id="search-results" class="max-h-[60vh] overflow-y-auto p-3 space-y-1 divide-y divide-slate-100 dark:divide-slate-800/40">
        <!-- Live search results inject here -->
      </div>
    </div>
  </div>
"""

def get_footer():
    return """
  <!-- Global Footer -->
  <footer class="mt-auto bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 py-10 no-print transition-colors">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
        <!-- Brand Info -->
        <div class="md:col-span-2">
          <div class="flex items-center gap-2.5 mb-3">
            <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-600 to-cyan-600 flex items-center justify-center text-white">
              <i data-lucide="function-square" class="w-4 h-4"></i>
            </div>
            <span class="font-extrabold text-base tracking-tight text-slate-900 dark:text-white">CalcVault M-1</span>
            <span class="text-[10px] px-2 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 font-bold">100% Free Access</span>
          </div>
          <p class="text-xs text-slate-500 dark:text-slate-400 leading-relaxed max-w-md">
            CalcVault M-1 is a free, open-access engineering mathematics revision portal curated for CGC College of Engineering / IKG-PTU students. Complete syllabus notes, derivations, formulas, and verified exam solutions without any paywalls.
          </p>
          <div class="mt-4 flex items-center gap-2 text-xs text-slate-400 dark:text-slate-500">
            <i data-lucide="check-circle" class="w-4 h-4 text-emerald-500"></i>
            <span>Curated by Krishna Kumar (B.Tech Cybersecurity, CGC CEC Landran) • Free Academic Project</span>
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-slate-900 dark:text-slate-200 mb-3">Syllabus Units</h4>
          <ul class="space-y-1.5 text-xs text-slate-500 dark:text-slate-400">
            <li><a href="unit-1.html" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition">Unit 1: Sequences & Series</a></li>
            <li><a href="unit-2.html" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition">Unit 2: Definite Integral Applications</a></li>
            <li><a href="unit-3.html" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition">Unit 3: Beta & Gamma Functions</a></li>
            <li><a href="unit-4.html" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition">Unit 4: Multivariable Calculus</a></li>
            <li><a href="unit-5.html" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition">Unit 5: Multiple Integrals</a></li>
          </ul>
        </div>

        <!-- Resources & Tools -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-slate-900 dark:text-slate-200 mb-3">Study Resources</h4>
          <ul class="space-y-1.5 text-xs text-slate-500 dark:text-slate-400">
            <li><a href="formulas.html" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition">Formula & Theorems Sheet</a></li>
            <li><a href="questions.html" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition">Solved Exam Question Bank</a></li>
            <li><a href="whiteboard.html" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition">Interactive Whiteboard Solver</a></li>
            <li><button onclick="window.print()" class="text-left hover:text-indigo-600 dark:hover:text-indigo-400 transition">Print Current Notes (PDF)</button></li>
            <li><button onclick="openSearchModal()" class="text-left hover:text-indigo-600 dark:hover:text-indigo-400 transition">Search All Topics (Ctrl+K)</button></li>
          </ul>
        </div>
      </div>

      <div class="pt-6 border-t border-slate-100 dark:border-slate-800/80 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400">
        <p>© 2026 CalcVault Study Portal • IKG-PTU BTAM101-18. Built for engineering excellence.</p>
        <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="flex items-center gap-1 hover:text-indigo-500 transition">
          <span>Back to top</span>
          <i data-lucide="arrow-up" class="w-3.5 h-3.5"></i>
        </button>
      </div>
    </div>
  </footer>

  <script src="assets/js/main.js"></script>
</body>
</html>
"""

# ==============================================================================
# 1. BUILD HOME PAGE (index.html)
# ==============================================================================
def build_home_page():
    unit_cards = []
    for u in UNITS:
        icon_name = UNIT_ICONS.get(u['id'], 'function-square')
        sec_count = len(u.get('sections', []))
        q_count = len(u.get('questions', []))
        read_time = u.get('readTime', '20 min read')
        
        # Extract preview bullets
        preview_topics = "".join([
            f'<li class="flex items-start gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-indigo-500 shrink-0 mt-0.5"></i><span class="line-clamp-1">{s["heading"]}</span></li>'
            for s in u.get('sections', [])[:3]
        ])

        card_html = f"""
        <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-6 shadow-xs hover:shadow-xl hover:border-indigo-500/40 dark:hover:border-indigo-500/40 transition-all duration-300 flex flex-col justify-between group">
          <div>
            <div class="flex items-center justify-between gap-2 mb-4">
              <span class="px-2.5 py-1 rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 text-xs font-bold tracking-wider uppercase border border-indigo-100 dark:border-indigo-900/50">{u["badge"]}</span>
              <span class="text-xs text-slate-400 flex items-center gap-1"><i data-lucide="clock" class="w-3.5 h-3.5"></i> {read_time}</span>
            </div>

            <div class="flex items-center gap-3 mb-3">
              <div class="w-10 h-10 rounded-2xl bg-indigo-50 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
                <i data-lucide="{icon_name}" class="w-5 h-5"></i>
              </div>
              <h3 class="font-extrabold text-base sm:text-lg text-slate-900 dark:text-white group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors leading-snug">
                <a href="{u["id"]}.html">{u["title"]}</a>
              </h3>
            </div>

            <p class="text-xs text-slate-500 dark:text-slate-400 mb-4 line-clamp-2 leading-relaxed">{u["subtitle"]}</p>

            <div class="pt-3 border-t border-slate-100 dark:border-slate-800/80 mb-5">
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-2">Key Topics Covered:</span>
              <ul class="text-xs text-slate-600 dark:text-slate-300 space-y-1.5">
                {preview_topics}
              </ul>
            </div>
          </div>

          <div class="pt-4 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between gap-2">
            <span class="text-[11px] font-medium text-slate-400">{sec_count} Topics • {q_count} Solved Q&As</span>
            <div class="flex items-center gap-2">
              <a href="{u["id"]}.html" class="px-3.5 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-xs transition flex items-center gap-1">
                <span>Study Notes</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </a>
            </div>
          </div>
        </div>
        """
        unit_cards.append(card_html)

    content = f"""
  {get_header(active_page='home')}

  <!-- Hero Section -->
  <section class="relative overflow-hidden py-14 sm:py-20 bg-gradient-to-b from-indigo-50/50 via-white to-slate-50 dark:from-slate-900/50 dark:via-slate-950 dark:to-slate-950 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-100/70 dark:bg-indigo-950/70 border border-indigo-200 dark:border-indigo-800 text-indigo-700 dark:text-indigo-300 text-xs font-bold mb-6">
        <i data-lucide="sparkles" class="w-3.5 h-3.5"></i>
        <span>100% Free & Open Academic Portal • CGC / IKG-PTU BTAM101-18 Curriculum</span>
      </div>

      <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black text-slate-900 dark:text-white tracking-tight mb-6 max-w-4xl mx-auto leading-tight">
        Engineering Mathematics-I, <br class="hidden sm:inline" />
        <span class="bg-gradient-to-r from-indigo-600 via-cyan-500 to-violet-600 bg-clip-text text-transparent">Simplified & Mastered.</span>
      </h1>

      <p class="text-sm sm:text-base text-slate-600 dark:text-slate-300 max-w-2xl mx-auto mb-8 leading-relaxed">
        Comprehensive revision notes, step-by-step mathematical proofs with KaTeX, verified university question banks, and rapid formula cheat sheets — all completely free without restrictions.
      </p>

      <!-- Main Action Buttons -->
      <div class="flex flex-wrap items-center justify-center gap-3 sm:gap-4 mb-12">
        <a href="unit-1.html" class="px-5 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-bold shadow-lg shadow-indigo-600/25 transition-all flex items-center gap-2">
          <i data-lucide="book-open" class="w-4 h-4"></i>
          <span>Start Revision (Unit 1)</span>
        </a>
        <a href="formulas.html" class="px-5 py-3 rounded-2xl bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 border border-slate-200 dark:border-slate-700 text-sm font-bold shadow-xs transition flex items-center gap-2">
          <i data-lucide="calculator" class="w-4 h-4 text-indigo-500"></i>
          <span>Formula Cheat Sheet</span>
        </a>
        <a href="questions.html" class="px-5 py-3 rounded-2xl bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-200 border border-slate-200 dark:border-slate-700 text-sm font-bold shadow-xs transition flex items-center gap-2">
          <i data-lucide="help-circle" class="w-4 h-4 text-violet-500"></i>
          <span>Solved Question Bank</span>
        </a>
        <a href="whiteboard.html" class="px-5 py-3 rounded-2xl bg-gradient-to-r from-cyan-600 to-indigo-600 hover:from-cyan-500 hover:to-indigo-500 text-white text-sm font-bold shadow-sm transition flex items-center gap-2">
          <i data-lucide="presentation" class="w-4 h-4"></i>
          <span>Interactive Whiteboard</span>
        </a>
      </div>

      <!-- Live Search Box in Hero -->
      <div class="max-w-xl mx-auto bg-white dark:bg-slate-900 rounded-2xl p-2 border border-slate-200 dark:border-slate-800 shadow-xl flex items-center gap-2 text-left cursor-pointer hover:border-indigo-500 transition" onclick="openSearchModal()">
        <i data-lucide="search" class="w-5 h-5 text-indigo-500 ml-2"></i>
        <span class="text-xs sm:text-sm text-slate-400 flex-1">Search any topic, formula, or exam proof (e.g. Ratio, Cardioid, Beta-Gamma, Euler, Jacobian)...</span>
        <span class="px-2 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-[10px] font-mono text-slate-500">Ctrl K</span>
      </div>

      <!-- Quick Metrics Grid -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-12 max-w-4xl mx-auto text-center">
        <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 p-4 rounded-2xl shadow-xs">
          <div class="text-2xl sm:text-3xl font-extrabold text-indigo-600 dark:text-indigo-400">5</div>
          <div class="text-xs text-slate-500 font-medium mt-1">Syllabus Units</div>
        </div>
        <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 p-4 rounded-2xl shadow-xs">
          <div class="text-2xl sm:text-3xl font-extrabold text-cyan-600 dark:text-cyan-400">20</div>
          <div class="text-xs text-slate-500 font-medium mt-1">Theory Sections</div>
        </div>
        <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 p-4 rounded-2xl shadow-xs">
          <div class="text-2xl sm:text-3xl font-extrabold text-emerald-600 dark:text-emerald-400">26</div>
          <div class="text-xs text-slate-500 font-medium mt-1">Solved Derivations & Q&As</div>
        </div>
        <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 p-4 rounded-2xl shadow-xs">
          <div class="text-2xl sm:text-3xl font-extrabold text-amber-600 dark:text-amber-400">0 ₹</div>
          <div class="text-xs text-slate-500 font-medium mt-1">100% Free Access</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Units Grid Section -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
    <div class="flex flex-col sm:flex-row items-start sm:items-end justify-between gap-4 mb-10">
      <div>
        <div class="flex items-center gap-2 text-indigo-600 dark:text-indigo-400 text-xs font-bold uppercase tracking-wider mb-2">
          <i data-lucide="layers" class="w-4 h-4"></i>
          <span>Curriculum Structure</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white">Explore All 5 Units</h2>
      </div>
      <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 max-w-md">
        Select a unit below to read comprehensive lecture notes, view equations, and study step-by-step solved university questions.
      </p>
    </div>

    <!-- 5 Unit Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {"".join(unit_cards)}
    </div>

    <!-- Quick Tools Banner -->
    <div class="mt-16 bg-gradient-to-br from-indigo-900 via-slate-900 to-slate-950 text-white rounded-3xl p-8 sm:p-12 relative overflow-hidden shadow-2xl">
      <div class="max-w-2xl relative z-10">
        <span class="px-3 py-1 rounded-full bg-indigo-500/20 text-indigo-300 text-xs font-bold border border-indigo-500/30">Essential Exam Preparation</span>
        <h3 class="text-2xl sm:text-3xl font-black mt-4 mb-3">Master Formulas, Derivations &amp; University Questions</h3>
        <p class="text-xs sm:text-sm text-indigo-100/80 leading-relaxed mb-6">
          Access the full mathematical formula sheet with standard test conditions, or practice the 26 recurring university exam questions with step-by-step proofs on the interactive whiteboard.
        </p>
        <div class="flex flex-wrap gap-3">
          <a href="formulas.html" class="px-4 py-2.5 rounded-xl bg-white text-slate-900 font-bold text-xs hover:bg-slate-100 transition shadow-sm">
            Open Formula Sheet
          </a>
          <a href="questions.html" class="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition shadow-sm">
            Browse Question Bank
          </a>
          <a href="whiteboard.html" class="px-4 py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow-sm">
            Interactive Whiteboard
          </a>
          <button onclick="window.print()" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs border border-slate-700 transition flex items-center gap-1.5">
            <i data-lucide="printer" class="w-3.5 h-3.5"></i>
            <span>Print Current Page</span>
          </button>
        </div>
      </div>
      <div class="absolute -right-10 -bottom-10 w-72 h-72 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none"></div>
    </div>
  </main>

  {get_footer()}
    """
    with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated index.html")

# ==============================================================================
# 2. BUILD INDIVIDUAL UNIT PAGES (unit-1.html to unit-5.html)
# ==============================================================================
def build_unit_pages():
    for idx, u in enumerate(UNITS):
        uid = u['id']
        badge = u['badge']
        title = u['title']
        subtitle = u['subtitle']
        read_time = u.get('readTime', '20 min read')
        sections = u.get('sections', [])
        questions = u.get('questions', [])

        # Prev / Next unit
        prev_unit = UNITS[idx - 1] if idx > 0 else None
        next_unit = UNITS[idx + 1] if idx < len(UNITS) - 1 else None

        # Build Section Table of Contents
        toc_items = "".join([
            f'<a href="#sec-{s_idx}" class="px-3 py-1.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-300 hover:text-indigo-600 dark:hover:text-indigo-400 hover:border-indigo-300 dark:hover:border-indigo-700 text-xs font-medium transition shrink-0">{s["heading"].split(":")[0] if ":" in s["heading"] else s["heading"][:32]}...</a>'
            for s_idx, s in enumerate(sections)
        ])

        # Build Theory Sections HTML
        sections_html = []
        for s_idx, s in enumerate(sections):
            bullets_html = ""
            if s.get('bullets'):
                b_items = "".join([
                    f'<li class="flex items-start gap-2.5 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed"><span class="w-1.5 h-1.5 rounded-full bg-indigo-500 shrink-0 mt-2"></span><span>{b}</span></li>'
                    for b in s['bullets']
                ])
                bullets_html = f'<ul class="space-y-2.5 my-4 bg-slate-50/70 dark:bg-slate-950/40 p-4 sm:p-5 rounded-2xl border border-slate-100 dark:border-slate-800/60">{b_items}</ul>'

            formula_html = ""
            if s.get('formula'):
                clean_formula_escaped = html.escape(s['formula'])
                js_escaped_formula = s['formula'].replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')
                formula_html = f"""
                <div class="mt-4 formula-box p-4 rounded-2xl border border-indigo-200 dark:border-indigo-900/40 relative group">
                  <div class="flex items-center justify-between pb-2 mb-2 border-b border-indigo-100 dark:border-indigo-950">
                    <span class="text-[10px] font-bold uppercase tracking-wider text-indigo-600 dark:text-indigo-400 flex items-center gap-1">
                      <i data-lucide="code" class="w-3.5 h-3.5"></i> Key Formula / Derivation Condition
                    </span>
                    <button onclick="copyFormula(`{js_escaped_formula}`, this)" class="text-[11px] px-2.5 py-1 rounded-lg bg-indigo-100/60 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-300 hover:bg-indigo-200 dark:hover:bg-indigo-900 transition flex items-center gap-1 no-print">
                      <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy
                    </button>
                  </div>
                  <pre class="text-xs sm:text-sm text-slate-800 dark:text-slate-200 overflow-x-auto whitespace-pre-wrap leading-relaxed"><code>{clean_formula_escaped}</code></pre>
                </div>
                """

            sec_card = f"""
            <article id="sec-{s_idx}" class="unit-card bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-20">
              <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white mb-3 flex items-center gap-2">
                <span class="w-2 h-6 rounded-full bg-indigo-600 shrink-0"></span>
                <span>{s["heading"]}</span>
              </h3>
              <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">{s["body"]}</p>
              {bullets_html}
              {formula_html}
            </article>
            """
            sections_html.append(sec_card)

        # Build Solved Questions HTML
        questions_html = []
        for q_idx, q in enumerate(questions):
            marks_badge = q.get('marks', '5 Marks')
            q_title = q.get('q', '')
            q_answer = q.get('a', '')

            q_card = f"""
            <details class="qa-card group bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-xs overflow-hidden" {"open" if q_idx == 0 else ""}>
              <summary class="p-4 sm:p-5 cursor-pointer select-none flex items-start justify-between gap-3 hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
                <div class="flex-1">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="px-2 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 text-[10px] font-bold">{marks_badge}</span>
                    <span class="text-[11px] text-slate-400">Exam Question {q_idx + 1}</span>
                  </div>
                  <h4 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-slate-100">{q_title}</h4>
                </div>
                <div class="w-7 h-7 rounded-xl bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-500 shrink-0 mt-0.5 no-print">
                  <i data-lucide="chevron-down" class="w-4 h-4 accordion-chevron transition-transform duration-200"></i>
                </div>
              </summary>
              <div class="qa-answer p-4 sm:p-6 pt-2 border-t border-slate-100 dark:border-slate-800/80 text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed bg-slate-50/40 dark:bg-slate-950/20">
                <div class="font-semibold text-indigo-600 dark:text-indigo-400 text-xs uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> Verified Model Solution &amp; Derivation:
                </div>
                <div>{q_answer}</div>
              </div>
            </details>
            """
            questions_html.append(q_card)

        # Pagination Bar
        prev_btn = f'<a href="{prev_unit["id"]}.html" class="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs font-bold text-slate-700 dark:text-slate-200 hover:border-indigo-500 transition"><i data-lucide="arrow-left" class="w-4 h-4"></i> Previous: {prev_unit["badge"]}</a>' if prev_unit else '<span class="hidden sm:inline"></span>'
        next_btn = f'<a href="{next_unit["id"]}.html" class="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 text-white text-xs font-bold hover:bg-indigo-500 transition shadow-xs">Next: {next_unit["badge"]} <i data-lucide="arrow-right" class="w-4 h-4"></i></a>' if next_unit else f'<a href="formulas.html" class="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 text-white text-xs font-bold hover:bg-indigo-500 transition shadow-xs">Formulas Cheat Sheet <i data-lucide="arrow-right" class="w-4 h-4"></i></a>'

        page_content = f"""
  {get_header(active_page=uid, title_prefix=f"{badge} — {title}")}

  <!-- Unit Hero Header -->
  <section class="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 py-10 transition-colors">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Breadcrumb -->
      <nav class="flex items-center gap-2 text-xs text-slate-500 mb-4 no-print">
        <a href="index.html" class="hover:text-indigo-600 dark:hover:text-indigo-400">Home</a>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
        <span>Syllabus Units</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
        <span class="text-indigo-600 dark:text-indigo-400 font-semibold">{badge}</span>
      </nav>

      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-2 mb-2">
            <span class="px-3 py-1 rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 text-xs font-extrabold uppercase tracking-wider border border-indigo-100 dark:border-indigo-900/50">{badge}</span>
            <span class="text-xs text-slate-400 flex items-center gap-1"><i data-lucide="clock" class="w-3.5 h-3.5"></i> {read_time}</span>
            <span class="px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 text-[10px] font-bold">100% Free</span>
          </div>
          <h1 class="text-2xl sm:text-4xl font-black text-slate-900 dark:text-white leading-tight">{title}</h1>
          <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-2 max-w-2xl">{subtitle}</p>
        </div>

        <div class="flex flex-wrap items-center gap-2 no-print shrink-0">
          <a href="#questions-section" class="px-3.5 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 text-xs font-bold hover:bg-slate-200 dark:hover:bg-slate-700 transition flex items-center gap-1.5">
            <i data-lucide="help-circle" class="w-3.5 h-3.5 text-indigo-500"></i>
            <span>Solved Q&As ({len(questions)})</span>
          </a>
          <a href="formulas.html#{uid}" class="px-3.5 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 text-xs font-bold hover:bg-slate-200 dark:hover:bg-slate-700 transition flex items-center gap-1.5">
            <i data-lucide="calculator" class="w-3.5 h-3.5 text-violet-500"></i>
            <span>Formulas</span>
          </a>
          <a href="whiteboard.html" class="px-3.5 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold shadow-xs transition flex items-center gap-1.5">
            <i data-lucide="presentation" class="w-3.5 h-3.5"></i>
            <span>Whiteboard</span>
          </a>
          <button onclick="window.print()" class="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-xs transition flex items-center gap-1.5">
            <i data-lucide="printer" class="w-3.5 h-3.5"></i>
            <span>Print Unit (PDF)</span>
          </button>
        </div>
      </div>

      <!-- Quick Section Jump Nav -->
      <div class="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800/80 flex items-center gap-2 overflow-x-auto pb-1 no-print">
        <span class="text-[11px] font-bold text-slate-400 shrink-0 uppercase tracking-wider mr-1">Jump to:</span>
        {toc_items}
      </div>
    </div>
  </section>

  <!-- Main Content Body -->
  <main class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10 flex-1 w-full space-y-8">
    <!-- Theory Sections -->
    {"".join(sections_html)}

    <!-- Solved University Questions Section -->
    <section id="questions-section" class="pt-8 border-t-2 border-slate-200 dark:border-slate-800 scroll-mt-20">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-6">
        <div>
          <span class="text-xs font-bold uppercase tracking-wider text-indigo-600 dark:text-indigo-400">Exam Preparation</span>
          <h3 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white">Solved University Exam Questions &amp; Proofs</h3>
          <p class="text-xs text-slate-500 mt-1">High-probability university exam questions with step-by-step model solutions.</p>
        </div>
        <div class="flex items-center gap-2 no-print">
          <button onclick="document.querySelectorAll('#questions-section details').forEach(d => d.open = true)" class="px-3 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-xs font-medium hover:bg-slate-200 dark:hover:bg-slate-700 transition">Expand All</button>
          <button onclick="document.querySelectorAll('#questions-section details').forEach(d => d.open = false)" class="px-3 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-xs font-medium hover:bg-slate-200 dark:hover:bg-slate-700 transition">Collapse All</button>
        </div>
      </div>

      <div class="space-y-4">
        {"".join(questions_html)}
      </div>
    </section>

    <!-- Bottom Unit Navigation Pagination -->
    <div class="pt-8 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-4 no-print">
      {prev_btn}
      <button onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" class="text-xs text-slate-500 hover:text-indigo-500 flex items-center gap-1 font-medium">
        <i data-lucide="arrow-up" class="w-3.5 h-3.5"></i> Back to Top
      </button>
      {next_btn}
    </div>
  </main>

  {get_footer()}
        """
        with open(os.path.join(BASE_DIR, f"{uid}.html"), 'w', encoding='utf-8') as f:
            f.write(page_content)
        print(f"Generated {uid}.html")

# ==============================================================================
# 3. BUILD FORMULAS CHEAT SHEET (formulas.html)
# ==============================================================================
def build_formulas_page():
    unit_formula_cards = []
    for u in UNITS:
        formulas_in_unit = []
        for s in u.get('sections', []):
            if s.get('formula'):
                formulas_in_unit.append({
                    'heading': s['heading'],
                    'formula': s['formula']
                })
        
        cards = []
        for f in formulas_in_unit:
            clean_formula_escaped = html.escape(f['formula'])
            js_escaped_formula = f['formula'].replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')
            cards.append(f"""
            <div class="formula-box p-4 rounded-2xl border border-indigo-200 dark:border-indigo-900/40 relative">
              <div class="flex items-center justify-between pb-2 mb-2 border-b border-indigo-100 dark:border-indigo-950">
                <span class="text-xs font-bold text-slate-800 dark:text-slate-200">{f["heading"]}</span>
                <button onclick="copyFormula(`{js_escaped_formula}`, this)" class="text-[11px] px-2.5 py-1 rounded-lg bg-indigo-100/60 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-300 hover:bg-indigo-200 dark:hover:bg-indigo-900 transition flex items-center gap-1 no-print">
                  <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy
                </button>
              </div>
              <pre class="text-xs sm:text-sm text-slate-800 dark:text-slate-200 overflow-x-auto whitespace-pre-wrap leading-relaxed"><code>{clean_formula_escaped}</code></pre>
            </div>
            """)

        unit_section = f"""
        <section id="{u["id"]}" class="unit-card bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-20">
          <div class="flex items-center justify-between gap-3 mb-4 pb-3 border-b border-slate-100 dark:border-slate-800">
            <div>
              <span class="px-2.5 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 text-xs font-bold uppercase tracking-wider">{u["badge"]}</span>
              <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white mt-1">{u["title"]}</h3>
            </div>
            <a href="{u["id"]}.html" class="text-xs font-semibold text-indigo-600 dark:text-indigo-400 hover:underline flex items-center gap-1 no-print">
              <span>View Full Unit</span>
              <i data-lucide="external-link" class="w-3 h-3"></i>
            </a>
          </div>
          <div class="space-y-4">
            {"".join(cards)}
          </div>
        </section>
        """
        unit_formula_cards.append(unit_section)

    content = f"""
  {get_header(active_page='formulas', title_prefix='Formula & Constant Cheat Sheet')}

  <!-- Hero Header -->
  <section class="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 py-10 transition-colors">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <span class="px-3 py-1 rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 text-xs font-extrabold uppercase tracking-wider">Quick Reference</span>
          <h1 class="text-2xl sm:text-4xl font-black text-slate-900 dark:text-white mt-2 leading-tight">Formula &amp; Theorems Cheat Sheet</h1>
          <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1 max-w-xl">
            All essential convergence test criteria, arc length and volume expressions, Beta-Gamma identities, Euler's theorem deductions, and multiple integrals formulas.
          </p>
        </div>
        <div class="flex items-center gap-2 no-print shrink-0">
          <button onclick="window.print()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-xs transition flex items-center gap-1.5">
            <i data-lucide="printer" class="w-3.5 h-3.5"></i>
            <span>Print Formula Sheet</span>
          </button>
        </div>
      </div>

      <!-- Quick Jump Links to Units -->
      <div class="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800/80 flex items-center gap-2 overflow-x-auto pb-1 no-print">
        <span class="text-[11px] font-bold text-slate-400 shrink-0 uppercase tracking-wider mr-1">Units:</span>
        <a href="#constants" class="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:text-indigo-600 text-xs font-semibold">Standard Invariants</a>
        {"".join([f'<a href="#{u["id"]}" class="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:text-indigo-600 text-xs font-semibold shrink-0">{u["badge"]}</a>' for u in UNITS])}
      </div>
    </div>
  </section>

  <main class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10 flex-1 w-full space-y-8">
    <!-- Standard Invariants Reference Table -->
    <section id="constants" class="unit-card bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-6 sm:p-8 shadow-xs scroll-mt-20">
      <div class="flex items-center justify-between gap-3 mb-4 pb-3 border-b border-slate-100 dark:border-slate-800">
        <div>
          <span class="px-2.5 py-0.5 rounded-full bg-violet-50 dark:bg-violet-950/60 text-violet-600 dark:text-violet-400 text-xs font-bold uppercase tracking-wider">Exam Standards</span>
          <h3 class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white mt-1">Frequently Examined Standard Results</h3>
        </div>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs sm:text-sm">
          <thead class="bg-slate-50 dark:bg-slate-800/50 text-slate-500 dark:text-slate-400 border-b border-slate-200 dark:border-slate-800">
            <tr>
              <th class="p-3 font-semibold">Theorem / Invariant</th>
              <th class="p-3 font-semibold">Mathematical Result</th>
              <th class="p-3 font-semibold">Conditions &amp; PTU Evaluator Notes</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 dark:divide-slate-800">
            <tr>
              <td class="p-3 font-medium text-slate-900 dark:text-white">p-Series Criterion</td>
              <td class="p-3 font-mono font-bold text-indigo-600 dark:text-indigo-400">sum (1 / n^p)</td>
              <td class="p-3 text-slate-500">Converges if p > 1, Diverges if p &le; 1</td>
            </tr>
            <tr>
              <td class="p-3 font-medium text-slate-900 dark:text-white">Gamma Half-Integer</td>
              <td class="p-3 font-mono font-bold text-indigo-600 dark:text-indigo-400">Gamma(1/2) = sqrt(pi)</td>
              <td class="p-3 text-slate-500">Proven using transformation x = y^2 and double integrals in polar coordinates</td>
            </tr>
            <tr>
              <td class="p-3 font-medium text-slate-900 dark:text-white">Cardioid Perimeter</td>
              <td class="p-3 font-mono font-bold text-indigo-600 dark:text-indigo-400">Perimeter = 8a</td>
              <td class="p-3 text-slate-500">For r = a(1 + cos theta), integrate from 0 to pi and multiply by 2 (symmetry)</td>
            </tr>
            <tr>
              <td class="p-3 font-medium text-slate-900 dark:text-white">Cycloid Arc Length</td>
              <td class="p-3 font-mono font-bold text-indigo-600 dark:text-indigo-400">Arch Length = 8a</td>
              <td class="p-3 text-slate-500">Parametric range theta in [0, 2*pi] for one complete revolution arch</td>
            </tr>
            <tr>
              <td class="p-3 font-medium text-slate-900 dark:text-white">Euler's 2nd Deduction</td>
              <td class="p-3 font-mono font-bold text-indigo-600 dark:text-indigo-400">x^2*u_xx + 2xy*u_xy + y^2*u_yy</td>
              <td class="p-3 text-slate-500">Equals F(u) * [F'(u) - 1], where F(u) = n * f(u) / f'(u)</td>
            </tr>
            <tr>
              <td class="p-3 font-medium text-slate-900 dark:text-white">Polar Jacobian</td>
              <td class="p-3 font-mono font-bold text-indigo-600 dark:text-indigo-400">dx dy = r dr dtheta</td>
              <td class="p-3 text-slate-500">Derived from determinant of partial derivatives d(x,y)/d(r,theta) = r</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- Formula Sections for each unit -->
    {"".join(unit_formula_cards)}
  </main>

  {get_footer()}
    """
    with open(os.path.join(BASE_DIR, 'formulas.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated formulas.html")

# ==============================================================================
# 4. BUILD SOLVED QUESTION BANK (questions.html)
# ==============================================================================
def build_questions_page():
    all_questions = []
    for u in UNITS:
        for q_idx, q in enumerate(u.get('questions', [])):
            all_questions.append({
                'unit_id': u['id'],
                'unit_badge': u['badge'],
                'unit_title': u['title'],
                'marks': q.get('marks', '5 Marks'),
                'q': q.get('q', ''),
                'a': q.get('a', '')
            })

    questions_cards = []
    for idx, q in enumerate(all_questions):
        card = f"""
        <article class="question-item qa-card bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-6 shadow-xs" data-unit="{q["unit_id"]}" data-marks="{q["marks"]}">
          <div class="flex items-center justify-between gap-2 mb-3">
            <div class="flex items-center gap-2">
              <a href="{q["unit_id"]}.html" class="px-2.5 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 text-xs font-bold hover:underline">{q["unit_badge"]}</a>
              <span class="text-xs text-slate-400 font-medium">• {q["unit_title"].split("&")[0]}</span>
            </div>
            <span class="px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-bold">{q["marks"]}</span>
          </div>

          <h3 class="text-sm sm:text-base font-extrabold text-slate-900 dark:text-white mb-3 leading-snug">{q["q"]}</h3>

          <details class="group mt-2">
            <summary class="inline-flex items-center gap-2 px-3 py-1.5 rounded-xl bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 text-xs font-bold cursor-pointer hover:bg-indigo-100 dark:hover:bg-indigo-900 transition select-none no-print">
              <i data-lucide="eye" class="w-3.5 h-3.5"></i>
              <span class="view-answer-text">View Model Solution &amp; Steps</span>
            </summary>
            <div class="qa-answer mt-3 pt-3 border-t border-slate-100 dark:border-slate-800 text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed bg-slate-50/60 dark:bg-slate-950/40 p-4 sm:p-5 rounded-2xl">
              <div class="font-bold text-emerald-600 dark:text-emerald-400 text-xs uppercase tracking-wider mb-2 flex items-center gap-1.5">
                <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> Verified Exam Derivation:
              </div>
              <div>{q["a"]}</div>
            </div>
          </details>
        </article>
        """
        questions_cards.append(card)

    content = f"""
  {get_header(active_page='questions', title_prefix='Solved Exam Question Bank')}

  <!-- Hero Header -->
  <section class="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 py-10 transition-colors">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-2 mb-2">
            <span class="px-3 py-1 rounded-full bg-violet-50 dark:bg-violet-950/60 text-violet-600 dark:text-violet-400 text-xs font-extrabold uppercase tracking-wider">Exam Repository</span>
            <span class="text-xs text-slate-400 font-semibold">{len(all_questions)} Solved Questions &amp; Proofs</span>
          </div>
          <h1 class="text-2xl sm:text-4xl font-black text-slate-900 dark:text-white leading-tight">Comprehensive Solved Question Bank</h1>
          <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1 max-w-xl">
            Frequently asked university exam questions, 2-mark definitions, 5-mark applications, and 10-mark full mathematical proofs with model answers.
          </p>
        </div>
        <div class="flex items-center gap-2 no-print shrink-0">
          <button onclick="window.print()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-xs transition flex items-center gap-1.5">
            <i data-lucide="printer" class="w-3.5 h-3.5"></i>
            <span>Print Questions (PDF)</span>
          </button>
        </div>
      </div>

      <!-- Live Search & Filter Bar -->
      <div class="mt-6 pt-6 border-t border-slate-100 dark:border-slate-800 space-y-4 no-print">
        <!-- Search Input -->
        <div class="relative">
          <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3.5 top-3"></i>
          <input id="qbank-search" oninput="filterQuestions()" type="text" placeholder="Filter questions by keyword (e.g. Raabe, Cardioid, Astroid, Beta-Gamma, Euler, Maxima, Jacobian)..." class="w-full pl-10 pr-4 py-2 rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs sm:text-sm focus:outline-hidden focus:border-indigo-500 text-slate-900 dark:text-slate-100 placeholder-slate-400" />
        </div>

        <!-- Filter Controls -->
        <div class="flex flex-wrap items-center justify-between gap-3">
          <div class="flex flex-wrap items-center gap-1.5" id="unit-filter-group">
            <button onclick="setUnitFilter('all', this)" class="unit-filter-btn px-3 py-1 rounded-xl text-xs font-bold bg-indigo-600 text-white shadow-xs">All Units</button>
            {"".join([f'<button onclick="setUnitFilter(\'{u["id"]}\', this)" class="unit-filter-btn px-3 py-1 rounded-xl text-xs font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition">{u["badge"]}</button>' for u in UNITS])}
          </div>

          <div class="flex items-center gap-2">
            <button onclick="document.querySelectorAll('.question-item details').forEach(d => d.open = true)" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-xs font-medium hover:bg-slate-200">Expand All</button>
            <button onclick="document.querySelectorAll('.question-item details').forEach(d => d.open = false)" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-xs font-medium hover:bg-slate-200">Collapse All</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <main class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10 flex-1 w-full">
    <div id="questions-list" class="space-y-4">
      {"".join(questions_cards)}
    </div>
    <div id="no-questions-msg" class="hidden text-center py-16 text-slate-400">
      <i data-lucide="help-circle" class="w-10 h-10 mx-auto mb-2 opacity-40"></i>
      <p class="text-sm font-semibold">No questions matched your search query.</p>
      <p class="text-xs text-slate-500 mt-1">Try another keyword or select "All Units".</p>
    </div>
  </main>

  <script>
    let activeUnitFilter = 'all';

    function setUnitFilter(unitId, btn) {{
      activeUnitFilter = unitId;
      document.querySelectorAll('.unit-filter-btn').forEach(b => {{
        b.classList.remove('bg-indigo-600', 'text-white', 'shadow-xs');
        b.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300');
      }});
      btn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300');
      btn.classList.add('bg-indigo-600', 'text-white', 'shadow-xs');
      filterQuestions();
    }}

    function filterQuestions() {{
      const query = (document.getElementById('qbank-search')?.value || '').trim().toLowerCase();
      const items = document.querySelectorAll('.question-item');
      let visibleCount = 0;

      items.forEach(item => {{
        const unit = item.getAttribute('data-unit');
        const text = item.textContent.toLowerCase();

        const matchesUnit = activeUnitFilter === 'all' || unit === activeUnitFilter;
        const matchesQuery = !query || text.includes(query);

        if (matchesUnit && matchesQuery) {{
          item.classList.remove('hidden');
          visibleCount++;
        }} else {{
          item.classList.add('hidden');
        }}
      }});

      const noMsg = document.getElementById('no-questions-msg');
      if (noMsg) {{
        noMsg.classList.toggle('hidden', visibleCount > 0);
      }}
    }}
  </script>

  {get_footer()}
    """
    with open(os.path.join(BASE_DIR, 'questions.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated questions.html")

# ==============================================================================
# 5. BUILD INTERACTIVE WHITEBOARD (whiteboard.html)
# ==============================================================================
def build_whiteboard_page():
    content = f"""
  {get_header(active_page='whiteboard', title_prefix='Interactive Whiteboard Solver')}

  <!-- Hero Header -->
  <section class="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 py-6 transition-colors no-print">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <span class="px-3 py-1 rounded-full bg-cyan-50 dark:bg-cyan-950/60 text-cyan-600 dark:text-cyan-400 text-xs font-extrabold uppercase tracking-wider">Step-by-Step Solver</span>
          <h1 class="text-xl sm:text-3xl font-black text-slate-900 dark:text-white mt-1 leading-tight">Interactive Derivation Whiteboard</h1>
          <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-0.5">
            Reveal mathematical solutions step-by-step, review exam evaluator tips, and track your revision mastery.
          </p>
        </div>
        <div class="flex items-center gap-2 shrink-0">
          <a href="questions.html" class="px-3.5 py-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 text-xs font-bold hover:bg-slate-200 dark:hover:bg-slate-700 transition flex items-center gap-1.5">
            <i data-lucide="help-circle" class="w-3.5 h-3.5 text-indigo-500"></i>
            <span>Question Bank</span>
          </a>
          <button onclick="window.print()" class="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-xs transition flex items-center gap-1.5">
            <i data-lucide="printer" class="w-3.5 h-3.5"></i>
            <span>Print Note (PDF)</span>
          </button>
        </div>
      </div>

      <!-- Unit Filter Tabs -->
      <div class="mt-5 flex items-center gap-2 overflow-x-auto pb-1" id="unit-tabs">
        <!-- Injected dynamically via whiteboard script -->
      </div>
    </div>
  </section>

  <!-- Main Whiteboard Workspace -->
  <main class="max-w-7xl w-full mx-auto p-4 grid grid-cols-1 lg:grid-cols-12 gap-5 flex-1">

    <!-- Left Sidebar: Question Selector -->
    <aside class="lg:col-span-4 flex flex-col gap-3 no-print">
      <div class="flex items-center justify-between px-1">
        <span class="text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400" id="question-count-label">
          26 Topics Available
        </span>
        <span class="text-xs font-bold text-cyan-600 dark:text-cyan-400 bg-cyan-500/10 px-2.5 py-0.5 rounded-full border border-cyan-500/20" id="progress-badge">
          0 / 26 Mastered
        </span>
      </div>

      <!-- Search Input -->
      <div class="relative">
        <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
        <input type="text" id="search-input" placeholder="Search 26 topics (e.g., Raabe, Cardioid, Jacobian)..."
               oninput="renderQuestionList()"
               class="w-full pl-9 pr-3 py-2 text-sm rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 focus:outline-hidden focus:border-cyan-500" />
      </div>

      <!-- Question Cards Container -->
      <div id="question-list" class="flex flex-col gap-2 max-h-[calc(100vh-270px)] overflow-y-auto pr-1">
        <!-- Injected dynamically -->
      </div>
    </aside>

    <!-- Right Main Panel: Lecture Whiteboard -->
    <section class="lg:col-span-8 flex flex-col bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm overflow-hidden">

      <!-- Slide Header -->
      <div class="p-4 sm:p-6 border-b border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-950/50">
        <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
          <div class="flex items-center gap-2">
            <span id="slide-unit-badge" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-cyan-600 text-white">UNIT 1</span>
            <span id="slide-marks-badge" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-amber-500/20 text-amber-800 dark:text-amber-300 border border-amber-500/30">10 Marks</span>
          </div>
          <button type="button" onclick="toggleMastered()" id="mastered-btn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold border border-slate-300 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 transition">
            <i data-lucide="check-circle-2" class="w-4 h-4"></i>
            <span>Mark as Mastered</span>
          </button>
        </div>

        <h2 id="slide-title" class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white leading-snug">
          Select a topic to begin
        </h2>
        <div id="slide-problem" class="mt-3 p-3.5 rounded-xl bg-white dark:bg-slate-950 border border-slate-200 dark:border-slate-800 text-xs sm:text-sm font-medium">
          <!-- Problem statement rendered here -->
        </div>
      </div>

      <!-- Exam Intuition & Trap Callout -->
      <div id="intuition-box" class="mx-4 sm:mx-6 mt-4 p-3.5 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-start gap-3">
        <i data-lucide="lightbulb" class="w-5 h-5 text-amber-500 shrink-0 mt-0.5"></i>
        <div class="text-xs sm:text-sm text-amber-950 dark:text-amber-200">
          <span class="font-bold block mb-0.5 text-amber-700 dark:text-amber-400">PTU Evaluator Tip &amp; Exam Trap:</span>
          <span id="intuition-text">Loading tip...</span>
        </div>
      </div>

      <!-- Step-by-Step Whiteboard Area -->
      <div class="flex-1 p-4 sm:p-6 overflow-y-auto space-y-3 min-h-[300px]" id="steps-container">
        <!-- Steps revealed here -->
      </div>

      <!-- Whiteboard Interactive Controls Footer -->
      <div class="p-4 border-t border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950/60 flex flex-wrap items-center justify-between gap-3 no-print">
        <div class="flex items-center gap-2">
          <button type="button" onclick="prevQuestion()" class="p-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700 transition" title="Previous Topic">
            <i data-lucide="chevron-left" class="w-4 h-4"></i>
          </button>
          <button type="button" onclick="nextQuestion()" class="p-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700 transition" title="Next Topic">
            <i data-lucide="chevron-right" class="w-4 h-4"></i>
          </button>
          <span id="step-counter" class="text-xs font-semibold text-slate-500 dark:text-slate-400 ml-1">
            Step 0 of 0
          </span>
        </div>

        <div class="flex items-center gap-2">
          <button type="button" onclick="resetSteps()" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-200 dark:bg-slate-800 hover:bg-slate-300 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 transition">
            Reset Board
          </button>
          <button type="button" onclick="revealAllSteps()" id="reveal-all-btn" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-cyan-500/15 hover:bg-cyan-500/25 text-cyan-700 dark:text-cyan-300 border border-cyan-500/30 transition">
            Reveal All
          </button>
          <button type="button" onclick="revealNextStep()" id="next-step-btn" class="flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-cyan-600 hover:bg-cyan-500 text-white shadow-md shadow-cyan-500/25 transition active:scale-95">
            <span>Next Step</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
        </div>
      </div>
    </section>
  </main>

  <script src="assets/js/data.js"></script>
  <script src="assets/js/whiteboard.js"></script>
  {get_footer()}
    """
    with open(os.path.join(BASE_DIR, 'whiteboard.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated whiteboard.html")

if __name__ == '__main__':
    build_home_page()
    build_unit_pages()
    build_formulas_page()
    build_questions_page()
    build_whiteboard_page()
    print("All CalcVault M-1 pages generated successfully!")
