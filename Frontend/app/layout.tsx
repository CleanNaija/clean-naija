import type { Metadata } from "next";
import "./globals.css";
import Head from "next/head";

export const metadata: Metadata = {
  title: {
    template: "%s | CleanNaija",
    default: "CleanNaija",
  },
  description: "Making healthy environments the new cool!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <Head>
        <link rel="icon" type="image/svg+xml" href="./icon.svg" />
      </Head>
      <body className="antialiased text-white overflow-x-hidden">{children}</body>
    </html>
  );
}
