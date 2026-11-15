import os
import argparse
import json
import sys
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="aiagent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": args.user_prompt,
        },
    ]

    for _ in range(20):
        messages, message = generate_content(client, messages, args)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                result_message = call_function(tool_call)
                messages.append(result_message)
                if not result_message["content"]:
                    raise Exception("No content!")
                if args.verbose:
                    print(f"-> {result_message['content']}")
        else:
            print(message.content)
            job_is_done = True
            break
        
    if not job_is_done:
        print("Not enough iterations!")
        sys.exit(1)


def generate_content(client, messages, args):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
    )
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        if response.usage:
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        else:
            raise RuntimeError("Usage property is None!")

    print(response.model)

    message = response.choices[0].message
    messages.append(message)

    return messages, message


if __name__ == "__main__":
    main()