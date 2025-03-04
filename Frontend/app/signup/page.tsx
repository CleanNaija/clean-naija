"use client";
import { Registration } from "@/lib/definitions";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function Signup() {
  const router = useRouter();
  const navDash = () => {
    router.push("/dashboard");
  };

  const [state, setState] = useState<Registration>({
    first_name: "",
    last_name: "",
    username: "",
    password: "",
    email: "",
  });

  const [confirmPassword, setConfirmPassword] = useState("");
  const [validationMessages, setValidationMessages] = useState({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const formsubmit = (e: any) => {
    e.preventDefault();
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ...state }),
    };
    const fetchp = async () => {
      try {
        const response = await fetch(
          "http://localhost:8000/api/register/",
          options,
        );

        const data = await response.json();
        console.log(data);

        if (!response.ok) {
          const errorText = await response.text();
          console.error(`Server Error:, ${errorText}`);
          return;
        }
      } catch (error) {
        console.error(`Fetch Error:, ${error}`);
      }
    };
    fetchp();
  };

  const getIsFieldsValid = () => {
    return (
      state.first_name.trim() !== "" &&
      state.last_name.trim() !== "" &&
      state.email.trim() !== "" &&
      state.password.trim() !== "" &&
      confirmPassword.trim() !== "" &&
      state.password === confirmPassword &&
      validationMessages.first_name === "" &&
      validationMessages.last_name === "" &&
      validationMessages.email === "" &&
      validationMessages.password === "" &&
      validationMessages.confirmPassword === ""
    );
  };

  const validateEmail = (email: string) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const validatePassword = (password: string) => {
    const passwordRegex =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,32}$/;
    return passwordRegex.test(password);
  };

  const handleBlur = (field: string) => {
    if (state[field as keyof Registration].trim() === "") {
      setValidationMessages((prev) => ({
        ...prev,
        [field]: "Cannot be blank",
      }));
    } else {
      setValidationMessages((prev) => ({
        ...prev,
        [field]: "",
      }));
    }
  };

  const handleEmailBlur = () => {
    if (!validateEmail(state.email)) {
      setValidationMessages((prev) => ({
        ...prev,
        email: "Invalid email format",
      }));
    } else {
      setValidationMessages((prev) => ({
        ...prev,
        email: "",
      }));
    }
  };

  const handlePasswordBlur = () => {
    if (!validatePassword(state.password)) {
      setValidationMessages((prev) => ({
        ...prev,
        password:
          "Password must contain uppercase, lowercase, number, and special character",
      }));
    } else {
      setValidationMessages((prev) => ({
        ...prev,
        password: "",
      }));
    }
  };

  const handleConfirmPasswordBlur = () => {
    if (state.password !== confirmPassword) {
      setValidationMessages((prev) => ({
        ...prev,
        confirmPassword: "Passwords do not match",
      }));
    } else {
      setValidationMessages((prev) => ({
        ...prev,
        confirmPassword: "",
      }));
    }
  };

  return (
    <div className="roboto flex h-[100vh] w-[100vw]">
      <section className="flex h-screen w-[50%] items-center justify-center bg-[#f5f5f5]">
        <div className="flex w-[90%] max-w-[400px] flex-col items-center rounded-lg bg-white p-6 shadow-lg">
          {/*Logo*/}
          <div className="mb-6 flex items-center">
            <div className="mr-2 rounded-full border border-[#06402b] px-2 py-1 text-[0.875rem] font-bold text-[#06402b]">
              CleanNaija
            </div>
            <h1 className="text-[1.25rem] font-semibold text-[#06402b]">
              CleanNaija
            </h1>
          </div>

          {/*Form Header*/}
          <h2 className="mb-2 text-center text-[1.875rem] font-bold text-[#06402b]">
            Create an account
          </h2>
          <p className="mb-4 text-[0.875rem] text-gray-600">
            Already have an account?{" "}
            <Link
              href=""
              className="font-medium text-[#06402b] hover:underline"
            >
              Sign In
            </Link>
          </p>

          {/*Form*/}
          <form
            className="flex w-full flex-col gap-4 text-black"
            onSubmit={formsubmit}
          >
            <div>
              <input
                type="text"
                placeholder="First Name"
                className="w-full rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
                value={state.first_name}
                onChange={(e) =>
                  setState({ ...state, first_name: e.target.value })
                }
                onBlur={() => handleBlur("first_name")}
              />
              {validationMessages.first_name && (
                <p className="text-xs text-red-500">
                  {validationMessages.first_name}
                </p>
              )}
            </div>

            <div>
              <input
                type="text"
                placeholder="Last Name"
                className="w-full rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
                value={state.last_name}
                onChange={(e) =>
                  setState({ ...state, last_name: e.target.value })
                }
                onBlur={() => handleBlur("last_name")}
              />
              {validationMessages.last_name && (
                <p className="text-xs text-red-500">
                  {validationMessages.last_name}
                </p>
              )}
            </div>

            <div>
              <input
                type="text"
                placeholder="Username"
                className="w-full rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
                value={state.username}
                onChange={(e) =>
                  setState({ ...state, username: e.target.value })
                }
                onBlur={() => handleBlur("username")}
              />
              {validationMessages.username && (
                <p className="text-xs text-red-500">
                  {validationMessages.username}
                </p>
              )}
            </div>
            <div>
              <input
                type="email"
                placeholder="Email"
                className="w-full rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
                value={state.email}
                onChange={(e) => setState({ ...state, email: e.target.value })}
                onBlur={handleEmailBlur}
              />
              {validationMessages.email && (
                <p className="text-xs text-red-500">
                  {validationMessages.email}
                </p>
              )}
            </div>
            <div>
              <input
                type="password"
                placeholder="Enter your password"
                className="w-full rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
                value={state.password}
                onChange={(e) =>
                  setState({ ...state, password: e.target.value })
                }
                onBlur={handlePasswordBlur}
              />
              {validationMessages.password && (
                <p className="text-xs text-red-500">
                  {validationMessages.password}
                </p>
              )}
            </div>
            <div>
              <input
                type="password"
                placeholder="Confirm Password"
                className="w-full rounded-md border border-gray-300 p-2 text-[0.875rem] focus:border-[#06402b] focus:outline-none"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                onBlur={handleConfirmPasswordBlur}
              />
              {validationMessages.confirmPassword && (
                <p className="text-xs text-red-500">
                  {validationMessages.confirmPassword}
                </p>
              )}
            </div>

            <button
              type="submit"
              disabled={!getIsFieldsValid()}
              className="mt-2 w-full rounded-md bg-[#06402b] py-2 text-[0.875rem] font-medium text-white hover:bg-[#052a1d] disabled:bg-[#06402b50]"
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
