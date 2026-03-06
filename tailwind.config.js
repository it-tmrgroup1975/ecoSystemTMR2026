/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/templates/**/*.html",
    "./static/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        'erp-purple': '#714B67', // Odoo Official Color
        'erp-bg': '#F4F7F6',
      }
    },
  },
  plugins: [],
}