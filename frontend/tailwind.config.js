/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#C41E3A',
        'primary-hover': '#E0243F',
        dark: '#0D0B0B',
        'dark-elevated': '#1A1616',
        'dark-card': '#201B1B',
        gold: '#D4A843',
        'gold-hover': '#E8C25A',
        'gold-light': '#F5E6B8',
        fg: '#F5F0EB',
        'fg-muted': '#A89E94',
        border: '#3A3230',
      },
      fontFamily: {
        heading: ['Playfair Display', 'Times New Roman', 'Georgia', 'serif'],
        body: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
