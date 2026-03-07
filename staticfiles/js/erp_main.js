// static/js/erp_main.js

/**
 * TMR Ecosystem - Mobile Menu Toggle Logic
 */
function toggleMobileMenu() {
    const sidebar = document.getElementById('main-sidebar');
    const overlay = document.getElementById('sidebar-overlay');

    if (sidebar && overlay) {
        // ตรวจสอบสถานะผ่าน class ของ Tailwind
        const isHidden = sidebar.classList.contains('-translate-x-full');

        if (isHidden) {
            // เปิดเมนู
            sidebar.classList.remove('-translate-x-full');
            sidebar.classList.add('translate-x-0');
            overlay.classList.remove('hidden');
            // ป้องกันการ scroll พื้นหลังเมื่อเปิดเมนู
            document.body.style.overflow = 'hidden';
        } else {
            // ปิดเมนู
            sidebar.classList.add('-translate-x-full');
            sidebar.classList.remove('translate-x-0');
            overlay.classList.add('hidden');
            document.body.style.overflow = 'auto';
        }
    }
}

/**
 * TMR Ecosystem - User Dropdown Toggle
 */
function toggleUserDropdown(event) {
    // ป้องกัน Event ลามไปหา window
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }

    const dropdown = document.getElementById('user-dropdown');
    if (!dropdown) return;

    // ตรวจสอบว่ามีคลาส hidden หรือไม่
    const isHidden = dropdown.classList.contains('hidden');

    if (isHidden) {
        dropdown.classList.remove('hidden');
        // เพิ่ม Animation เล็กน้อย
        dropdown.classList.add('block');
    } else {
        dropdown.classList.add('hidden');
        dropdown.classList.remove('block');
    }
}

// ปิด Dropdown เมื่อคลิกที่อื่น
window.addEventListener('click', function(e) {
    const dropdown = document.getElementById('user-dropdown');
    if (dropdown && !dropdown.classList.contains('hidden')) {
        // ตรวจสอบว่าจุดที่คลิก ไม่ใช่ตัว dropdown เอง
        if (!dropdown.contains(e.target)) {
            dropdown.classList.add('hidden');
        }
    }
});

// ปรับปรุงฟังก์ชัน Resize เพื่อความสมบูรณ์
window.addEventListener('resize', () => {
    const isDesktop = window.innerWidth >= 768;
    const sidebar = document.getElementById('main-sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    const dropdown = document.getElementById('user-dropdown');

    if (isDesktop) {
        if (sidebar) sidebar.classList.remove('-translate-x-full');
        if (overlay) overlay.classList.add('hidden');
    } else {
        if (dropdown) dropdown.classList.add('hidden'); // ปิด dropdown เมื่อสลับเป็น mobile เพื่อความสะอาด
    }
});