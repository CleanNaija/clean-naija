"use client";
import { useEffect, useState } from "react";
import { Calendar } from "@/components/ui/calendar";
import Header from "../ui/Dashboard/Header";
import Nav from "../ui/Dashboard/Nav";
import Link from "next/link";
import Footer from "../ui/Home/Footer";

export default function Page() {
  const [opened, setOpened] = useState<Boolean>(false);
  const [startdate] = useState(new Date());
  const [date] = useState<Date | undefined>(new Date(2024, 11, 18));
  const [endDate, setEndDate] = useState<Date | undefined>();

  useEffect(() => {
    const newEndDate = new Date(startdate);
    newEndDate.setMonth(startdate.getMonth() + 3);
    setEndDate(newEndDate);
  }, [startdate]);

  const transactions = [
    {
      id: 1,
      name: "Lajolo Waste Disposal",
      date: "3rd December, 2024",
      amount: "#5,000.00",
      status: "Completed",
      paymentMethod: "Debit Card **** 4186",
    },
    {
      id: 2,
      name: "Lajolo Waste Disposal",
      date: "3rd December, 2024",
      amount: "#5,000.00",
      status: "Completed",
      paymentMethod: "Debit Card **** 4186",
    },
    {
      id: 3,
      name: "Lajolo Waste Disposal",
      date: "3rd December, 2024",
      amount: "#5,000.00",
      status: "Completed",
      paymentMethod: "Debit Card **** 4186",
    },
    {
      id: 4,
      name: "Lajolo Waste Disposal",
      date: "3rd December, 2024",
      amount: "#5,000.00",
      status: "Completed",
      paymentMethod: "Debit Card **** 4186",
    },
  ];

  return (
    <div className="roboto flex flex-col h-[100vh] w-[100vw] OV">
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
            <div className="h-[300px] flex-grow rounded-xl bg-[#003676] py-6 pl-6 pr-2 text-white [box-shadow:_-2px_4px_20px_0px_#00000040]">
              <div className="scrollbar scrollbar-thumb-blue-300 scrollbar-track-[#003676] h-full overflow-y-auto pr-6">
                <div className="flex items-center justify-between border-b border-white pb-4">
                  <h2 className="text-lg font-semibold">Recent Transactions</h2>
                  <div className="flex items-center gap-1 text-[0.75rem]">
                    <span>Last 7 Days</span>
                    <img src="/chv-down.svg" alt="" />
                  </div>
                </div>

                <table className="mt-1 w-full text-left">
                  <thead className="border-b border-white">
                    <tr className="text-sm text-blue-300">
                      <th className="py-2">TRANSACTION</th>
                      <th className="py-2">AMOUNT</th>
                      <th className="py-2">STATUS</th>
                      <th className="py-2">PAYMENT METHOD</th>
                    </tr>
                  </thead>
                  <tbody>
                    {transactions.map((transaction) => (
                      <tr key={transaction.id} className="border-b text-sm">
                        <td className="py-4">
                          <div className="flex items-center gap-2">
                            <img src="/car.svg" alt="" />
                            <div>
                              <p>{transaction.name}</p>
                              <p className="text-xs text-blue-300">
                                {transaction.date}
                              </p>
                            </div>
                          </div>
                        </td>
                        <td className="py-4">{transaction.amount}</td>
                        <td className="py-4">{transaction.status}</td>
                        <td className="py-4">{transaction.paymentMethod}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>

                <div className="mt-4 text-right">
                  <Link
                    href=""
                    className="text-sm text-blue-300 hover:underline"
                  >
                    View All Transactions
                  </Link>
                </div>
              </div>
            </div>

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
