import Link from "next/link";

export default function Header() {
  return (
    <header className="flex h-[15vh] w-[80%] items-center justify-between">
      <div className="flex items-center gap-[5px]">
        <img src="/logo.svg" alt="logo" className="h-[35px]" />
        <p className="rounded-[10px] bg-white px-[7px] py-[2px] text-base">
          <span className="font-[500] text-[#003676]">Clean</span>
          <span className="text-[#06402b]">Naija</span>{" "}
        </p>
      </div>

      <nav className="flex w-[40%] justify-between text-[0.8125rem] text-[#acacac]">
        <Link href="">Home</Link>
        <Link href="">Services</Link>
        <Link href="">Articles</Link>
        <Link href="">Contact</Link>
      </nav>

      <div className="flex gap-[10px] text-[0.8125rem] font-[500]">
        <button className="w-[80px] rounded-[20px] bg-white px-[10px] py-[5px] text-[#06402b]">
          Log In
        </button>
        <button className="w-[80px] rounded-[20px] bg-[#003676] px-[10px] py-[5px]">
          Sign Up
        </button>
      </div>
    </header>
  );
}
