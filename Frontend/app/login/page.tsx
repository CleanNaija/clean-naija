export default function Login() {
  return (
    <div className="roboto flex h-[100vh] w-[100vw]">
      <section className="flex h-screen w-[50%] items-center justify-center bg-[#f5f5f5]">
        <div className="flex w-[90%] max-w-[400px] flex-col items-center rounded-lg bg-white p-6 shadow-lg">
          {/* the Logo */}
          <div className="mb-6 flex items-center">
            <div className="mr-2 rounded-full border border-[#06402b] px-2 py-1 text-[0.875rem] font-bold text-[#06402b]">
              CleanNaija
            </div>
            <h1 className="text-[1.25rem] font-semibold text-[#06402b]">
              CleanNaija
            </h1>
          </div>

          {/* the Form Header */}
          <h2 className="mb-2 text-center text-[1.875rem] font-bold text-[#06402b]">
            Create an account
          </h2>
          <p className="mb-4 text-[0.875rem] text-gray-600">
            Already have an account?{" "}
            <a
              href="/login"
              className="font-medium text-[#06402b] hover:underline"
            >
              Sign In
            </a>
          </p>

          {/* the Form part*/}
          <form className="flex w-full flex-col gap-4">
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="First Name"
                className="w-1/2 rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
              />
              <input
                type="text"
                placeholder="Last Name"
                className="w-1/2 rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
              />
            </div>
            <input
              type="email"
              placeholder="Email"
              className="w-full rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
            />
            <input
              type="password"
              placeholder="Enter your password"
              className="w-full rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
            />

            <button
              type="submit"
              className="mt-2 w-full rounded-md bg-[#06402b] py-2 text-[0.875rem] font-medium text-white hover:bg-[#052a1d]"
            >
              Create account
            </button>
          </form>

          {/* the Divider */}
          <div className="my-4 flex w-full items-center">
            <hr className="w-full border-gray-300" />
            <span className="mx-2 text-[0.75rem] text-gray-400">or</span>
            <hr className="w-full border-gray-300" />
          </div>

          {/* Google Sign-Up */}
          <button className="flex w-full items-center justify-center gap-2 rounded-md border border-gray-300 py-2 text-[0.875rem] font-medium text-gray-600 hover:bg-gray-100">
            Continue with Google
          </button>
        </div>
      </section>
      <section className="flex w-[50%] items-center bg-[linear-gradient(-45deg,_#06402b_35%,_#B8F6D5_35%,_#B8F6D5_48%,_#06402b_48%,_#06402b_52%,_#B8F6D5_52%,_#B8F6D5_65%,_#06402b_65%,_#06402b)] pl-9 text-[3.125rem]">
        <p>
          <b>CleanNaija</b>
          <br />
          The Future of Waste <br />
          Disposal in Nigeria
        </p>
      </section>
    </div>
  );
}
