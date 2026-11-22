/**
 * CalcVault M-1 Core Application Script
 * 100% Free & Open Access - No Paywalls
 * Author: Krishna Kumar (B.Tech Cybersecurity, CGC CEC Landran)
 */

// Safe Storage Wrapper (resilient to sandboxed iframes and strict storage policies)
const memStore = {};
const safeStorage = {
  get(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (e) {
      return memStore[key] || null;
    }
  },
  set(key, val) {
    memStore[key] = String(val);
    try {
      window.localStorage.setItem(key, String(val));
    } catch (e) {}
  },
  remove(key) {
    delete memStore[key];
    try {
      window.localStorage.removeItem(key);
    } catch (e) {}
  }
};

// Global App State
let selectedUnit = "All";
let currentQuestionId = (typeof QUESTIONS_DB !== 'undefined' && QUESTIONS_DB.length > 0) ? QUESTIONS_DB[0].id : null;
let revealedCount = 1;
let masteredIds = new Set(JSON.parse(safeStorage.get('btam101_mastered') || '[]'));

// Theme Management
function initTheme() {
  const savedTheme = safeStorage.get('calcvault_theme');
  if (savedTheme === 'light') {
    document.documentElement.classList.remove('dark');
  } else {
    // Default to dark theme for night-time engineering exam study
    document.documentElement.classList.add('dark');
  }
  updateThemeIcons();
}

function toggleTheme() {
  const isDark = document.documentElement.classList.toggle('dark');
  safeStorage.set('calcvault_theme', isDark ? 'dark' : 'light');
  updateThemeIcons();
}

function updateThemeIcons() {
  const isDark = document.documentElement.classList.contains('dark');
  document.querySelectorAll('.theme-icon-sun').forEach(el => {
    el.style.display = isDark ? 'inline-block' : 'none';
  });
  document.querySelectorAll('.theme-icon-moon').forEach(el => {
    el.style.display = isDark ? 'none' : 'inline-block';
  });
}

