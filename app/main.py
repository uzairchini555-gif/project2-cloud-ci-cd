from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
	return {"Mustafa ka kurta tight ho gaya"}
@app.get("/health")
def health():
	return {"Status": "Healthy"}
