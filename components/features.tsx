"use client";
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
};