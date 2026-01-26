import { z } from "zod";

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
export const getFeaturedCaseStudies = (count: number) => getAllCaseStudies().slice(0, count);