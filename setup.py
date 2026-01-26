import os

# Define the project structure and file contents
project_files = {
    "package.json": """{
  "name": "ai-portfolio",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "14.2.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "zod": "^3.22.4",
    "resend": "^3.2.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.2.1",
    "lucide-react": "^0.358.0"
  },
  "devDependencies": {
    "typescript": "^5.3.3",
    "@types/node": "^20.11.0",
    "@types/react": "^18.2.48",
    "@types/react-dom": "^18.2.18",
    "autoprefixer": "^10.4.17",
    "postcss": "^8.4.33",
    "tailwindcss": "^3.4.1",
    "eslint": "^8.56.0",
    "eslint-config-next": "14.2.0"
  }
}""",
    "next.config.js": """/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};

module.exports = nextConfig;""",
    "tsconfig.json": """{
  "compilerOptions": {
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}""",
    "tailwind.config.ts": """import type { Config } from "tailwindcss";

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
export default config;""",
    "postcss.config.js": """module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};""",
    ".env.local.example": """RESEND_API_KEY=re_xxxxxxxxxxxx
CONTACT_EMAIL=your-email@example.com""",
    "app/globals.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply bg-secondary-50 text-secondary-900;
  }
}""",
    "lib/utils.ts": """import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}""",
    "lib/data.ts": """import { z } from "zod";

// --- Types ---
export interface CaseStudy {
  slug: string;
  title: string;
  description: string;
  problem: string;
  solution: string;
  technicalApproach: string;
  tools: string[];
  outcome: string;
  status: "Live" | "Case Study" | "Prototype";
  demoLink?: string;
  repoLink?: string;
  publishedDate: string;
  tags: string[];
}

export interface ContactFormData {
  name: string;
  email: string;
  message: string;
  source?: string;
}

// --- Validation Schemas ---
export const contactFormSchema = z.object({
  name: z.string().min(2, { message: "Name must be at least 2 characters." }),
  email: z.string().email({ message: "Please enter a valid email address." }),
  message: z.string().min(10, { message: "Message must be at least 10 characters." }),
  source: z.string().optional(),
});

// --- Data ---
const caseStudies: CaseStudy[] = [
  {
    slug: "ai-whatsapp-sales-agent",
    title: "AI WhatsApp Sales Agent",
    description: "An intelligent sales assistant that handles end-to-end sales conversations on WhatsApp.",
    problem: "Manual WhatsApp sales processes do not scale effectively. Responding to every inquiry manually is slow.",
    solution: "Built an LLM agent with persistent memory to lookup products, log chats, and place orders directly.",
    technicalApproach: "Orchestrated using n8n workflows with a LangChain agent. Integrates Google Sheets and WhatsApp Business API.",
    tools: ["n8n", "LangChain agent", "Google Sheets", "WhatsApp API", "Gemini", "OpenAI"],
    outcome: "Automated end-to-end sales conversations with built-in guardrails.",
    status: "Prototype",
    publishedDate: "2024-09-15",
    tags: ["AI Agent", "WhatsApp", "Sales"],
  },
  {
    slug: "x-twitter-lead-finder",
    title: "X (Twitter) Automation Lead Finder",
    description: "Automated pipeline for sourcing leads and generating personalized outreach on X.",
    problem: "Finding qualified automation leads manually is difficult and time consuming.",
    solution: "Created a system for scheduled search, filtering, and enrichment via Apollo with LLM-personalized emails.",
    technicalApproach: "Utilizes X API for data monitoring, Apollo for enrichment, and Groq for fast inference. Logic handles dispatch via Gmail.",
    tools: ["X API", "Apollo", "Groq", "Gmail", "Google Sheets", "n8n"],
    outcome: "Created a fully automated lead sourcing to outreach pipeline.",
    status: "Live",
    publishedDate: "2024-11-02",
    tags: ["Lead Gen", "Outreach", "AI Writing"],
  },
  {
    slug: "google-maps-business-scraper",
    title: "Google Maps Business Scraper",
    description: "High-efficiency scraping workflow for local business intelligence and lead generation.",
    problem: "Manual contact research is slow and tedious.",
    solution: "Developed a workflow to scrape maps results, extract websites/emails, deduplicate entries, and store clean data.",
    technicalApproach: "Implemented in n8n using raw HTTP requests and JavaScript for parsing. Includes logic for validation.",
    tools: ["n8n", "HTTP", "JavaScript", "Google Sheets"],
    outcome: "Significantly faster business lead list generation compared to manual research.",
    status: "Live",
    publishedDate: "2024-08-20",
    tags: ["Scraping", "Lead Intelligence"],
  },
  {
    slug: "daily-ai-news-summary-agent",
    title: "Daily AI News Summary Agent",
    description: "Autonomous agent that curates, summarizes, and delivers daily AI industry news.",
    problem: "Daily news synthesis takes time and information overload is common.",
    solution: "Built an automation for RSS ingestion combined with LLM summarization and direct email delivery.",
    technicalApproach: "Ingests data from multiple RSS feeds, uses OpenAI for summarization, and creates a daily digest via Gmail.",
    tools: ["RSS", "OpenAI", "Gmail", "n8n"],
    outcome: "Provides automated daily briefings to save research time.",
    status: "Live",
    publishedDate: "2024-07-10",
    tags: ["Research Automation", "Summarization"],
  },
];

