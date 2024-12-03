import React from "react";
import { featuresgrid } from "@/lib/data";
import Header from "@/app/ui/Home/Header";
import Button from "@/app/ui/Home/Button";
import Footer from "@/app/ui/Home/Footer";

export default function Home() {
  const benefits: React.ReactNode[] = [
    <>
      Streamlined waste disposal processes that
      <br /> save time and effort.
    </>,
    <>
      Access to reliable recycling options for <br />a cleaner environment.
    </>,
    <>
      Empowering communities with sustainable
      <br /> waste management solutions.
    </>,
  ];

  return (
    <div className="roboto w-[100vw]">
      <section className="relative flex h-[100vh] w-[100%] flex-col items-center bg-[#06402b]">
        <Header />
        <>
          <img
            src="/truck.svg"
            alt=""
            className="absolute -left-[30px] top-[15vh] h-[18.75rem] w-[18.75rem]"
          />
          <img
            src="/r-bin.svg"
            alt=""
            className="absolute right-0 top-[35vh] h-[215px] w-[250px]"
          />
          <img
            src="/y-bin.svg"
            alt=""
            className="absolute -bottom-[10vh] left-[15vw] h-[300px] w-[300px]"
          />
          <img
            src="/b-bin.svg"
            alt=""
            className="absolute -bottom-[15vh] right-[15vw] h-[300px] w-[300px]"
          />
        </>
        <div className="mt-[5vh] flex flex-col items-center gap-[10px]">
          <p className="text-center text-[3.75rem] leading-tight">
            Building Nigeria&apos;s Cleaner
            <br />
            Tomorrow Today!
          </p>
          <p className="z-10 w-[30vw] min-w-[300px] text-center text-sm">
            Welcome to CleanNaija!
            <br />
            Our mission is to revolutionize waste management in Nigeria by
            leveraging cutting-edge technology to create an efficient,
            user-friendly system. CleanNaija bridges the gap between waste
            disposal companies and individuals, fostering a cleaner, greener
            future for everyone.
          </p>
        </div>
        <Button />
      </section>
      <section className="flex w-[100%] flex-col items-center py-[7vh]">
        <h1 className="h1-gradient z-10 text-center text-[2.5rem] font-[300]">
          Efficient Waste Management <br />
          Services
        </h1>
        <p className="text-base text-black">
          Making healthy environments the new cool!
        </p>
        <div className="grid h-[60vh] min-h-[400px] w-[90%] grid-cols-3 grid-rows-2 justify-center gap-[20px] pt-[30px] text-black">
          {featuresgrid.map((features, index) => (
            <div
              key={index}
              className="flex flex-col justify-between border-[5px] border-solid border-[#06402B] p-[15px] shadow-[8px_10px_4px_0px_#00000033]"
            >
              <div className="relative">
                <img
                  src="/rtup-arrow.svg"
                  alt=""
                  className="absolute right-0 top-0 h-[36px] w-[36px]"
                />
              </div>
              <div className="h-[60%]">
                <b className="text-base">{features.heading}</b>
                <p className="text-sm">{features.description}</p>
              </div>
            </div>
          ))}
        </div>
      </section>
      <section className="flex h-[100vh] w-[100%] flex-col items-center justify-center gap-[1.5rem] bg-[#003676]">
        <div className="w-[80%]">
          <h1 className="text-[3.125rem] text-white">
            Automate your waste disposal with
            <br /> CleanNaija in 3 steps
          </h1>
        </div>
        <div className="flex w-[80%] justify-between">
          <div className="h-[180px] w-[250px] bg-[linear-gradient(107deg,_#11437F_11.55%,_#003676_100%)] px-[30px]">
            <h1 className="text-[50px] text-[#ffffff90]">1</h1>
            <p className="text-[25px]">Sign Up</p>
          </div>
          <div className="mt-[100px] h-[180px] w-[250px] bg-[linear-gradient(107deg,_#11437F_11.55%,_#003676_100%)] px-[30px]">
            <h1 className="text-[50px] text-[#ffffff90]">2</h1>
            <p className="text-[25px]">Register</p>
          </div>
          <div className="mt-[200px] h-[180px] w-[250px] bg-[linear-gradient(107deg,_#11437F_11.55%,_#003676_100%)] px-[30px]">
            <h1 className="text-[50px] text-[#ffffff90]">3</h1>
            <p className="text-[25px]">Use our Services</p>
          </div>
        </div>
      </section>
      <section className="flex w-[100%] flex-col items-center py-[7vh]">
        <div className="flex w-[80%] items-center justify-between">
          <div className="text-[#003676]">
            <h1 className="text-[2.5rem] leading-none">
              Benefits of using <br />
              Clean Naija Include:
            </h1>
            <ul className="mt-[30px] flex flex-col gap-[10px]">
              {benefits.map((object, index) => (
                <li
                  key={index}
                  className="flex gap-[5px] text-[0.9375rem] leading-tight"
                >
                  <img
                    src="/chv-right.svg"
                    alt=""
                    className="h-[25px] w-[25px]"
                  />
                  {object}
                </li>
              ))}
            </ul>
          </div>
          <div className="w-[50%]">
            <img src="/m-truck.svg" alt="" className="h-[60vh]" />
          </div>
        </div>
      </section>
      <section className="flex w-[100%] flex-col items-center bg-[#b8f6d5] py-[14vh]">
        <div className="flex w-[80%] flex-col items-center gap-[20px]">
          <h1 className="text-center text-[3.124rem] leading-none text-[#003676]">
            Keep your environment clean effortlessly with <br />{" "}
            <b>CleanNaija</b>
          </h1>
          <p className="mt-[30px] text-center text-[1.25rem] text-[#003676]">
            Simplify waste management, connect with recycling services, and
            contribute <br /> to a healthier planet—all in one place.
          </p>
          <Button />
        </div>
      </section>
      <section className="flex w-[100%] flex-col items-center bg-[#06402b] pb-[2vh] pt-[14vh]">
        <div className="mb-[10vh] flex w-[80%] gap-[15%]">
          <div className="flex w-[30%] flex-col gap-[10px]">
            <p className="w-fit rounded-[15px] bg-white px-[10px] py-[5px] text-[0.9375rem]">
              <span className="text-[#003676]">Clean</span>
              <span className="text-[#06402b]">Naija</span>
            </p>
            <p className="text-[0.75rem] leading-tight">
              CleanNaija is your trusted partner for seamless waste management
              and recycling solutions.
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
        <Footer />
      </section>
    </div>
  );
}
