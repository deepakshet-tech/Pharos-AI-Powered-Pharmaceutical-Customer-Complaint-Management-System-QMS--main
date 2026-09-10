import tailwindcssAnimate from "tailwindcss-animate";

/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bone: "#F5F7FB",
        ink: "#0F172A",
        pine: "#0B1220",
        brand: {
          DEFAULT: "#2563EB",
          dark: "#1D4ED8",
          soft: "#DBEAFE",
          glow: "#38BDF8",
        },
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
        display: ["Inter", "system-ui", "sans-serif"],
        mono: ["Inter", "ui-monospace", "monospace"],
      },
      boxShadow: {
        card: "0 1px 2px rgba(15,23,42,.05), 0 10px 24px -12px rgba(37,99,235,.22)",
        lift: "0 2px 6px rgba(15,23,42,.06), 0 18px 32px -14px rgba(37,99,235,.26)",
      },
    },
  },
  plugins: [tailwindcssAnimate],
};
