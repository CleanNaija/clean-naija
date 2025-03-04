
export default function Footer() {
  return (
    <section className="flex w-[100%] flex-col items-center bg-[#06402b] pb-[2vh] pt-[14vh]">
      <div className="mb-[10vh] flex w-[80%] gap-[15%]">
        <div className="flex w-[30%] flex-col gap-[10px]">
          <p className="w-fit rounded-[15px] bg-white px-[10px] py-[5px] text-[0.9375rem]">
            <span className="text-[#003676]">Clean</span>
            <span className="text-[#06402b]">Naija</span>
          </p>
          <p className="text-[0.75rem] leading-tight">
            CleanNaija is your trusted partner for seamless waste management and
            recycling solutions.
            <br />
            Join us in creating cleaner communities and a healthier planet
            today!
          </p>
        </div>
        <div className="flex w-[30%] flex-col gap-[15px]">
          <h1 className="text-[0.9375rem]">Contact Us</h1>
          <div className="flex flex-col gap-[10px] text-[0.75rem]">
            <p className="flex items-center gap-[5px]" itemProp="email">
              <img src="/email.svg" alt="" className="w-[20px]" />
              cleannaija@gmail.com
            </p>
            <p className="flex items-center gap-[5px]" itemProp="telephone">
              <img src="/phone.svg" alt="" className="w-[20px]" />
              +2348148774367
            </p>
            <p className="flex items-center gap-[5px]">
              <img src="/linkedin.svg" alt="" className="w-[20px]" />
              @cleannaija
            </p>
            <p className="flex items-center gap-[5px]">
              <img src="/twitter.svg" alt="" className="w-[20px]" />
              @cleannaija
            </p>
          </div>
        </div>
      </div>
      <footer className="w-[80%]">
        <hr className="" />
        <div className="mt-[10px] flex justify-between">
          <p className="text-[12px]">
            &copy; CleanNaija 2024. All rights reserved
          </p>
          <div className="flex gap-[20px] text-[12px]">
            <p>Terms and Conditions</p>
            <p>Privacy Policy</p>
          </div>
        </div>
      </footer>
    </section>
  );
}