export const getAllCaseStudies = () => caseStudies.sort((a, b) => new Date(b.publishedDate).getTime() - new Date(a.publishedDate).getTime());
export const getCaseStudyBySlug = (slug: string) => caseStudies.find((study) => study.slug === slug);
export const getFeaturedCaseStudies = (count: number) => getAllCaseStudies().slice(0, count);""",
    "lib/email.ts": """import { Resend } from "resend";
import { ContactFormData } from "./data";

const resend = new Resend(process.env.RESEND_API_KEY);

export async function sendContactEmail(data: ContactFormData) {
  if (!process.env.RESEND_API_KEY) {
    console.log("Resend API Key missing. Simulating email send:", data);
    return { success: true };
  }
  try {
    await resend.emails.send({
      from: "Portfolio Contact <onboarding@resend.dev>",
      to: process.env.CONTACT_EMAIL || "delivered@resend.dev",
      subject: "New Contact Form Submission",
      html: `<h2>New Contact Request</h2><p><strong>Name:</strong> ${data.name}</p><p><strong>Email:</strong> ${data.email}</p><p><strong>Source:</strong> ${data.source || "N/A"}</p><br /><p><strong>Message:</strong></p><p>${data.message}</p>`,
    });
    return { success: true };
  } catch (error) {
    console.error("Failed to send email:", error);
    throw error;
  }
}""",
    "components/ui.tsx": """import React, { forwardRef } from "react";
import { cn } from "@/lib/utils";

// --- Button ---
export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary";
  size?: "sm" | "md" | "lg";
}
export const Button: React.FC<ButtonProps> = ({ className, variant = "primary", size = "md", ...props }) => {
  const variants = {
    primary: "bg-primary-600 text-white hover:bg-primary-700 focus:ring-primary-500",
    secondary: "bg-white text-secondary-900 border border-secondary-300 hover:bg-secondary-50 focus:ring-secondary-500",
  };
  const sizes = { sm: "px-3 py-1.5 text-sm", md: "px-4 py-2 text-base", lg: "px-6 py-3 text-lg" };
  return (
    <button className={cn("inline-flex items-center justify-center rounded-md font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50", variants[variant], sizes[size], className)} {...props} />
  );
};

// --- Input ---
export const Input = forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement> & { error?: string }>(({ className, error, ...props }, ref) => (
  <div className="w-full">
    <input ref={ref} className={cn("w-full rounded-md border border-secondary-300 bg-white px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary-500", error && "border-red-500 focus:ring-red-500", className)} {...props} />
    {error && <p className="mt-1 text-xs text-red-500">{error}</p>}
  </div>
));
Input.displayName = "Input";

