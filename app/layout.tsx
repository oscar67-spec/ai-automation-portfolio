import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { Header, Footer } from "@/components/layout";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
export const metadata: Metadata = { title: "AI Automation Engineer | Portfolio", description: "Portfolio showcasing AI automation systems." };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="flex min-h-screen flex-col bg-secondary-50 font-sans text-secondary-900 antialiased">
        <Header /><main className="flex-grow">{children}</main><Footer />
      </body>
    </html>
  );
}