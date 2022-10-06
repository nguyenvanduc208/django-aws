from dotenv import load_dotenv
import os

load_dotenv()

print('>>>:',os.getenv('COGNITOR_USER_CLIENT_ID'))