// --- Textarea ---
export const Textarea = forwardRef<HTMLTextAreaElement, React.TextareaHTMLAttributes<HTMLTextAreaElement> & { error?: string }>(({ className, error, ...props }, ref) => (
  <div className="w-full">
    <textarea ref={ref} className={cn("w-full rounded-md border border-secondary-300 bg-white px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 min-h-[100px]", error && "border-red-500 focus:ring-red-500", className)} {...props} />
    {error && <p className="mt-1 text-xs text-red-500">{error}</p>}
  </div>
));
Textarea.displayName = "Textarea";

// --- Card ---
export const Card: React.FC<React.HTMLAttributes<HTMLDivElement>> = ({ className, children, ...props }) => (
  <div className={cn("bg-white rounded-lg border border-secondary-200 shadow-sm overflow-hidden", className)} {...props}>{children}</div>
);""",
    "components/layout.tsx": """ "use client";
import React, { useState } from "react";
import Link from "next/link";
import { Menu, X, Cpu, Linkedin, Twitter, Mail, FileText } from "lucide-react";
import { Button } from "@/components/ui";

export const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const navLinks = [{ href: "/", label: "Home" }, { href: "/automations", label: "Automations" }, { href: "/about", label: "About" }, { href: "/contact", label: "Contact" }];

  return (
    <header className="sticky top-0 z-50 w-full border-b border-secondary-200 bg-white/80 backdrop-blur-md">
      <div className="container mx-auto px-4 md:px-6">
        <div className="flex h-16 items-center justify-between">
          <Link href="/" className="flex items-center gap-2 font-bold text-secondary-900">
            <Cpu className="h-6 w-6 text-primary-600" />
            <span className="text-xl">AI AutoEng</span>
          </Link>
          <nav className="hidden md:flex items-center gap-6">
            {navLinks.map((link) => <Link key={link.href} href={link.href} className="text-sm font-medium text-secondary-600 hover:text-primary-600">{link.label}</Link>)}
            <Link href="/contact"><Button size="sm">Discuss an Automation</Button></Link>
          </nav>
          <button className="md:hidden p-2" onClick={() => setIsMenuOpen(!isMenuOpen)}>{isMenuOpen ? <X /> : <Menu />}</button>
        </div>
      </div>
      {isMenuOpen && (
        <div className="md:hidden border-t border-secondary-200 bg-white px-4 py-4 shadow-lg flex flex-col space-y-4">
          {navLinks.map((link) => <Link key={link.href} href={link.href} onClick={() => setIsMenuOpen(false)} className="text-base font-medium">{link.label}</Link>)}
          <Link href="/contact" onClick={() => setIsMenuOpen(false)}><Button className="w-full">Discuss an Automation</Button></Link>
        </div>
      )}
    </header>
  );
};

export const Footer = () => {
  return (
    <footer className="border-t border-secondary-200 bg-white">
      <div className="container mx-auto px-4 py-8 md:px-6 md:py-12">
        <div className="grid grid-cols-1 gap-8 md:grid-cols-4">
          <div className="space-y-4">
            <Link href="/" className="flex items-center gap-2 font-bold text-secondary-900"><Cpu className="h-6 w-6 text-primary-600" /><span className="text-xl">AI AutoEng</span></Link>
            <p className="text-sm text-secondary-500">Building intelligent automation systems that save time and drive revenue.</p>
          </div>
          <div>
            <h3 className="mb-4 text-sm font-semibold">Navigation</h3>
            <ul className="space-y-2 text-sm text-secondary-600">
              <li><Link href="/" className="hover:text-primary-600">Home</Link></li>
              <li><Link href="/automations" className="hover:text-primary-600">Automations</Link></li>
              <li><Link href="/contact" className="hover:text-primary-600">Contact</Link></li>
            </ul>
          </div>
          <div>
            <h3 className="mb-4 text-sm font-semibold">Connect</h3>
            <div className="flex space-x-4">
              <Link href="mailto:chidiadi.works@gmail.com" className="text-secondary-400 hover:text-primary-600"><Mail className="h-5 w-5" /><span className="sr-only">Email</span></Link>
              <Link href="https://www.linkedin.com/in/chidiadi-anyamele-792b01358" target="_blank" className="text-secondary-400 hover:text-primary-600"><Linkedin className="h-5 w-5" /><span className="sr-only">LinkedIn</span></Link>
              <Link href="https://x.com/tfawinner?s=21" target="_blank" className="text-secondary-400 hover:text-primary-600"><Twitter className="h-5 w-5" /><span className="sr-only">X</span></Link>
              <Link href="https://www.notion.so/Writing-Portfolio-Chidiadi-Oscar-80e4aeb6031d4a96967cd0a87849074a" target="_blank" className="text-secondary-400 hover:text-primary-600"><FileText className="h-5 w-5" /><span className="sr-only">Portfolio</span></Link>
            </div>
          </div>
        </div>
        <div className="mt-8 border-t pt-8 text-center text-sm text-secondary-500">&copy; {new Date().getFullYear()} AI Automation Engineer. All rights reserved.</div>
      </div>
    </footer>
  );
};""",
    "components/features.tsx": """ "use client";
