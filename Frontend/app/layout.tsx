import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    template: "%s | CleanNaija",
    default: "CleanNaija",
  },
  description: "Making healthy environments the new cool!",
  icons: {
    icon: "/icon.svg",
    shortcut: "/icon.svg",
    apple: "/icon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="overflow-x-hidden text-white antialiased">
        {children}
      </body>
    </html>
  );
}
