import { transactions } from "@/lib/data";
import Link from "next/link";

export default function Table() {
  return (
    <div className="h-[300px] flex-grow rounded-xl bg-[#003676] py-6 pl-6 pr-2 text-white [box-shadow:_-2px_4px_20px_0px_#00000040]">
      <div className="h-full overflow-y-auto pr-6 scrollbar scrollbar-track-[#003676] scrollbar-thumb-blue-300">
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
          <Link href="" className="text-sm text-blue-300 hover:underline">
            View All Transactions
          </Link>
        </div>
      </div>
    </div>
  );
}