import React, { useState } from "react";
import Link from "next/link";
import { ArrowRight, Calendar, ArrowLeft, ExternalLink, Github, CheckCircle2, Wrench, FileCode, Lightbulb } from "lucide-react";
import { Card, Button, Input, Textarea } from "@/components/ui";
import { CaseStudy, contactFormSchema } from "@/lib/data";
import { cn } from "@/lib/utils";

// --- Case Study Card ---
export const CaseStudyCard: React.FC<{ caseStudy: CaseStudy }> = ({ caseStudy }) => (
  <Link href={`/case-studies/${caseStudy.slug}`} className="group block h-full">
    <Card className="h-full transition-all duration-300 hover:shadow-lg hover:border-primary-200">
      <div className="p-6 flex flex-col h-full">
        <div className="mb-4 flex items-center justify-between">
          <span className={cn("inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium", caseStudy.status === "Live" ? "bg-green-100 text-green-800" : "bg-primary-50 text-primary-700")}>{caseStudy.status}</span>
          <div className="flex items-center text-xs text-secondary-500"><Calendar className="mr-1 h-3 w-3" />{new Date(caseStudy.publishedDate).toLocaleDateString()}</div>
        </div>
        <h3 className="mb-2 text-xl font-bold text-secondary-900 group-hover:text-primary-600">{caseStudy.title}</h3>
        <p className="mb-4 flex-grow text-sm text-secondary-500 line-clamp-3">{caseStudy.description}</p>
        <div className="flex items-center text-sm font-medium text-primary-600">View Case Study <ArrowRight className="ml-1 h-4 w-4" /></div>
      </div>
    </Card>
  </Link>
);

