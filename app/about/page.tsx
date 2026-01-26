import Link from "next/link";
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
}