import os
from dotenv import load_dotenv

load_dotenv()

name = os.getenv("MY_NAME")
city = os.getenv("MY_CITY")
print(f"Hello, {name} from {city}!")