// --- Case Study Detail ---
export const CaseStudyDetail: React.FC<{ caseStudy: CaseStudy }> = ({ caseStudy }) => (
  <article className="container mx-auto max-w-4xl px-4 py-12 md:px-6">
    <Link href="/automations" className="mb-8 inline-flex items-center text-sm font-medium text-secondary-500 hover:text-primary-600"><ArrowLeft className="mr-1 h-4 w-4" /> Back to Automations</Link>
    <header className="mb-12 border-b border-secondary-200 pb-8">
      <div className="mb-4 flex flex-wrap items-center gap-3">
        <span className={cn("inline-flex items-center rounded-full px-3 py-1 text-sm font-medium", caseStudy.status === "Live" ? "bg-green-100 text-green-800" : "bg-primary-50 text-primary-700")}>{caseStudy.status}</span>
        <span className="flex items-center text-sm text-secondary-500"><Calendar className="mr-1.5 h-4 w-4" />{new Date(caseStudy.publishedDate).toLocaleDateString()}</span>
      </div>
      <h1 className="mb-4 text-3xl font-bold text-secondary-900 md:text-5xl">{caseStudy.title}</h1>
      <p className="text-xl text-secondary-600">{caseStudy.description}</p>
      <div className="mt-8 flex gap-4">
        {caseStudy.demoLink ? <Link href={caseStudy.demoLink} target="_blank"><Button className="gap-2">Watch Demo <ExternalLink className="h-4 w-4" /></Button></Link> : <div className="flex items-center gap-2 rounded-md bg-secondary-100 px-4 py-2 text-sm text-secondary-600"><span>Demo available on request.</span><Link href="/contact" className="font-medium text-primary-600 hover:underline">Contact me</Link></div>}
        {caseStudy.repoLink && <Link href={caseStudy.repoLink} target="_blank"><Button variant="secondary" className="gap-2">View Code <Github className="h-4 w-4" /></Button></Link>}
      </div>
    </header>
    <div className="grid gap-12 md:grid-cols-[2fr_1fr]">
      <div className="space-y-12">
        <section><h2 className="mb-4 flex items-center text-2xl font-bold"><Lightbulb className="mr-2 h-6 w-6 text-yellow-500" /> The Problem</h2><p className="text-lg text-secondary-700">{caseStudy.problem}</p></section>
        <section><h2 className="mb-4 flex items-center text-2xl font-bold"><Wrench className="mr-2 h-6 w-6 text-primary-500" /> The Solution</h2><p className="text-lg text-secondary-700">{caseStudy.solution}</p></section>
        <section><h2 className="mb-4 flex items-center text-2xl font-bold"><FileCode className="mr-2 h-6 w-6 text-purple-500" /> Technical Approach</h2><p className="text-lg text-secondary-700">{caseStudy.technicalApproach}</p></section>
        <section><h2 className="mb-4 flex items-center text-2xl font-bold"><CheckCircle2 className="mr-2 h-6 w-6 text-green-500" /> Outcomes</h2><p className="text-lg text-secondary-700">{caseStudy.outcome}</p></section>
      </div>
      <aside className="space-y-8">
        <div className="rounded-xl border border-secondary-200 p-6"><h3 className="mb-4 font-bold">Tech Stack</h3><div className="flex flex-wrap gap-2">{caseStudy.tools.map(t => <span key={t} className="rounded-md border px-3 py-1.5 text-sm">{t}</span>)}</div></div>
      </aside>
    </div>
  </article>
);

// --- Contact Form ---
export const ContactForm = () => {
  const [formData, setFormData] = useState({ name: "", email: "", message: "", source: "web" });
  const [status, setStatus] = useState("idle");
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus("submitting");
    const result = contactFormSchema.safeParse(formData);
    if (!result.success) { setStatus("idle"); return; }
    try {
      const res = await fetch("/api/contact", { method: "POST", body: JSON.stringify(formData) });
      const data = await res.json();
      if (!res.ok) throw new Error(data.message || "Error");
      setStatus("success"); setFormData({ name: "", email: "", message: "", source: "web" });
    } catch (err: any) { setStatus("error"); setErrorMessage(err.message); }
  };

  if (status === "success") return <div className="rounded-lg bg-green-50 p-6 text-center border border-green-200"><h3 className="text-xl font-bold text-green-800">Message Sent!</h3><p>I'll get back to you within 24 hours.</p><Button variant="secondary" onClick={() => setStatus("idle")} className="mt-4">Send another</Button></div>;

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {status === "error" && <div className="bg-red-50 p-4 text-red-700 border-red-200">{errorMessage}</div>}
      <div><label className="block text-sm font-medium mb-2">Name</label><Input value={formData.name} onChange={(e) => setFormData({ ...formData, name: e.target.value })} disabled={status === "submitting"} /></div>
      <div><label className="block text-sm font-medium mb-2">Email</label><Input type="email" value={formData.email} onChange={(e) => setFormData({ ...formData, email: e.target.value })} disabled={status === "submitting"} /></div>
      <div><label className="block text-sm font-medium mb-2">How did you find me?</label><select value={formData.source} onChange={(e) => setFormData({ ...formData, source: e.target.value })} className="w-full rounded-md border border-secondary-300 p-2 text-sm"><option value="web">Portfolio</option><option value="linkedin">LinkedIn</option><option value="twitter">Twitter</option></select></div>
      <div><label className="block text-sm font-medium mb-2">Message</label><Textarea value={formData.message} onChange={(e) => setFormData({ ...formData, message: e.target.value })} rows={5} disabled={status === "submitting"} /></div>
      <Button type="submit" className="w-full" disabled={status === "submitting"}>{status === "submitting" ? "Sending..." : "Send Message"}</Button>
    </form>
  );
};""",
    "app/layout.tsx": """import type { Metadata } from "next";
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
}""",
    "app/page.tsx": """import Link from "next/link";
