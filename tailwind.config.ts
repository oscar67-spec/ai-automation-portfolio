import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: { sans: ["var(--font-inter)", "sans-serif"] },
      colors: {
        primary: {
          50: "#f0fdfa", 100: "#ccfbf1", 200: "#99f6e4", 300: "#5eead4",
          400: "#2dd4bf", 500: "#14b8a6", 600: "#0F766E", 700: "#0d9488",
          800: "#115e59", 900: "#134e4a", 950: "#042f2e",
        },
        secondary: {
          50: "#F9FAFB", 100: "#f3f4f6", 200: "#e5e7eb", 300: "#d1d5db",
          400: "#9ca3af", 500: "#6B7280", 600: "#4b5563", 700: "#374151",
          800: "#1f2937", 900: "#1F2933", 950: "#0f172a",
        },
      },
    },
  },
  plugins: [],
};
export default config;