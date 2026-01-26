import Link from "next/link";
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
}