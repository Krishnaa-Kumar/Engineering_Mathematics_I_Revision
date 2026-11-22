/**
 * CalcVault — Engineering Mathematics-I Study Portal
 * Global Interactive JS (Theme, Navigation, Global Search, Print, Toast Utilities)
 * Curated by Krishna Kumar (B.Tech Cybersecurity, CGC CEC Landran)
 */

// Initialize Theme
(function initTheme() {
  const savedTheme = localStorage.getItem('calcvault_theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
})();

function toggleTheme() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('calcvault_theme', isDark ? 'dark' : 'light');
  updateThemeIcons();
}

function updateThemeIcons() {
  const isDark = document.documentElement.classList.contains('dark');
  document.querySelectorAll('.theme-toggle-icon').forEach(icon => {
    if (isDark) {
      icon.setAttribute('data-lucide', 'sun');
    } else {
      icon.setAttribute('data-lucide', 'moon');
    }
  });
  if (window.lucide) {
    lucide.createIcons();
  }
}

// Mobile Menu Drawer
function toggleMobileMenu(forceState) {
  const menu = document.getElementById('mobile-menu');
  const backdrop = document.getElementById('mobile-backdrop');
  if (!menu) return;

  const isOpen = forceState !== undefined ? forceState : menu.classList.contains('translate-x-0');
  if (isOpen) {
    menu.classList.remove('translate-x-0');
    menu.classList.add('-translate-x-full');
    backdrop?.classList.add('hidden');
  } else {
    menu.classList.remove('-translate-x-full');
    menu.classList.add('translate-x-0');
    backdrop?.classList.remove('hidden');
  }
}

// Global Search Engine
let searchUnitsCache = null;

async function loadSearchData() {
  if (searchUnitsCache) return searchUnitsCache;
  try {
    const res = await fetch('assets/data/units.json');
    if (res.ok) {
      searchUnitsCache = await res.json();
      return searchUnitsCache;
    }
  } catch (e) {
    console.error('Failed to load search data:', e);
  }
  return [];
}

function openSearchModal() {
  const modal = document.getElementById('search-modal');
  if (!modal) return;
  modal.classList.remove('hidden');
  modal.classList.add('flex');
  loadSearchData();
  const input = document.getElementById('search-input');
  if (input) {
    input.value = '';
    setTimeout(() => input.focus(), 50);
    renderSearchResults('');
  }
}

function closeSearchModal() {
  const modal = document.getElementById('search-modal');
  if (!modal) return;
  modal.classList.add('hidden');
  modal.classList.remove('flex');
}

async function handleSearchInput(query) {
  renderSearchResults(query.trim().toLowerCase());
}

async function renderSearchResults(query) {
  const resultsContainer = document.getElementById('search-results');
  if (!resultsContainer) return;

  if (!query) {
    resultsContainer.innerHTML = `
      <div class="p-8 text-center text-slate-400 dark:text-slate-500">
        <i data-lucide="search" class="w-8 h-8 mx-auto mb-2 opacity-50"></i>
        <p class="text-xs">Type a topic, theorem, or formula (e.g. <em>Ratio Test, Cardioid, Beta-Gamma, Euler, Jacobian, Maxima</em>)...</p>
      </div>
    `;
    if (window.lucide) lucide.createIcons();
    return;
  }

  const units = await loadSearchData();
  const results = [];

  units.forEach(unit => {
    // Check unit title & subtitle
    if (unit.title.toLowerCase().includes(query) || unit.subtitle.toLowerCase().includes(query)) {
      results.push({
        type: 'Unit Overview',
        badge: unit.badge,
        title: unit.title,
        url: `${unit.id}.html`,
        snippet: unit.subtitle
      });
    }

    // Check sections
    unit.sections.forEach(sec => {
      const headingMatch = sec.heading.toLowerCase().includes(query);
      const bodyMatch = sec.body.toLowerCase().includes(query);
      const formulaMatch = sec.formula && sec.formula.toLowerCase().includes(query);
      if (headingMatch || bodyMatch || formulaMatch) {
        results.push({
          type: 'Topic Section',
          badge: unit.badge,
          title: sec.heading,
          url: `${unit.id}.html#${encodeURIComponent(sec.heading)}`,
          snippet: formulaMatch ? `Formula: ${sec.formula.substring(0, 110)}...` : sec.body.replace(/<[^>]*>/g, '').substring(0, 110) + '...'
        });
      }
    });

    // Check questions
    unit.questions.forEach(q => {
      const qMatch = q.q.toLowerCase().includes(query);
      const aMatch = q.a.toLowerCase().includes(query);
      if (qMatch || aMatch) {
        results.push({
          type: 'Exam Derivation',
          badge: `${unit.badge} • ${q.marks}`,
          title: q.q,
          url: `questions.html?q=${encodeURIComponent(query)}#${unit.id}`,
          snippet: q.a.replace(/<[^>]*>/g, '').substring(0, 110) + '...'
        });
      }
    });
  });

  if (results.length === 0) {
    resultsContainer.innerHTML = `
      <div class="p-8 text-center text-slate-500">
        <p class="text-sm font-medium">No results found for "${query}"</p>
        <p class="text-xs text-slate-400 mt-1">Try searching for keywords like "Ratio", "Cycloid", "Euler", "Beta", "Jacobian".</p>
      </div>
    `;
    return;
  }

  resultsContainer.innerHTML = results.slice(0, 12).map(r => `
    <a href="${r.url}" class="block p-3 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 border border-transparent hover:border-slate-200 dark:hover:border-slate-700 transition">
      <div class="flex items-center justify-between gap-2 mb-1">
        <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 uppercase tracking-wider">${r.badge}</span>
        <span class="text-[11px] text-slate-400">${r.type}</span>
      </div>
      <h4 class="text-sm font-semibold text-slate-800 dark:text-slate-200">${r.title}</h4>
      <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 line-clamp-2">${r.snippet}</p>
    </a>
  `).join('');

  if (window.lucide) lucide.createIcons();
  renderMath(resultsContainer);
}

