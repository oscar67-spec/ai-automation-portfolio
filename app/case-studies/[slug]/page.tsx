import { notFound } from "next/navigation";
import { getAllCaseStudies, getCaseStudyBySlug } from "@/lib/data";
import { CaseStudyDetail } from "@/components/features";

export async function generateStaticParams() { return getAllCaseStudies().map((s) => ({ slug: s.slug })); }
export default function CaseStudyPage({ params }: { params: { slug: string } }) {
  const study = getCaseStudyBySlug(params.slug);
  if (!study) notFound();
  return <CaseStudyDetail caseStudy={study} />;
}