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

// ตรวจสอบกรณีเปลี่ยนขนาดหน้าจอ (Resize) แล้วลืมปิด Overlay
window.addEventListener('resize', () => {
    if (window.innerWidth >= 768) { // 768px คือ md: ของ Tailwind
        const sidebar = document.getElementById('main-sidebar');
        const overlay = document.getElementById('sidebar-overlay');
        if (sidebar) sidebar.classList.remove('-translate-x-full');
        if (overlay) overlay.classList.add('hidden');
        document.body.style.overflow = 'auto';
    } else {
        const sidebar = document.getElementById('main-sidebar');
        if (sidebar && !sidebar.classList.contains('translate-x-0')) {
             sidebar.classList.add('-translate-x-full');
        }
    }
});