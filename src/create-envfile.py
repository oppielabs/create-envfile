import os
import base64

encoded_env_file = os.environ.get("INPUT_ENV_FILE")

if encoded_env_file != None:
    decoded_env_file = base64.b64decode(encoded_env_file).decode('utf-8')

    with open("/github/workspace/" + str(os.environ.get("INPUT_FILE_NAME", ".env")), "w") as text_file:
        text_file.write(decoded_env_file)