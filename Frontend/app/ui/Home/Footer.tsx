import { year } from "@/lib/utils";
export default function Footer() {
    return (
      <footer className="w-[80%]">
        <hr className="" />
        <div className="mt-[10px] flex justify-between">
          <p className="text-[12px]">
            &copy; CleanNaija {year}. All rights reserved
          </p>
          <div className="flex gap-[20px] text-[12px]">
            <p>Terms and Conditions</p>
            <p>Privacy Policy</p>
          </div>
        </div>
      </footer>
    );
}