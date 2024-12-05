export default function Header({
  opened,
  setOpened,
}: {
  opened: Boolean;
  setOpened: Function;
}) {
  return (
    <header className="fixed flex h-[10vh] w-[100vw] items-center gap-[1.875rem] bg-[#06402b] px-5 pr-[3.75rem]">
      <button
        onClick={() => {
          setOpened(!opened);
        }}
      >
        <img
          src={!opened ? "/menu.svg" : "/close.svg"}
          alt=""
          className="h-8 w-8"
        />
      </button>
      <div className="flex flex-grow justify-between">
        <div className="flex items-center gap-[0.3125rem]">
          <div className="h-[1.875rem] w-[1.875rem] rounded-[50%] bg-white" />
          <div className="flex flex-col gap-[0.125rem] leading-none">
            <p className="text-base">Test User</p>
            <p className="text-[0.75rem]">Hello, Welcome Back!</p>
          </div>
        </div>
        <div className="flex items-center gap-4">
          <div className="flex h-10 w-[18.75rem] items-center justify-center gap-1 rounded-[1rem] bg-white p-4">
            <img src="/search.svg" alt="" className="h-5" />
            <input
              type="text"
              placeholder="Search"
              className="w-full border-none bg-transparent py-2 pr-4 text-[#06402b] placeholder-[#acacac] outline-none"
            />
          </div>
          <div>
            <img src="/bell.svg" alt="" className="h-8 w-8" />
          </div>
        </div>
      </div>
    </header>
  );
}