// Copy Formula utility
function copyFormula(text, btnElement) {
  navigator.clipboard.writeText(text).then(() => {
    showToast('Formula copied to clipboard!', 'success');
    if (btnElement) {
      const origHtml = btnElement.innerHTML;
      btnElement.innerHTML = `<i data-lucide="check" class="w-3.5 h-3.5 text-emerald-500"></i> Copied`;
      if (window.lucide) lucide.createIcons();
      setTimeout(() => {
        btnElement.innerHTML = origHtml;
        if (window.lucide) lucide.createIcons();
      }, 2000);
    }
  }).catch(() => {
    showToast('Failed to copy formula', 'error');
  });
}

// Toast notification
function showToast(message, type = 'info') {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'fixed bottom-4 right-4 z-[100] flex flex-col gap-2 max-w-sm w-full pointer-events-none px-4 sm:px-0';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  const bgClass = type === 'success' 
    ? 'bg-emerald-600 text-white' 
    : type === 'error' 
    ? 'bg-rose-600 text-white' 
    : 'bg-slate-900 text-white dark:bg-slate-800';
  
  toast.className = `${bgClass} px-4 py-3 rounded-xl shadow-xl text-xs sm:text-sm font-medium flex items-center justify-between gap-3 pointer-events-auto transform transition-all duration-300 translate-y-2 opacity-0`;
  toast.innerHTML = `
    <div class="flex items-center gap-2">
      <i data-lucide="${type === 'success' ? 'check-circle' : type === 'error' ? 'alert-triangle' : 'info'}" class="w-4 h-4 shrink-0"></i>
      <span>${message}</span>
    </div>
    <button onclick="this.parentElement.remove()" class="text-white/70 hover:text-white">&times;</button>
  `;

  container.appendChild(toast);
  if (window.lucide) lucide.createIcons();

  requestAnimationFrame(() => {
    toast.classList.remove('translate-y-2', 'opacity-0');
  });

  setTimeout(() => {
    toast.classList.add('opacity-0', 'translate-y-2');
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// KaTeX Safe Auto-Renderer
function renderMath(element) {
  const target = element || document.body;
  if (typeof renderMathInElement !== 'undefined') {
    renderMathInElement(target, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false }
      ],
      throwOnError: false
    });
  }
}

// Global Keyboard Shortcuts
document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
    e.preventDefault();
    openSearchModal();
  }
  if (e.key === 'Escape') {
    closeSearchModal();
    toggleMobileMenu(true);
  }
});

// Page Initialization
document.addEventListener('DOMContentLoaded', () => {
  updateThemeIcons();
  if (window.lucide) lucide.createIcons();
  renderMath(document.body);
});
