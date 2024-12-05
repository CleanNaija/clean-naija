"use client";
import { useRouter } from "next/navigation";
export default function Button() {
  const router = useRouter();
  const navLogin = () => {
    router.push("/login");
  };
  return (
    <button
      className="z-10 mt-[20px] flex w-fit items-center gap-[5px] rounded-[17px] bg-[#003676] px-[10px] py-[7px] text-[0.9375rem]"
      onClick={navLogin}
    >
      <p>Get Started Now!</p>
      <img src="/rt-arrow.svg" alt="" className="h-[25px] w-[25px]" />
    </button>
  );
}