import { ArrowRight, Bot, Terminal, Cpu, Workflow, Link as LinkIcon } from "lucide-react";
import { Button } from "@/components/ui";
import { CaseStudyCard } from "@/components/features";
import { getFeaturedCaseStudies } from "@/lib/data";

export default function Home() {
  const featured = getFeaturedCaseStudies(3);
  const stack = [{ n: "n8n", i: Workflow }, { n: "OpenAI", i: Bot }, { n: "LangChain", i: LinkIcon }, { n: "Twilio", i: Cpu }, { n: "Python", i: Terminal }];
  return (
    <div className="flex flex-col">
      <section className="relative overflow-hidden bg-white py-20 md:py-32">
        <div className="container mx-auto px-4 md:px-6 text-center max-w-4xl">
          <h1 className="mb-6 text-4xl font-extrabold text-secondary-900 sm:text-5xl md:text-6xl">I build automation workflows that replace manual work.</h1>
          <p className="mb-6 text-xl text-secondary-600">I design and implement practical automation systems using tools like n8n.</p>
          <div className="flex justify-center gap-4 flex-col sm:flex-row"><Link href="/contact"><Button size="lg" className="w-full sm:w-auto">Discuss an Automation</Button></Link><Link href="/automations"><Button variant="secondary" size="lg" className="w-full sm:w-auto">View Automations</Button></Link></div>
        </div>
      </section>
      <section className="py-20 container mx-auto px-4 md:px-6">
        <div className="mb-12 flex justify-between items-center"><h2 className="text-3xl font-bold">Featured Automations</h2><Link href="/automations" className="hidden sm:block"><Button variant="secondary">View All <ArrowRight className="ml-2 h-4 w-4" /></Button></Link></div>
        <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">{featured.map(s => <CaseStudyCard key={s.slug} caseStudy={s} />)}</div>
      </section>
      <section className="bg-white py-20 container mx-auto px-4 md:px-6 text-center">
        <h2 className="mb-12 text-3xl font-bold">Technology Stack</h2>
        <div className="flex flex-wrap justify-center gap-6">{stack.map(t => <div key={t.n} className="flex flex-col items-center p-4 border rounded-xl"><t.i className="h-8 w-8 mb-2" /><span>{t.n}</span></div>)}</div>
      </section>
      <section className="bg-secondary-900 py-20 text-white text-center">
        <div className="container mx-auto px-4">
          <h2 className="mb-6 text-3xl font-bold">Ready to automate your business?</h2>
          <Link href="/contact"><Button size="lg" className="bg-white text-secondary-900 hover:bg-secondary-100">Get in Touch</Button></Link>
        </div>
      </section>
    </div>
  );
}""",
    "app/about/page.tsx": """import Link from "next/link";
import { CheckCircle } from "lucide-react";
import { Button } from "@/components/ui";

export default function AboutPage() {
  const skills = { "AI Automation": ["Workflow Design", "AI Agents", "Prompt Engineering"], "Tools": ["n8n", "OpenAI / Gemini", "LangChain", "Web Scraping"] };
  return (
    <div className="container mx-auto px-4 py-16 md:px-6 max-w-4xl">
      <h1 className="mb-8 text-4xl font-bold">About Me</h1>
      <div className="grid gap-12 md:grid-cols-[2fr_1fr]">
        <div className="space-y-6 text-lg text-secondary-700">
          <p>I build automation systems that take repetitive, manual work off people’s hands. My focus is on designing practical workflows that connect tools, data, and AI.</p>
          <Link href="/contact"><Button size="lg">Let's Work Together</Button></Link>
        </div>
        <div className="space-y-6">
          {Object.entries(skills).map(([cat, items]) => (
            <div key={cat} className="rounded-xl border bg-white p-6 shadow-sm"><h3 className="mb-4 font-bold">{cat}</h3><ul className="space-y-2">{items.map(s => <li key={s} className="flex items-center text-sm"><CheckCircle className="mr-2 h-4 w-4 text-primary-500" />{s}</li>)}</ul></div>
          ))}
        </div>
      </div>
    </div>
  );
}""",
    "app/automations/page.tsx": """import { getAllCaseStudies } from "@/lib/data";
