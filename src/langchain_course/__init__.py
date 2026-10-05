import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# method looks for .env file and loads the environment variables from there.
load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    # print(os.environ.get("OPENAI_API_KEY"))


# This line tells Python to actually run the function
if __name__ == "__main__":
    main()
