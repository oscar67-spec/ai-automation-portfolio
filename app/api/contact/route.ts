import { NextResponse } from "next/server";
import { contactFormSchema } from "@/lib/data";
import { sendContactEmail } from "@/lib/email";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const result = contactFormSchema.safeParse(body);
    if (!result.success) return NextResponse.json({ message: "Invalid data" }, { status: 400 });
    await sendContactEmail(result.data);
    return NextResponse.json({ message: "Sent" }, { status: 200 });
  } catch (error) {
    return NextResponse.json({ message: "Error" }, { status: 500 });
  }
}