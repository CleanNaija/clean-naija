import { nav } from "@/lib/data";
import clsx from "clsx";
import Link from "next/link";
export default function Nav({ opened }: { opened: Boolean }) {
  return (
    <nav
      className={clsx(
        "z-50 flex h-[100%] w-[20vw] flex-col gap-4 bg-[#06402b] text-white px-5 py-8 transition-transform duration-300 ease-in-out",
        {
          
          "hidden ": !opened,
        },
      )}
    >
      {nav.map((nav, index) => (
        <Link key={index} href={nav.href} className="flex items-center gap-1">
          <img src={nav.imagesrc} alt="" className="h-5 w-5" />
          {nav.description}
        </Link>
      ))}
    </nav>
  );
}