import { CaseStudyCard } from "@/components/features";

export default function AutomationsPage() {
  return (
    <div className="container mx-auto px-4 py-16 md:px-6">
      <h1 className="mb-4 text-4xl font-bold">AI Automation Projects</h1>
      <p className="mb-12 max-w-2xl text-xl text-secondary-600">A collection of case studies showcasing custom AI agents.</p>
      <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">{getAllCaseStudies().map(s => <CaseStudyCard key={s.slug} caseStudy={s} />)}</div>
    </div>
  );
}""",
    "app/contact/page.tsx": """import { ContactForm } from "@/components/features";
import { Mail, Linkedin, Twitter } from "lucide-react";

export default function ContactPage() {
  return (
    <div className="container mx-auto px-4 py-16 md:px-6 max-w-5xl">
      <h1 className="mb-12 text-center text-4xl font-bold">Get in Touch</h1>
      <div className="grid gap-12 md:grid-cols-2">
        <div className="space-y-8">
          <div><h2 className="mb-4 text-2xl font-bold">Let's build something</h2><p className="text-lg text-secondary-600">I'm currently available for freelance projects and consulting.</p></div>
          <div className="space-y-6">
            <div className="flex items-start"><Mail className="mt-1 mr-4 h-6 w-6 text-primary-600" /><div><h3 className="font-semibold">Email</h3><a href="mailto:chidiadi.works@gmail.com" className="text-secondary-600 hover:text-primary-600 hover:underline">chidiadi.works@gmail.com</a></div></div>
            <div className="flex items-start"><Linkedin className="mt-1 mr-4 h-6 w-6 text-primary-600" /><div><h3 className="font-semibold">LinkedIn</h3><a href="https://www.linkedin.com/in/chidiadi-anyamele-792b01358" target="_blank" className="text-secondary-600 hover:text-primary-600 hover:underline">Connect on LinkedIn</a></div></div>
            <div className="flex items-start"><Twitter className="mt-1 mr-4 h-6 w-6 text-primary-600" /><div><h3 className="font-semibold">X (Twitter)</h3><a href="https://x.com/tfawinner?s=21" target="_blank" className="text-secondary-600 hover:text-primary-600 hover:underline">Follow for updates</a></div></div>
          </div>
        </div>
        <div className="rounded-xl border border-secondary-200 bg-white p-6 shadow-sm"><ContactForm /></div>
      </div>
    </div>
  );
}""",
    "app/case-studies/[slug]/page.tsx": """import { notFound } from "next/navigation";
import { getAllCaseStudies, getCaseStudyBySlug } from "@/lib/data";
import { CaseStudyDetail } from "@/components/features";

export async function generateStaticParams() { return getAllCaseStudies().map((s) => ({ slug: s.slug })); }
export default function CaseStudyPage({ params }: { params: { slug: string } }) {
  const study = getCaseStudyBySlug(params.slug);
  if (!study) notFound();
  return <CaseStudyDetail caseStudy={study} />;
}""",
    "app/api/contact/route.ts": """import { NextResponse } from "next/server";
import { contactFormSchema } from "@/lib/data";
import { sendContactEmail } from "@/lib/email";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const result = contactFormSchema.safeParse(body);
    if (!result.success) return NextResponse.json({ message: "Invalid data" }, { status: 400 });
    await sendContactEmail(result.data);
    return NextResponse.json({ message: "Sent" }, { status: 200 });
  } catch (error) {
    return NextResponse.json({ message: "Error" }, { status: 500 });
  }
}"""
}

def create_project():
    for path, content in project_files.items():
        # Create directories if they don't exist
        dir_name = os.path.dirname(path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        
        # Write the file content
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip())
            
    print("✅ Project successfully created!")
    print("Run 'npm install' to install dependencies.")
    print("Run 'npm run dev' to start the server.")

if __name__ == "__main__":
    create_project()