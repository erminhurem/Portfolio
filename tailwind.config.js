/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', './static/**/*.css', './static/**/*.js'],
  theme: {
    extend: { colors: {
                'navy-blue': '#001F3F',
                'light-gray': '#F5F5F5',
                'orange': '#FF851B',
                },
              },
  },
  plugins: [],
}

