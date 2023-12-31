/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/**/*.{html,js,svelte,ts}",
    "./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}",
  ],
  plugins: [require("flowbite/plugin")],
  darkMode: "class",
  theme: {
    extend: {
      fontFamily: {
        // raleway: ["Raleway", "sans-serif"],
        // Inter: ["Inter", "sans-serif"],
      },
      colors: {
        // blue: "#1E1E1E",
        // pink: "#E1348B",
        // bs: "#0D0E14",
        // primary: "#E1348B",
      },
      screens: {
        sm: "768px",
        lg: "1024px",
        xl: "1280px",
      },
    },

    fontFamily: {
      // ral: ["Raleway", "sans-serif"],
      // raleway: ["Raleway", "sans-serif"],
      // Inter: ["Inter", "sans-serif"],
    },
  },
};

// colors: {
//   primary: {
//     50: '#FFF5F2',
//     100: '#FFF1EE',
//     200: '#FFE4DE',
//     300: '#FFD5CC',
//     400: '#FFBCAD',
//     500: '#FE795D',
//     600: '#EF562F',
//     700: '#EB4F27',
//     800: '#CC4522',
//     900: '#A5371B'
//   }
// }
