from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
	return {"message": "Project 2 is running with CI/CD"}
@app.get("/health")
def health():
	return {"Status": "Healthy"}
