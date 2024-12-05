import type { Metadata } from "next";


export const metadata: Metadata = {
  title: "Log in",
  description: "Log in to get started!",
};

export default function Layout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return <div>{children}</div>;
}
