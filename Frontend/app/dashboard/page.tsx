"use client";
import { useEffect, useState } from "react";
import { Calendar } from "@/components/ui/calendar";
import Header from "../ui/Dashboard/Header";
import Nav from "../ui/Dashboard/Nav";
import Footer from "../ui/Home/Footer";
import Table from "../ui/Dashboard/Table";

export default function Page() {
  const [opened, setOpened] = useState<boolean>(false);
  const [startdate] = useState(new Date());
  const [date] = useState<Date | undefined>(new Date(2024, 11, 18));
  const [endDate, setEndDate] = useState<Date | undefined>();

  useEffect(() => {
    const newEndDate = new Date(startdate);
    newEndDate.setMonth(startdate.getMonth() + 3);
    setEndDate(newEndDate);
  }, [startdate]);

  return (
    <div className="roboto OV flex h-[100vh] w-[100vw] flex-col">
      <Header opened={opened} setOpened={setOpened} />
      <section className="mt-[10vh] flex w-[100vw] flex-grow overflow-hidden">
        <Nav opened={opened} />
        <div className="flex h-[100%] w-[100%] flex-col items-center overflow-y-scroll">
          <div className="mt-[20px] w-[100%] px-[5%] pb-[30px]">
            <p className="text-2xl text-[#06402b]">
              What do you want to do today?
            </p>
            <div className="mt-[20px] grid w-[100%] grid-cols-2 grid-rows-1 gap-5 text-[2rem] text-[#06402b]">
              <div className="flex h-[15rem] items-center gap-4 rounded-2xl bg-[#b8f6d5] p-4 [box-shadow:-2px_4px_20px_0px_#00000040]">
                <img src="/wst-dispose.svg" alt="" />
                <p>Waste Disposal</p>
              </div>
              <div className="flex h-[15rem] items-center gap-4 rounded-2xl bg-[#b8f6d5] p-4 [box-shadow:-2px_4px_20px_0px_#00000040]">
                <img src="/recycle.svg" alt="" />
                <p>Recycling</p>
              </div>
            </div>
          </div>
          <div className="mb-[20px] flex w-[100%] gap-[50px] px-[5%] pb-[20px]">
            <Table />
            <div className="flex h-fit w-fit flex-col items-center rounded-xl border-2 border-solid border-[#b8f6d5] p-[20px] text-black [box-shadow:_-2px_4px_20px_0px_#00000040]">
              <p className="text-sm text-[#003676]">Schedule</p>
              <p className="text-sm text-[#003676]">
                Next pickup on <b>{date?.getDate()}</b>
              </p>
              <Calendar
                mode="single"
                selected={date}
                fromDate={startdate}
                toDate={endDate}
                className="border-none"
              />
            </div>
          </div>
          <div className="h-[1000px_!important] w-[100%] bg-[#b8f6d5]">jnd</div>
          <Footer />
        </div>
      </section>
    </div>
  );
}
