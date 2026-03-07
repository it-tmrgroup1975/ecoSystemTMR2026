/**
 * TMR Ecosystem 2026 - Master Interface Logic
 * Senior ERP Architect Standard
 */

// --- 1. Mobile Menu Logic ---
window.toggleMobileMenu = function() {
    const sidebar = document.getElementById('main-sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    const body = document.body;

    if (!sidebar || !overlay) return;

    const isHidden = sidebar.classList.contains('-translate-x-full');

    if (isHidden) {
        sidebar.classList.replace('-translate-x-full', 'translate-x-0');
        overlay.classList.remove('hidden');
        body.style.overflow = 'hidden';
    } else {
        sidebar.classList.replace('translate-x-0', '-translate-x-full');
        overlay.classList.add('hidden');
        body.style.overflow = 'auto';
    }
};

// --- 2. User Profile Popup Logic ---
window.toggleUserDropdown = function(event) {
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }

    const dropdown = document.getElementById('user-dropdown');
    if (!dropdown) return;

    // สลับคลาส hidden เพื่อแสดง/ซ่อน
    if (dropdown.classList.contains('hidden')) {
        dropdown.classList.remove('hidden');
    } else {
        dropdown.classList.add('hidden');
    }
};

// --- 3. Global Click Listener (ปิด Popup เมื่อคลิกที่อื่น) ---
window.addEventListener('click', function(e) {
    const dropdown = document.getElementById('user-dropdown');
    // ถ้าเมนูเปิดอยู่ และจุดที่คลิกไม่ใช่ตัวเมนูเอง ให้ปิดเมนู
    if (dropdown && !dropdown.classList.contains('hidden')) {
        if (!dropdown.contains(e.target)) {
            dropdown.classList.add('hidden');
        }
    }
});

// --- 4. Window Resize Observer ---
window.addEventListener('resize', () => {
    const isDesktop = window.innerWidth >= 768;
    const sidebar = document.getElementById('main-sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    const dropdown = document.getElementById('user-dropdown');

    if (isDesktop) {
        if (sidebar) sidebar.classList.replace('-translate-x-full', 'translate-x-0');
        if (overlay) overlay.classList.add('hidden');
    } else {
        if (dropdown) dropdown.classList.add('hidden');
    }
});

console.log("🚀 TMR Ecosystem Interface: Operational");