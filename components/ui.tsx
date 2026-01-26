import React, { forwardRef } from "react";
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
);