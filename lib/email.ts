import { Resend } from "resend";
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
}