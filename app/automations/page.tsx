import { getAllCaseStudies } from "@/lib/data";
import { CaseStudyCard } from "@/components/features";

export default function AutomationsPage() {
  return (
    <div className="container mx-auto px-4 py-16 md:px-6">
      <h1 className="mb-4 text-4xl font-bold">AI Automation Projects</h1>
      <p className="mb-12 max-w-2xl text-xl text-secondary-600">A collection of case studies showcasing custom AI agents.</p>
      <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">{getAllCaseStudies().map(s => <CaseStudyCard key={s.slug} caseStudy={s} />)}</div>
    </div>
  );
}