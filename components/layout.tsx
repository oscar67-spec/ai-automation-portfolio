"use client";
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
};