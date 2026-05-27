# create virtual environtment
python -m venv .venv
# activate environtment
.\.venv\Scripts\activate
# install depedencies
pip install -r requirements.txt
# run server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload