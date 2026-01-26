import { ContactForm } from "@/components/features";
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
}