// Mobile Menu Toggle
function toggleMobileMenu() {
  const menu = document.getElementById('mobile-nav-menu');
  if (menu) {
    menu.classList.toggle('hidden');
  }
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

// Filtered Questions Helper
function getFilteredQuestions() {
  if (typeof QUESTIONS_DB === 'undefined') return [];
  const searchInput = document.getElementById('search-input');
  const query = searchInput ? searchInput.value.toLowerCase().trim() : '';

  return QUESTIONS_DB.filter(q => {
    const matchesUnit = selectedUnit === "All" || q.unit === selectedUnit;
    const matchesSearch = !query ||
      q.title.toLowerCase().includes(query) ||
      q.problem.toLowerCase().includes(query) ||
      q.unit.toLowerCase().includes(query);
    return matchesUnit && matchesSearch;
  });
}

// Interactive Whiteboard Logic
function initWhiteboard() {
  if (typeof QUESTIONS_DB === 'undefined' || QUESTIONS_DB.length === 0) return;

  // Read URL query parameters for direct deep-linking
  const params = new URLSearchParams(window.location.search);
  const unitParam = params.get('unit');
  const topicParam = params.get('topic');

  if (unitParam && UNITS.includes(unitParam)) {
    selectedUnit = unitParam;
  }
  if (topicParam && QUESTIONS_DB.some(q => q.id === topicParam)) {
    currentQuestionId = topicParam;
    const found = QUESTIONS_DB.find(q => q.id === topicParam);
    if (found && !unitParam) {
      selectedUnit = found.unit;
    }
  }

  renderUnitTabs();
  renderQuestionList();
  if (currentQuestionId) {
    loadSlide(currentQuestionId);
  }
  updateGlobalStats();
}

function renderUnitTabs() {
  const container = document.getElementById('unit-tabs');
  if (!container || typeof UNITS === 'undefined') return;

  container.innerHTML = UNITS.map(unit => {
    const active = selectedUnit === unit;
    const label = unit === "All" ? `All Topics (${QUESTIONS_DB.length})` : unit;
    return `
      <button type="button" onclick="selectUnit('${unit}')"
        class="px-3.5 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap transition ${
          active
            ? 'bg-cyan-600 text-white shadow-sm'
            : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
        }">
        ${label}
      </button>
    `;
  }).join('');
}

function selectUnit(unit) {
  selectedUnit = unit;
  renderUnitTabs();
  renderQuestionList();
  const filtered = getFilteredQuestions();
  if (filtered.length > 0 && !filtered.some(q => q.id === currentQuestionId)) {
    loadSlide(filtered[0].id);
  }
}

function renderQuestionList() {
  const listEl = document.getElementById('question-list');
  if (!listEl) return;

  const filtered = getFilteredQuestions();
  const countLabel = document.getElementById('question-count-label');
  const progressBadge = document.getElementById('progress-badge');

  if (countLabel) countLabel.textContent = `${filtered.length} Topics Shown`;
  if (progressBadge) progressBadge.textContent = `${masteredIds.size} / ${QUESTIONS_DB.length} Mastered`;

  if (filtered.length === 0) {
    listEl.innerHTML = `<div class="p-6 text-center text-sm text-slate-400">No matching questions found in ${selectedUnit}.</div>`;
    return;
  }

  listEl.innerHTML = filtered.map(q => {
    const isSelected = q.id === currentQuestionId;
    const isMastered = masteredIds.has(q.id);
    return `
      <button type="button" onclick="loadSlide('${q.id}')"
        class="text-left p-3.5 rounded-xl border transition-all ${
          isSelected
            ? 'bg-cyan-500/10 border-cyan-500 shadow-sm'
            : 'bg-white dark:bg-[#151e32] border-slate-200 dark:border-slate-800 hover:border-cyan-400 dark:hover:border-cyan-600'
        }">
        <div class="flex items-center justify-between gap-2 mb-1">
          <span class="text-[11px] font-bold uppercase tracking-wider text-cyan-600 dark:text-cyan-400">${q.unit} • ${q.marks}</span>
          ${isMastered ? '<span class="text-xs text-emerald-500 font-bold flex items-center gap-1">✓ Mastered</span>' : ''}
        </div>
        <div class="text-sm font-semibold text-slate-800 dark:text-slate-100 line-clamp-2">${q.title}</div>
      </button>
    `;
  }).join('');
}

function loadSlide(id) {
  currentQuestionId = id;
  revealedCount = 1;
  const q = QUESTIONS_DB.find(item => item.id === id);
  if (!q) return;

  const unitBadge = document.getElementById('slide-unit-badge');
  const marksBadge = document.getElementById('slide-marks-badge');
  const title = document.getElementById('slide-title');
  const problem = document.getElementById('slide-problem');
  const intuition = document.getElementById('intuition-text');

  if (unitBadge) unitBadge.textContent = q.unit;
  if (marksBadge) marksBadge.textContent = q.marks;
  if (title) title.textContent = q.title;
  if (problem) problem.innerHTML = q.problem;
  if (intuition) intuition.innerHTML = q.intuition;

  updateMasteredButton();
  renderSteps();
  renderQuestionList();
  renderMath(document.getElementById('slide-problem'));
  renderMath(document.getElementById('intuition-box'));
}

function renderSteps() {
  const q = QUESTIONS_DB.find(item => item.id === currentQuestionId);
  const container = document.getElementById('steps-container');
  if (!q || !container) return;

  const total = q.steps.length;
  const stepCounter = document.getElementById('step-counter');
  if (stepCounter) stepCounter.textContent = `Step ${Math.min(revealedCount, total)} of ${total}`;

  const nextBtn = document.getElementById('next-step-btn');
  if (nextBtn) {
    if (revealedCount >= total) {
      nextBtn.classList.add('opacity-50', 'cursor-not-allowed');
    } else {
      nextBtn.classList.remove('opacity-50', 'cursor-not-allowed');
    }
  }

  container.innerHTML = q.steps.slice(0, revealedCount).map((step, idx) => `
    <div class="step-animate p-4 rounded-xl bg-slate-50 dark:bg-[#0b1120] border border-slate-200 dark:border-slate-800">
      <div class="flex items-center gap-2 mb-1.5">
        <span class="w-6 h-6 rounded-full bg-cyan-600 text-white text-xs font-bold flex items-center justify-center shrink-0">
          ${idx + 1}
        </span>
        <h3 class="text-xs sm:text-sm font-bold text-cyan-700 dark:text-cyan-400 uppercase tracking-wide">
          ${step.label}
        </h3>
      </div>
      <div class="text-sm sm:text-base text-slate-800 dark:text-slate-200 leading-relaxed pl-8">
        ${step.math}
      </div>
    </div>
  `).join('');

  renderMath(container);
  container.scrollTop = container.scrollHeight;
}

function revealNextStep() {
  const q = QUESTIONS_DB.find(item => item.id === currentQuestionId);
  if (q && revealedCount < q.steps.length) {
    revealedCount++;
    renderSteps();
  }
}

function revealAllSteps() {
  const q = QUESTIONS_DB.find(item => item.id === currentQuestionId);
  if (q) {
    revealedCount = q.steps.length;
    renderSteps();
  }
}

function resetSteps() {
  revealedCount = 1;
  renderSteps();
}

function nextQuestion() {
  const filtered = getFilteredQuestions();
  const idx = filtered.findIndex(q => q.id === currentQuestionId);
  if (idx >= 0 && idx < filtered.length - 1) {
    loadSlide(filtered[idx + 1].id);
  }
}

function prevQuestion() {
  const filtered = getFilteredQuestions();
  const idx = filtered.findIndex(q => q.id === currentQuestionId);
  if (idx > 0) {
    loadSlide(filtered[idx - 1].id);
  }
}

// Revision Mastery Progress Tracker
function toggleMastered(targetId) {
  const id = targetId || currentQuestionId;
  if (!id) return;

  if (masteredIds.has(id)) {
    masteredIds.delete(id);
  } else {
    masteredIds.add(id);
  }
  safeStorage.set('btam101_mastered', JSON.stringify([...masteredIds]));
  updateMasteredButton();
  renderQuestionList();
  updateGlobalStats();
}

function updateMasteredButton() {
  const btn = document.getElementById('mastered-btn');
  if (!btn) return;

  const isMastered = masteredIds.has(currentQuestionId);
  if (isMastered) {
    btn.className = "flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-emerald-600 text-white shadow-sm transition";
    btn.innerHTML = `<i data-lucide="check-circle-2" class="w-4 h-4"></i><span>Mastered ✓</span>`;
  } else {
    btn.className = "flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold border border-slate-300 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 transition";
    btn.innerHTML = `<i data-lucide="circle" class="w-4 h-4"></i><span>Mark as Mastered</span>`;
  }
  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function updateGlobalStats() {
  const badge = document.getElementById('global-mastery-count');
  if (badge && typeof QUESTIONS_DB !== 'undefined') {
    badge.textContent = `${masteredIds.size} / ${QUESTIONS_DB.length}`;
  }
}

// 100% Free Instant Print & PDF Cheat-Sheet
function buildPrintableCheatSheet(filterUnit = "All") {
  const printContent = document.getElementById('print-content');
  if (!printContent || typeof QUESTIONS_DB === 'undefined') return;

  const questionsToPrint = filterUnit === "All"
    ? QUESTIONS_DB
    : QUESTIONS_DB.filter(q => q.unit === filterUnit);

  const cardsHtml = questionsToPrint.map((q, index) => `
    <div class="print-card mb-4 p-4 border border-slate-300 rounded-lg">
      <div class="text-xs font-bold uppercase text-indigo-700">${q.unit} • ${q.marks}</div>
      <h3 class="text-base font-bold mt-0.5">${index + 1}. ${q.title}</h3>
      <div class="text-sm font-medium my-2 p-2 bg-slate-100 rounded">${q.problem}</div>
      <div class="text-xs italic text-slate-600 mb-2"><b>PTU Evaluator Tip:</b> ${q.intuition}</div>
      <div class="space-y-2 text-sm">
        ${q.steps.map(s => `<div><b>${s.label}:</b> ${s.math}</div>`).join('')}
      </div>
    </div>
  `).join('');

  const footerCreditHtml = `
    <div class="print-card bg-slate-50 border border-slate-300 mt-6 p-4 rounded-lg">
      <div class="flex items-center justify-between gap-4">
        <div>
          <div class="text-xs font-bold uppercase text-cyan-800">CalcVault M-1 • IKG-PTU BTAM101-18 Exam Revision</div>
          <h3 class="text-base font-bold mt-0.5">Author &amp; Curator: Krishna Kumar</h3>
          <p class="text-xs text-slate-600">B.Tech Cybersecurity, CGC College of Engineering, Landran • Free Educational Resource</p>
          <p class="text-xs text-slate-700 mt-1">
            Complete 26-Topic High-Yield Revision Guide for 1st Semester Engineering Students. Free for all peers.
          </p>
        </div>
      </div>
    </div>
  `;

  printContent.innerHTML = cardsHtml + footerCreditHtml;
  renderMath(printContent);
}

// Instant One-Click Print Trigger (No Payment, No Popups)
function triggerCheatSheetPrint(filterUnit = "All") {
  buildPrintableCheatSheet(filterUnit);
  const printContainer = document.getElementById('print-container');
  if (printContainer) {
    printContainer.classList.remove('hidden');
    renderMath(printContainer);
  }
  setTimeout(() => {
    window.print();
  }, 200);
}

// Initialize Application on Page Load
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  if (document.getElementById('question-list')) {
    initWhiteboard();
  }
  if (document.getElementById('print-content')) {
    buildPrintableCheatSheet();
  }
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});
